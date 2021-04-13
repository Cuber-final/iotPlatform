<template>
    <el-row type="flex" class="row-bg" justify="center" >
        <el-col :xs="8" :sm="6" :md="4" :lg="3" :xl="1">
            <div class="grid-content bg-purple"></div>
        </el-col>
        <el-col :xs="4" :sm="6" :md="8" :lg="9" :xl="11">
            <div class="grid-content bg-purple-light"></div>
        </el-col>
        <el-col :xs="4" :sm="6" :md="8" :lg="9" :xl="11">
            <div class="grid-content bg-purple"></div>
        </el-col>
        <el-col :xs="8" :sm="6" :md="4" :lg="3" :xl="1">
            <div class="grid-content bg-purple-light"></div>
        </el-col>
    </el-row>
</template>

<script>
    export default {
        //component的名字不要和html原有的属性标签重复，会报错
        name: "pageBottom"
    }
</script>

<style scoped>
    a {
        text-decoration-line: none;
    }

    .el-col {
        border-radius: 4px;
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
        min-height: 30px;
    }

    .el-row {
        height: 60px;
        padding: 10px 0;
        margin: 0 0;
        height: 40px;
        background-color: #f9fafc;
    }
</style>
