import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { createVuetify } from 'vuetify';
import * as components from 'vuetify/components';

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)
// TODO:一括importしているのでビルドサイズが大きくなる、最終的に必要なコンポーネントのみにしたい
app.use(createVuetify({
    components,
}))

app.mount('#app')
