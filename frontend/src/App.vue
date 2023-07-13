<script setup>
</script>

<template>
  <div class="common-layout margin_lf">
    <el-container>
      <el-header><h2 class="my-3">DevChatRecipe</h2></el-header>
      <el-main>
        <RouterView />
      </el-main>
    </el-container>
  </div>
</template>
  
<style scoped>
.margin_lf {
  margin-left: auto;
  margin-right: auto;
  width: 1000px;
}
</style>
