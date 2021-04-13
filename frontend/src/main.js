import Vue from 'vue'
import App from './App'
import router from './router'
//引入elementUI
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css';
//用于在某些条件下隐藏元素，比如移动端页面实现侧边栏的缩小/隐藏
import 'element-ui/lib/theme-chalk/display.css';
import store from './store'

//引入echarts,指定版本4.2.0
import echarts from 'echarts'
Vue.prototype.$echarts = echarts;
import SIdentify from './components/user/identify'

Vue.use(SIdentify);

Vue.config.productionTip = false
Vue.use(ElementUI);
//引入axios
import Axios from 'axios'
//设置全局URL
Axios.defaults.baseURL = 'http://127.0.0.1:8000/';
Vue.prototype.$axios = Axios

/* eslint-disable no-new */
new Vue({
    el: '#app',
    router,
    store,
    Axios,
    components: { App },
    template: '<App/>'
})
