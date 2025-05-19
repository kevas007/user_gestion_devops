<template>
  <div id="app">
    <header>
      <h1>Gestionnaire d'Utilisateurs</h1>
    </header>

    <main>
      <user-list />
    </main>

    <footer>
      <p>Développé avec Vue.js, TypeScript et Pinia</p>
    </footer>
  </div>
</template>

<script setup lang="ts">
import UserList from '@/components/UserList.vue';
</script>

<style>
html, body {
  margin: 0;
  padding: 0;
  height: 100%;
  width: 100%;
}

body {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  overflow-x: hidden;
}

#app {
  width: 100%;
  min-height: 100vh; /* Utilise la hauteur complète de la fenêtre visible */
  display: flex;
  flex-direction: column;
}

header {
  background-color: #34495e;
  color: white;
  padding: 1rem;
  text-align: center;
  width: 100%;
}

main {
  flex: 1; /* Prend tout l'espace disponible entre header et footer */
  padding: 20px;
  width: calc(100% - 40px); /* Largeur totale moins le padding */
  box-sizing: border-box; /* Pour inclure padding dans la largeur */
}

footer {
  background-color: #f8f9fa;
  padding: 1rem;
  text-align: center;
  color: #6c757d;
  width: 100%;
}

/* Ajustement pour les composants internes */
.users-container {
  width: 100%;
  max-width: 1200px; /* Largeur maximale pour les grands écrans */
  margin: 0 auto; /* Centrage horizontal */
}
</style>
