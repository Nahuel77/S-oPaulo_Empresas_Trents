<script setup lang="ts">
/*
  Acá irían futuras props o imports de componentes:
  import LineChart from '@/components/LineChart.vue'
  import BarChart from '@/components/BarChart.vue'
  etc.
*/
</script>

<template>
  <div class="home">

    <!-- HEADER -->
    <header class="header">
      <h1>SP-Empresas-Trends</h1>
      <p>
        Dashboard analyzing new businesses opening in the city of
        <strong>São Paulo</strong>
      </p>
    </header>

    <!-- GRID PRINCIPAL -->
    <div class="grid">

      <!-- CARD 1: Total -->
      <div class="card big-number">
        <h2>5,267</h2>
        <p>New Businesses</p>
      </div>

      <!-- CARD 2: Línea -->
      <div class="card">
        <h3>New Businesses Over Time</h3>
        <div class="placeholder">[ Line Chart ]</div>
      </div>

      <!-- CARD 3: Mapa -->
      <div class="card">
        <h3>New Businesses by Neighborhood</h3>
        <div class="placeholder">[ Map Placeholder ]</div>
      </div>

      <!-- CARD 4: Sectores -->
      <div class="card">
        <h3>Top Sectors</h3>
        <div class="placeholder">[ Bar Chart ]</div>
      </div>

    </div>

  </div>
</template>

<style scoped>
.home {
  padding: 0;
  font-family: Inter, sans-serif;
  display: flex;
  flex-direction: column;
}

/* ---------- Header ---------- */
.header {
  width: 100vw;
  text-align: left;
  margin-bottom: 40px;
  background-color: var(--color-primary);
  padding: 10px 40px;
}

.header h1 {
  font-size: 32px;
  font-weight: 700;
  margin-bottom: 8px;
  color: var(--color-text-light);
}

.header p {
  font-size: 17px;
  color: var(--color-text-light);
}

/* ---------- Grid ---------- */
.grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-auto-rows: minmax(260px, auto);
  gap: 24px;
}

/* ---------- Cards ---------- */
.card {
  background: white;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.05);
}

.big-number {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.big-number h2 {
  font-size: 56px;
  margin: 0;
  font-weight: 700;
}

.big-number p {
  font-size: 18px;
  margin-top: 6px;
  color: #555;
}

/* ---------- Placeholder para charts/mapas ---------- */
.placeholder {
  margin-top: 20px;
  height: 180px;
  border-radius: 8px;
  background: #e8eef5;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #637085;
  font-size: 14px;
  border: 1px dashed #b9c3d0;
}
</style>
