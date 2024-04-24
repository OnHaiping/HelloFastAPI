<script setup>
</script>

<template>
  <el-container>
    <el-header>Header</el-header>
    <el-main>Main</el-main>
    <el-footer>Footer</el-footer>
  </el-container>
</template>

<style>
.el-footer {
  color: #888;
  margin-top: 15px;
  text-align: center;
  padding: 10px;
}

.el-header {
  height: 32px;
  background-color: black;
  line-height: 32px;
  text-align: center;
  padding: 0 !important;
}

.el-main {
  padding: 0 3px 0 3px !important;
}

.imdb {
  font-size: 12px;
  font-weight: bold;
  color: black;
  text-decoration: none;
  background: #f5c518;
  border-radius: 5px;
  padding: 3px 5px;
}

.float-right {
  float: right;
}
</style>