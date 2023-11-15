<script lang="ts" setup>
import { ref, reactive } from 'vue';
import axios from "axios";
import { useRouter } from 'vue-router'
import { useGptStore } from "@/stores/gpt"
import { ElLoading } from 'element-plus'
import type { FormInstance, FormRules } from 'element-plus'
import { Buffer } from 'buffer'

const router = useRouter()

const data = reactive({
  responses: "",
  input: "",
  voice: ""
});

// キャラクタ(口)リップシンク用
const mouse = reactive({
  imgUrl: "/src/assets/img/mouse_close.png"
});

const { setGptResponse, getGptResponse } = useGptStore()

let ctx = null // AudioContext: Nodeの作成、音声のデコードの制御などを行う
let audioSrc = null // AudioBufferSourceNode: 音声入力ノード
let analyser = null // AnalyserNode: 音声解析ノード
let sampleInterval = null
let prevSpec = 0 // 前回のサンプリングで取得したスペクトルの配列

/* 音声データをAudioBufferに変換 */
const preparedBuffer = async (arrayBuffer) => {
  ctx = new AudioContext()
  const audioBuffer = await ctx.decodeAudioData(arrayBuffer)
  return audioBuffer
}

/* 入力ノード、Analyserノードを生成し、出力層に接続 */
const buildNodes = (audioBuffer) => {
  audioSrc = new AudioBufferSourceNode(ctx, { buffer: audioBuffer })
  analyser = new AnalyserNode(ctx)
  analyser.fftSize = 512
  audioSrc.connect(analyser).connect(ctx.destination)
}

/* スペクトルをもとにリップシンクを行う */
const syncLip = (spectrums) => {
  let totalSpec = 0
  const totalSpectrum = spectrums.reduce(function (a, x) { return a + x })
  if (totalSpectrum > prevSpec) {
    mouse.imgUrl = "/src/assets/img/mouse_open.png"
  } else if (prevSpec - totalSpectrum < 1000) {
    mouse.imgUrl = "/src/assets/img/mouse_open_light.png"
  } else {
    mouse.imgUrl = "/src/assets/img/mouse_close.png"
  }
  prevSpec = totalSpectrum
}

/* 音声再生処理 */
const playVoice = async (arrayBuffer) => {
  const audioBuffer = await preparedBuffer(arrayBuffer) // audioBuffer取得
  buildNodes(audioBuffer) // 入力、解析ノード作成
  audioSrc.start() // 音声再生開始

  // 50ms毎に音声のサンプリング→解析→リップシンクを行う
  sampleInterval = setInterval(() => {
    let spectrums = new Uint8Array(analyser.fftSize)
    analyser.getByteFrequencyData(spectrums)
    syncLip(spectrums)
  }, 50)

  // 音声終了時のコールバック： リソースの開放、無効化していたボタンを有効化する
  audioSrc.onended = () => {
    clearInterval(sampleInterval)
    audioSrc = null
    ctx.close()
    ctx = null
    prevSpec = 0
  }
}

// chatGPT&Voicevox実行
const requestApi = async (formEl: FormInstance | undefined) => {

  // 入力チェック
  if (!formEl) return
  let validFlg = false;
  await formEl.validate((valid, fields) => {
    if (!valid) {
      validFlg = true;
    }
  })
  if (validFlg) return

  // ローディング画面を表示
  const loadingInstance = ElLoading.service({ fullscreen: true })

  // chatGPT実行
  const result = await axios.post(import.meta.env.VITE_API_URL_BASE + import.meta.env.VITE_API_CHAT_GPT,
    {
      prompt: {
        appOverview: ruleForm.appOverview,
        programmingLanguage: ruleForm.programmingLanguage,
        platform: ruleForm.platform,
        useDatabase: ruleForm.useDatabase,
        useCloud: ruleForm.useCloud
      }
    }
  );

  // voicevox実行(1)
  const result2 = await axios.post(import.meta.env.VITE_API_VOICEVOX_URL_BASE + import.meta.env.VITE_API_VOICEVOX_AUDIO_QUERY
    .replace("[content]", result.data.content));
  let request = axios.create({
    responseType: 'arraybuffer',
    responseEncoding: 'binary'
  })

  // voicevox実行(2)
  const result3 = await axios.post(import.meta.env.VITE_API_VOICEVOX_URL_BASE + import.meta.env.VITE_API_VOICEVOX_SYNTHESIS
    , result2.data, { responseType: 'arraybuffer', });
  const afterText = Buffer.from(result3.data, 'binary').toString('base64')
  data.voice = "data:audio/wav;base64," + afterText
  const music = new Audio(data.voice);
  music.play();

  // リップシンク
  playVoice(result3.data)

  // chatGPT結果画面表示
  setGptResponse(result.data)
  data.responses = getGptResponse()

  // ローディング画面を非表示
  loadingInstance.close()
};

interface RuleForm {
  appOverview: string
  programmingLanguage: string
  platform: string
  useDatabase: boolean
  useCloud: boolean
}

const formSize = ref('default')
const ruleFormRef = ref<FormInstance>()
const ruleForm = reactive<RuleForm>({
  appOverview: '',
  programmingLanguage: 1,
  platform: 1,
  useDatabase: false,
  useCloud: false,
})

const rules = reactive<FormRules<RuleForm>>({
  appOverview: [
    { required: true, message: 'アプリ概要を入力して下さい', trigger: 'blur' },
    { max: 50, message: 'アプリ概要を50文字以内で入力してください', trigger: 'blur' }
  ],
})

// リセット処理
const resetForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return
  formEl.resetFields()
  data.responses = ""
};

const programmingLanguageList = [
  {
    "id": 1,
    "dispName": "指定なし",
    "prompt": "unspecified"
  },
  {
    "id": 2,
    "dispName": "Python",
    "prompt": "Python"
  },
  {
    "id": 3,
    "dispName": "PHP",
    "prompt": "PHP"
  },
  {
    "id": 4,
    "dispName": "Ruby",
    "prompt": "Ruby"
  },
  {
    "id": 5,
    "dispName": "JavaScript",
    "prompt": "JavaScript"
  },
  {
    "id": 6,
    "dispName": "TypeScript",
    "prompt": "TypeScript"
  },
  {
    "id": 7,
    "dispName": "Java",
    "prompt": "Java"
  },
  {
    "id": 8,
    "dispName": "Kotlin",
    "prompt": "Kotlin"
  },
  {
    "id": 9,
    "dispName": "Scala",
    "prompt": "Scala"
  },
  {
    "id": 10,
    "dispName": "C#",
    "prompt": "C#"
  },
  {
    "id": 11,
    "dispName": "Go",
    "prompt": "Go"
  },
  {
    "id": 12,
    "dispName": "Rust",
    "prompt": "Rust"
  },
  {
    "id": 13,
    "dispName": "Swift",
    "prompt": "Swift"
  }
];

const platformList = [
  {
    "id": 1,
    "dispname": "指定なし",
    "prompt": "unspecified"
  },
  {
    "id": 2,
    "dispname": "WEBブラウザ",
    "prompt": "WEB"
  },
  {
    "id": 3,
    "dispname": "スマートフォン",
    "prompt": "Mobile Application"
  },
  {
    "id": 4,
    "dispname": "コンソール",
    "prompt": "Console Application"
  },
  {
    "id": 5,
    "dispname": "デスクトップ",
    "prompt": "Desktop Application"
  },
  {
    "id": 6,
    "dispname": "クロスプラットフォーム",
    "prompt": "Cross Platform Application"
  }
];
</script>

<template>
  <el-card shadow="never" class="w-full max-w-md" :body-style="{ padding: 20 }">
    <div class="m-8 text-center">
      <el-link href="https://element-plus.org/en-US/" :underline="false" class="m-0">
        <img src="https://element-plus.org/images/element-plus-logo.svg" class="block w-[120px] h-[28px]"
          alt="Element Plus" />
      </el-link>
    </div>
    <el-form ref="ruleFormRef" :rules="rules" :model="ruleForm" :size="formSize" label-position="top">

      <!-- キャラクタ表示 -->
      <img class="body" src="@/assets/img/body.gif" alt="" />
      <img class="eye" src="@/assets/img/eye.gif" />
      <img class="mouse" :src="mouse.imgUrl" />

      <!-- 入力項目 -->
      <el-form-item label="作りたいアプリ概要を入力" prop="appOverview">
        <el-input v-model="ruleForm.appOverview" size="large" />
      </el-form-item>
      <el-form-item label="言語を入力" prop="programmingLanguage">
        <el-select v-model="ruleForm.programmingLanguage" value-key="id">
          <el-option v-for="programmingLanguage in programmingLanguageList" :key="programmingLanguage.id"
            :label="`${programmingLanguage.dispName}`" :value="programmingLanguage.id" />
        </el-select>
      </el-form-item>
      <el-form-item label="プラットフォームを入力" prop="platform">
        <el-select v-model="ruleForm.platform" value-key="id">
          <el-option v-for="platform in platformList" :key="platform.id" :label="`${platform.dispname}`"
            :value="platform.id" />
        </el-select>
      </el-form-item>
      <el-form-item class="flex justify-between mb-2" prop="useDatabase">
        <el-checkbox v-model="ruleForm.useDatabase" label="DBを使用する" size="large" />
      </el-form-item>
      <el-form-item class="flex justify-between mb-2" prop="useCloud">
        <el-checkbox v-model="ruleForm.useCloud" label="クラウドを使用する" size="large" />
      </el-form-item>

      <!-- ボタン -->
      <el-button @click="requestApi(ruleFormRef)" type="primary" size="large" class="w-full">作成</el-button>
      <el-button @click="resetForm(ruleFormRef)" size="large" class="w-full">リセット</el-button>

    </el-form>
  </el-card>
  <el-card v-if="data.responses !== ''" shadow="never" class="w-full max-w-md margin">
    <div class="response__container">
      <div class="response">
        <div class="text">{{ data.responses.content }}</div>
      </div>
    </div>
  </el-card>
</template>

<style scoped>
.margin {
  margin-top: 20px;
}

.response__container .response {
  position: relative;
  display: block;
  margin: 10px 0;
  margin-top: -5px;
  max-width: 95%;
  float: left;
  margin-right: 5px;
  clear: both;
}

.response__container .response .text {
  padding: 10px;
  border-radius: 10px;
  margin: 0;
  background-color: #D6D9D7;
  /* 背景色 自分 */
  color: #000000;
  /* 文字色 */
  font-size: 15px;
  /* 文字サイズ */
  white-space: pre-wrap;
  /* 改行 */
}

.control-panel {
  position: relative;
  z-index: 2;
}

.character {
  position: relative;
}

img {
  position: absolute;
}

img.body {
  top: 220px;
  left: 320px;
  width: 150px;
  height: 330px;
}

img.eye {
  top: 283px;
  left: 350px;
  width: 90px;
  height: 30px;
}

img.mouse {
  z-index: 1;
  top: 324px;
  left: 372px;
  width: 47px;
  height: 25px;
}

img.face {
  z-index: 1;
}
</style>