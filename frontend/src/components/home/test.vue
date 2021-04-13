<template>

    <el-container direction="vertical">
        <!--顶部-->
        <div class="x-header">
            <topNav></topNav>
        </div>
        <!--主体内容显示-->
        <el-main>
            <router-view></router-view>
        </el-main>
        <!--底部-->
        <!-- 要设计好保证页面不超过屏幕比例且能展示全部内容 -->
        <div class="x-footer">
            <pageBottom></pageBottom>
        </div>
    </el-container>
</template>
<script>
    import topNav from './header'
    import pageBottom from './footer'
    export default {
        name: 'test',
        data() {
            return {}
        },
        components: {
            'pageBottom': pageBottom,
            'topNav': topNav,
        },
    }
</script>
<style scoped>
    .el-main {
        width: 100%;
        min-height: calc(100vh - 120px);
    }

    .x-header {
        padding: 0;
        height: 100px;
    }

    .x-footer {
        height: 60px;
    }

    @import './assets/css/global.css';
</style>
