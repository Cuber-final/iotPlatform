import Vue from 'vue'
import store from '../store/index.js'
import Router from 'vue-router'

//路由懒加载
const Home = resolve => {
    require.ensure(['../components/home/test.vue'], () => {
        resolve(require('../components/home/test.vue'));
    });
};
const Introduce = resolve => {
    require.ensure(['../components/home/introduce.vue'], () => {
        resolve(require('../components/home/introduce.vue'));
    });
};

const NotFound = resolve => {
    require.ensure(['../components/notFound.vue'], () => {
        resolve(require('../components/notFound.vue'));
    });
};
const Login = resolve => {
    require.ensure(['../components/user/login.vue'], () => {
        resolve(require('../components/user/login.vue'));
    });
};

const Register = resolve => {
    require.ensure(['../components/user/register.vue'], () => {
        resolve(require('../components/user/register.vue'));
    });
};


import Developer from '../components/developer/index'
import Dashboard from '../components/developer/dashboard'
import Charts from '../components/developer/charts'
import Devices from '../components/developer/device'
import Streams from '../components/developer/stream'
import Triggers from '../components/developer/trigger'
import Console from '../components/developer/console'

//启用路由管理
Vue.use(Router)

const router = new Router({
    mode: 'history',
    routes: [
        //访问主页时重定向加载introduce模块
        { path: '/', redirect: { path: '/introduce' } },
        {
            name: 'test',
            path: '/',
            component: Home,
            children: [
                { name: 'introduce', path: 'introduce', component: Introduce },
            ]
        },
        { path: '/developer', redirect: { path: '/developer/dashboard' } },
        {
            name: 'developer',
            path: '/developer',
            component: Developer,
            meta: {
                requiresAuth: true
            },
            children: [
                { name: 'dashboard', path: 'dashboard', component: Dashboard, meta: { requiresAuth: true } },
                { name: 'charts', path: 'charts', component: Charts, meta: { requiresAuth: true } },
                { name: 'devices', path: 'devices', component: Devices, meta: { requiresAuth: true } },
                { name: 'streams', path: 'streams', component: Streams, meta: { requiresAuth: true } },
                { name: 'console', path: 'console', component: Console, meta: { requiresAuth: true } },
                { name: 'triggers', path: 'triggers', component: Triggers, meta: { requiresAuth: true } },
            ]
        },
        {
            path: '*',
            component: NotFound
        },
        { name: 'login', path: '/login', component: Login },
        { name: 'register', path: '/register', component: Register },
    ]
})

router.beforeEach((to, from, next) => {
    //获取store里面的token
    let token = store.state.token;
    //判断要去的路由有没有requiresAuth
    if (to.meta.requiresAuth) {

        if (token) {
            next();
        } else {
            next({
                path: '/login',
                query: { redirect: to.fullPath } // 将刚刚要去的路由path（却无权限）作为参数，方便登录成功后直接跳转到该路由
            });
        }

    } else {
        next(); //如果无需token,那么随它去吧
    }
});
//将路由挂载
export default router;
