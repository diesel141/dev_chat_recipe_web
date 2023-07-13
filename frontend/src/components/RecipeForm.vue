<script lang="ts" setup>
import { ref, reactive } from 'vue';
import axios from "axios";
import { useRouter } from 'vue-router'
import { useGptStore } from "@/stores/gpt"
import { ElLoading } from 'element-plus'
import type { FormInstance, FormRules } from 'element-plus'

const router = useRouter()

const data = reactive({
    responses: "",
    input: "",
});

const {setGptResponse, getGptResponse} =useGptStore()

// 疎通確認用
const url = "http://localhost:8000/api/test";
const requestApi = async (formEl: FormInstance | undefined) => {
    if (!formEl) return
    let submitFlg = false;
    await formEl.validate((valid, fields) => {
      if (valid) {
        console.log('submit!')
        submitFlg = true;
      } else {
        console.log('error submit!', fields)
        submitFlg = false;
      }
    })

    if (!submitFlg) return
    
    // alert("appOverview:" + ruleForm.appOverview);
    // alert("programmingLanguage:" + ruleForm.programmingLanguage);
    // alert("useDatabase:" + ruleForm.useDatabase);
    // alert("useCloud:" + ruleForm.useCloud);
    const loadingInstance = ElLoading.service({ fullscreen: true })
    // リクエスト(入力項目をjson)
    //const result = await axios.get(url);
    const result = await axios.post(url,
    {
        prompt: {
            appOverview: ruleForm.appOverview,
            programmingLanguage: ruleForm.programmingLanguage,
            useDatabase: ruleForm.useDatabase,
            useCloud: ruleForm.useCloud
        }
    }
    );
    setGptResponse(result.data)
    data.responses = getGptResponse()
    loadingInstance.close()
    //router.push('/result')
};

interface RuleForm {
  appOverview: string
  programmingLanguage: string
  useDatabase: boolean
  useCloud: boolean
}

const formSize = ref('default')
const ruleFormRef = ref<FormInstance>()
const ruleForm = reactive<RuleForm>({
  appOverview: '',
  programmingLanguage: '',
  useDatabase: false,
  useCloud: false,
})

const rules = reactive<FormRules<RuleForm>>({
  appOverview: [
    { required: true, message: 'アプリ概要を入力して下さい', trigger: 'blur' },
  ],
})

const resetForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return
  formEl.resetFields()
  data.responses = ""
};


</script>

<template>
    <el-card shadow="never" class="w-full max-w-md" :body-style="{ padding: 20 }">
        <div class="m-8 text-center">
            <el-link href="https://element-plus.org/en-US/" :underline="false" class="m-0">
                <img src="https://element-plus.org/images/element-plus-logo.svg" class="block w-[120px] h-[28px]"
                    alt="Element Plus" />
            </el-link>
        </div>
        <el-form
            ref="ruleFormRef"
            :rules="rules"
            :model="ruleForm"
            :size="formSize"
            label-position="top">
            <el-form-item label="作りたいアプリ概要を入力" prop="appOverview">
                <el-input v-model="ruleForm.appOverview" size="large" />
            </el-form-item>
            <el-form-item label="言語を入力" prop="programmingLanguage">
                <el-input size="large" v-model="ruleForm.programmingLanguage"/>
            </el-form-item>
            <el-form-item class="flex justify-between mb-2" prop="useDatabase">
                <el-checkbox v-model="ruleForm.useDatabase" label="DBを使用する" size="large" />
            </el-form-item>
            <el-form-item class="flex justify-between mb-2" prop="useCloud">
                <el-checkbox v-model="ruleForm.useCloud" label="クラウドを使用する" size="large" />
            </el-form-item>
            <el-button @click="requestApi(ruleFormRef)" type="primary" size="large" class="w-full">作成</el-button>
            <el-button @click="resetForm(ruleFormRef)" size="large" class="w-full">リセット</el-button>
        </el-form>
    </el-card>
    <el-card v-if="data.responses !== ''" shadow="never" class="w-full max-w-md">
      <div class="response__container">
        <div class="response">
          <div class="text">{{ data.responses.content }}</div>
        </div>
      </div>
    </el-card>
</template>

<style scoped>
.response__container .response {
    position: relative;
    display: block;
    margin: 5px 0;
    max-width: 95%;
    float: left;
    margin-right: 5px;   /* 15px */
    clear: both;
}

.response__container .response .text {
  padding: 10px;
  border-radius: 10px;
  margin: 0;
  background-color: #D6D9D7;  /* 背景色 自分 */
  color: #000000;   /* 文字色 */
  font-size: 15px;  /* 文字サイズ */
}

</style>
