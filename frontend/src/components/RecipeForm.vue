<script setup>
import { ref, reactive } from 'vue';
import axios from "axios";
import { useRouter } from 'vue-router'
import { useGptStore } from "@/stores/gpt";
import { ElLoading } from 'element-plus'

const router = useRouter()

const data = reactive({
    responses: "",
    input: "",
});

const {setGptResponse, getGptResponse} =useGptStore()

// 疎通確認用
const url = "http://localhost:8000/api/test";
const requestApi = async () => {
    //alert("appOverview:" + appOverview.value);
    //alert("programmingLanguage:" + programmingLanguage.value);
    //alert("useDatabase:" + useDatabase.value);
    //alert("useCloud:" + useCloud.value);
    const loadingInstance = ElLoading.service({ fullscreen: true })
    // リクエスト(入力項目をjson)
    //const result = await axios.get(url);
    const result = await axios.post(url,
    {
        prompt: {
            appOverview: appOverview.value,
            programmingLanguage: programmingLanguage.value,
            useDatabase: useDatabase.value,
            useCloud: useCloud.value
        }
    }
    );
    setGptResponse(result.data)
    data.responses = getGptResponse()
    loadingInstance.close()
    //router.push('/result')
};

// 検索項目
const appOverview = ref('');
const programmingLanguage = ref('');
const useDatabase = ref(false);
const useCloud = ref(false);

</script>

<template>
    <el-card shadow="never" class="w-full max-w-md" :body-style="{ padding: 20 }">
        <div class="m-8 text-center">
            <el-link href="https://element-plus.org/en-US/" :underline="false" class="m-0">
                <img src="https://element-plus.org/images/element-plus-logo.svg" class="block w-[120px] h-[28px]"
                    alt="Element Plus" />
            </el-link>
            <h2 class="my-3">DevChatRecipe</h2>
        </div>
        <el-form label-position="top">
            <el-form-item label="作りたいアプリ概要を入力*">
                <el-input v-model="appOverview" placeholder="Please input" size="large" />
            </el-form-item>
            <el-form-item label="言語を入力">
                <el-input size="large" v-model="programmingLanguage"/>
            </el-form-item>
            <div class="flex justify-between mb-2">
                <el-checkbox v-model="useDatabase" label="DBを使用する" size="large" />
            </div>
            <div class="flex justify-between mb-2">
                <el-checkbox v-model="useCloud" label="クラウドを使用する" size="large" />
            </div>
            <el-button @click="requestApi" type="primary" size="large" class="w-full">作成</el-button>
        </el-form>
    </el-card>

    <el-card shadow="never" class="w-full max-w-md" :body-style="{ padding: 20 }">
        <h2 class="my-3">Result</h2>
        <div>
            <el-form>
                {{ data.responses.content }}
            </el-form>
        </div>
    </el-card>
</template>

<style scoped></style>
