<template>
  <div 
    class="sidebar-wrapper" 
    @mouseenter="hover = true" 
    @mouseleave="hover = false"
  >
    <div :class="['sidebar', { open: hover }]">
      <div class="icon-container" v-if="!hover">
        <!-- Ícono mientras está cerrado -->
        <slot name="icon">☰</slot>
      </div>

      <div class="menu-items" v-if="hover">
        <slot>
          <a href="#">Home</a>
          <a href="#">Geo</a>
          <a href="#">Sectors</a>
          <a href="#">Trends</a>
          <a href="#">About</a>
        </slot>
        <div class="theme">
          <!-- <a>T</a> -->
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const hover = ref(false);
</script>

<style scoped>
.sidebar-wrapper {
  position: fixed;
  bottom: 30px;
  left: 30px;
  z-index: 9999;
}

.sidebar {
  background: #1e1e1e;
  color: white;
  border-radius: 50%;
  width: 60px;
  height: 60px;
  transition: all 0.35s ease;
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
}

/* Cuando se abre */
.sidebar.open {
  width: 220px;
  height: 280px;
  border-radius: 16px;
  padding: 20px;
  flex-direction: column;
}

/* Ícono inicial */
.icon-container {
  font-size: 24px;
}

/* Items del menú */
.menu-items {
  display: flex;
  flex-direction: column;
  gap: 12px;
  width: 100%;
  justify-content: end;
}

.menu-items a {
  color: white;
  text-decoration: none;
  font-size: 18px;
  transition: 0.2s;
}

.menu-items a:hover {
  opacity: 0.6;
}
</style>
