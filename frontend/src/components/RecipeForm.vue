<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router'


const msg = ref('Form page');
const router = useRouter()

const requestApi = () => {
    console.log('requestApi');
    router.push('/result')
}

</script>

<template>
    <div>
        <h1>{{ msg }}</h1>
    </div>
    <button @click="requestApi">実行</button>
</template>

<style scoped></style>
