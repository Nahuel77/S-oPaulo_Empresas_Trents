<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import sidebar from './components/sidebar.vue'
</script>

<template>
   <sidebar />
  <RouterView />
</template>

<style scoped>
  :root{
    padding: 0;
    margin: 0;
  }
</style>
