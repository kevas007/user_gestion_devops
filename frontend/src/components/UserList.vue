<template>
  <div class="users-container">
    <h2>Liste des Utilisateurs</h2>

    <div class="actions">
      <button @click="refreshUsers" class="btn refresh">Rafraîchir</button>
      <button @click="seedDatabase" class="btn seed">Seed Database</button>
      <button @click="showAddUserForm" class="btn add">Ajouter un utilisateur</button>
    </div>

    <div v-if="userStore.loading" class="loading">
      Chargement...
    </div>

    <div v-if="userStore.error" class="error">
      {{ userStore.error }}
    </div>

    <table v-if="userStore.users.length > 0" class="users-table">
      <thead>
        <tr>
          <th>ID</th>
          <th>Nom d'utilisateur</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="user in userStore.users" :key="user.id">
          <td>{{ user.id }}</td>
          <td>{{ user.username }}</td>
          <td class="actions">
            <button @click="editUser(user)" class="btn edit">Modifier</button>
            <button @click="confirmDelete(user.id!)" class="btn delete">Supprimer</button>
          </td>
        </tr>
      </tbody>
    </table>

    <div v-else-if="!userStore.loading" class="no-users">
      Aucun utilisateur trouvé. Utilisez le bouton "Seed Database" pour ajouter des données d'exemple.
    </div>

    <user-form
      v-if="showForm"
      :user="currentUser"
      @save="saveUser"
      @cancel="showForm = false"
    />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useUserStore } from '@/stores/user';
import UserForm from '@/components/UserForm.vue';
import type { User } from '@/types/models';

const userStore = useUserStore();
const showForm = ref<boolean>(false);
const currentUser = ref<User>({ username: '' });

function refreshUsers() {
  userStore.fetchUsers();
}

async function seedDatabase() {
  try {
    await userStore.seedDatabase();
  } catch (error) {
    // L'erreur est déjà gérée dans le store
  }
}

function showAddUserForm() {
  currentUser.value = { username: '' };
  showForm.value = true;
}

function editUser(user: User) {
  currentUser.value = { ...user };
  showForm.value = true;
}

async function confirmDelete(id: number) {
  if (confirm('Êtes-vous sûr de vouloir supprimer cet utilisateur?')) {
    await userStore.deleteUser(id);
  }
}

async function saveUser(user: User) {
  try {
    if (user.id) {
      // Mise à jour
      await userStore.updateUser(user.id, { username: user.username });
    } else {
      // Création
      await userStore.createUser({ username: user.username });
    }
    showForm.value = false;
  } catch (error) {
    // L'erreur est déjà gérée dans le store
  }
}

onMounted(() => {
  userStore.fetchUsers();
});
</script>

<style scoped>
.users-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.actions {
  margin-bottom: 20px;
}

.btn {
  padding: 8px 12px;
  margin-right: 10px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.refresh {
  background-color: #4CAF50;
  color: white;
}

.seed {
  background-color: #2196F3;
  color: white;
}

.add {
  background-color: #8BC34A;
  color: white;
}

.edit {
  background-color: #FF9800;
  color: white;
}

.delete {
  background-color: #F44336;
  color: white;
}

.loading, .error, .no-users {
  padding: 15px;
  margin: 10px 0;
  border-radius: 4px;
}

.loading {
  background-color: #E3F2FD;
}

.error {
  background-color: #FFEBEE;
  color: #D32F2F;
}

.no-users {
  background-color: #F5F5F5;
  color: #616161;
}

.users-table {
  width: 100%;
  border-collapse: collapse;
}

.users-table th, .users-table td {
  border: 1px solid #ddd;
  padding: 12px;
  text-align: left;
}

.users-table th {
  background-color: #f2f2f2;
}

.users-table tr:hover {
  background-color: #f5f5f5;
}
</style>
