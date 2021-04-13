<template>
    <el-menu class="el-menu-demo" mode="horizontal" @select="handleSelect" background-color="#282c34" text-color="#ffffff" :default-active="$route.path" router>
        <el-row>
            <el-col :xs="6" :sm="4" :md="3" :lg="2" :xl="1">
                <el-menu-item index="introduce">
                    Logo
                </el-menu-item>

            </el-col>
            <el-col :xs="6" :sm="4" :md="3" :lg="2" :xl="1" :offset="1" class="hidden-md-and-down">
                <el-menu-item index="introduce">
                    <span>平台介绍</span>
                </el-menu-item>

            </el-col>

            <el-col :xs="6" :sm="4" :md="3" :lg="2" :xl="1" class="hidden-md-and-down">
                <el-menu-item index="document">
                    <span>接入指南</span>
                </el-menu-item>
            </el-col>
            <el-col :xs="6" :sm="4" :md="3" :lg="2" :xl="1" class="hidden-md-and-down">
                <el-menu-item index="resource">
                    <span>资源下载</span>
                </el-menu-item>
            </el-col>


            <el-col class="hidden-md-and-down" :xs="8" :sm="4" :md="3" :lg="2" :xl="1">
                <el-menu-item index="/developer">
                    <span>开发者中心</span>
                </el-menu-item>
            </el-col>


            <el-col :xs="6" :sm="4" :md="3" :lg="2" :xl="1" :offset="4">
                <el-menu-item index="/login">
                    <span>登录</span>
                </el-menu-item>
            </el-col>

            <el-col :xs="6" :sm="4" :md="3" :lg="2" :xl="1">
                <el-submenu index="4">
                    <template slot="title">
                        <div class="head-img">
                          <i class="fa fa-user fa-lg"></i>
                        </div>
                    </template>
                    <el-menu-item index="4-1">个人中心</el-menu-item>
                    <el-menu-item index="4-2">账户设置</el-menu-item>
                    <el-menu-item index="4-3">退出</el-menu-item>
                </el-submenu>
            </el-col>
            <!-- 当屏幕比例较小时将部分导航选项嵌入下拉菜单中显示 -->

            <el-col class="hidden-md-and-up" :span="6" :xs="6" :sm="4" :md="3" :lg="2" :xl="1">
                <el-submenu index="2">
                    <template slot="title">更多</template>
                    <el-menu-item index="2-1">接入指南</el-menu-item>
                    <el-menu-item index="2-2">平台介绍</el-menu-item>
                    <el-menu-item index="2-3">资源下载</el-menu-item>
                </el-submenu>
            </el-col>


        </el-row>
    </el-menu>

</template>
<script>
    export default {
        name: "HTopNavBar",
        data() {
            return {
            }
        },
        methods: {
            handleSelect(key, keyPath) {
                console.log(key, keyPath);
            }
        }
    }
</script>
<style scoped>
    a {
        text-decoration: none;
    }

    .router-link-active {
        text-decoration: none;
    }


    .bg-purple-dark {
        background: #99a9bf;
    }

    .bg-purple {
        background: #d3dce6;
    }

    .bg-purple-light {
        background: #e5e9f2;
    }

    .grid-content {
        border-radius: 4px;
        min-height: 36px;
    }

    .el-icon-arrow-down {
        padding: 5px 0;
        font-size: 12px;
    }
</style>
