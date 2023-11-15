import { defineStore } from 'pinia'

// vue2(vuex) ⇒ vue3(pinia)
export const useGptStore = defineStore('gpt', () => {
  // 変数
  let gptResponse

  //getters
  const getGptResponse = () => gptResponse

  //setters
  const setGptResponse = (res) => gptResponse = res

  return { getGptResponse, setGptResponse }
})