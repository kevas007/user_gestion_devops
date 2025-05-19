<template>
  <div class="form-container">
    <h3>{{ formTitle }}</h3>
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="username">Nom d'utilisateur</label>
        <input
          type="text"
          id="username"
          v-model="formUser.username"
          required
          placeholder="Entrez un nom d'utilisateur"
        >
      </div>

      <div class="form-actions">
        <button type="button" class="btn cancel" @click="$emit('cancel')">Annuler</button>
        <button type="submit" class="btn save">Enregistrer</button>
      </div>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watch } from 'vue';
import type { User } from '@/types/models';

const props = defineProps<{
  user: User
}>();

const emit = defineEmits<{
  (e: 'save', user: User): void
  (e: 'cancel'): void
}>();

const formUser = ref<User>({ ...props.user });

const formTitle = computed(() => {
  return props.user.id
    ? `Modifier l'utilisateur: ${props.user.username}`
    : 'Ajouter un nouvel utilisateur';
});

watch(() => props.user, (newUser) => {
  formUser.value = { ...newUser };
});

function submitForm() {
  if (!formUser.value.username.trim()) {
    alert('Le nom d\'utilisateur ne peut pas être vide');
    return;
  }

  emit('save', { ...formUser.value });
}
</script>

<style scoped>
.form-container {
  background-color: #f9f9f9;
  padding: 20px;
  margin-top: 20px;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
}

.form-actions {
  display: flex;
  justify-content: flex-end;
  margin-top: 20px;
}

.btn {
  padding: 8px 12px;
  margin-left: 10px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.cancel {
  background-color: #757575;
  color: white;
}

.save {
  background-color: #4CAF50;
  color: white;
}
</style>
