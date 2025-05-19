<template>
  <div class="home">
    <h1>Bienvenue sur l'Application de Gestion</h1>
    <p>
      Cette application vous permet de gérer vos utilisateurs et autres ressources.
    </p>
    <div class="actions">
      <router-link to="/users" class="button">
        Gestion des Utilisateurs
      </router-link>
    </div>
  </div>
</template>

<style scoped>
.home {
  text-align: center;
  padding: 40px 20px;
}

.actions {
  margin-top: 30px;
}

.button {
  display: inline-block;
  padding: 12px 24px;
  background-color: #34495e;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  font-weight: bold;
  transition: background-color 0.3s;
}

.button:hover {
  background-color: #2c3e50;
}
</style>
