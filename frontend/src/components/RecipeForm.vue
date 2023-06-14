<script setup>
import { reactive } from 'vue';
import axios from "axios";
//import { useRouter } from 'vue-router'

//const router = useRouter()

const data = reactive({
    responses: "",
});

// 疎通確認用
const url = "http://localhost:8000/api/test";
const requestApi = async () => {
    const result = await axios.get(url);
    data.responses = result.data;
};


</script>

<template>
    <div>
        <h1>{{ data.responses }}</h1>
    </div>
    <button @click="requestApi">実行</button>
</template>

<style scoped></style>
