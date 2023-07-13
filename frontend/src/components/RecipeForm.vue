<script setup>
import { ref, reactive } from 'vue';
import axios from "axios";
import { useRouter } from 'vue-router'
import { useGptStore } from "@/stores/gpt";

const router = useRouter()

const data = reactive({
    responses: "",
});

const {setGptResponse, getGptResponse} =useGptStore()

// 疎通確認用
const url = "http://localhost:8000/api/test";
const requestApi = async () => {
    //alert("appOverview:" + appOverview.value);
    //alert("programmingLanguage:" + programmingLanguage.value);
    //alert("useDatabase:" + useDatabase.value);
    //alert("useCloud:" + useCloud.value);
    // リクエスト(入力項目をjson)
    //const result = await axios.get(url);
    const result = await axios.post(url,{
        appOverview: appOverview.value,
        programmingLanguage: programmingLanguage.value,
        useDatabase: useDatabase.value,
        useCloud: useCloud.value
    });
    setGptResponse(result.data)
    data.responses = getGptResponse()
    router.push('/result')
};

// 検索項目
const appOverview = ref('');
const programmingLanguage = ref('');
const useDatabase = ref(false);
const useCloud = ref(false);

</script>

<template>
    <div>
        <h1>{{ data.responses }}</h1>
        <!--検索項目-->
        作りたいアプリ概要を入力*　<input type="text" v-model="appOverview" /><br>        
        言語を入力　<input type="text" v-model="programmingLanguage" /><br>
        DBを使用する　<input type="checkbox" v-model="useDatabase" /><br>
        クラウドを使用する　<input type="checkbox" v-model="useCloud" /><br>
    </div>
    <button @click="requestApi">実行</button>
</template>

<style scoped></style>
