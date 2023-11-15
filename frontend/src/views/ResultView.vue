<script setup>
import { useGptStore } from "@/stores/gpt";

const { getGptResponse } = useGptStore()

</script>

<template>
    <div>
        {{ getGptResponse() }}
        <h1>This is an Result page</h1>
    </div>
</template> 