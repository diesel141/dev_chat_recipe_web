<script setup>
import { reactive, ref } from 'vue';
import axios from "axios";
//import { useRouter } from 'vue-router'

//const router = useRouter()

const data = reactive({
    responses: "",
    input: "",
});

// 疎通確認用
const url = "http://localhost:8000/api/test";
const requestApi = async () => {
    const result = await axios.get(url);
    data.responses = result.data;
};

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
                <el-input v-model="data.input" placeholder="Please input" size="large" />
            </el-form-item>
            <el-form-item label="言語を入力">
                <el-input size="large" />
            </el-form-item>
            <div class="flex justify-between mb-2">
                <el-checkbox v-model="checked" label="DBを使用する" size="large" />
            </div>
            <div class="flex justify-between mb-2">
                <el-checkbox v-model="checked" label="クラウドを使用する" size="large" />
            </div>
            <el-button @click="requestApi" type="primary" size="large" class="w-full">作成</el-button>
        </el-form>
    </el-card>

    <div>
        {{ data.responses }}
    </div>
</template>

<style scoped></style>
