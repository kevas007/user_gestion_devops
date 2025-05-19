<template>
  <div class="users-view">
    <h1>Gestion des Utilisateurs</h1>
    <user-list />
  </div>
</template>

<script setup lang="ts">
import UserList from '@/components/UserList.vue';
</script>

<style scoped>
.users-view {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}
</style>
