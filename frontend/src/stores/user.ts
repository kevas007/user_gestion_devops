import { defineStore } from 'pinia';
import axios, { AxiosError } from 'axios';
import type { User, UserState } from '@/types/models';

const api = axios.create({
  baseURL: '/api',
  headers: {
    'Content-Type': 'application/json'
  }
});

export const useUserStore = defineStore('user', {
  state: (): UserState & { seedResult: { message: string; newUsersAdded: boolean } | null } => ({
    users: [],
    loading: false,
    error: null,
    seedResult: null
  }),

  getters: {
    getUserById: (state) => (id: number) =>
      state.users.find(user => user.id === id) || null
  },

  actions: {
    async fetchUsers() {
      this.loading = true;
      this.error = null;
      try {
        const response = await api.get<User[]>('/users');
        this.users = response.data;
      } catch (err) {
        const error = err as AxiosError;
        this.error = `Erreur lors du chargement des utilisateurs : ${error.message}`;
        console.error(error);
      } finally {
        this.loading = false;
      }
    },

    async createUser(userData: Omit<User, 'id'>) {
      this.loading = true;
      this.error = null;
      try {
        const response = await api.post<User>('/users', userData);
        this.users.push(response.data);
        return response.data;
      } catch (err) {
        const error = err as AxiosError;
        this.error = `Erreur lors de la création : ${error.message}`;
        console.error(error);
        throw error;
      } finally {
        this.loading = false;
      }
    },

    async updateUser(id: number, userData: Partial<User>) {
      this.loading = true;
      this.error = null;
      try {
        const response = await api.put<User>(`/users/${id}`, userData);
        const idx = this.users.findIndex(u => u.id === id);
        if (idx !== -1) this.users[idx] = response.data;
        return response.data;
      } catch (err) {
        const error = err as AxiosError;
        this.error = `Erreur lors de la mise à jour : ${error.message}`;
        console.error(error);
        throw error;
      } finally {
        this.loading = false;
      }
    },

    async deleteUser(id: number) {
      this.loading = true;
      this.error = null;
      try {
        await api.delete(`/users/${id}`);
        this.users = this.users.filter(u => u.id !== id);
      } catch (err) {
        const error = err as AxiosError;
        this.error = `Erreur lors de la suppression : ${error.message}`;
        console.error(error);
        throw error;
      } finally {
        this.loading = false;
      }
    },

    /**
     * Lance le seeding et recharge ensuite les utilisateurs.
     * Utilise l’endpoint /api/seed (POST).
     * Retourne un objet { message, newUsersAdded }.
     */
    async seedDatabase(): Promise<{ message: string; newUsersAdded: boolean }> {
      this.loading = true;
      this.error = null;
      try {
        const { data } = await api.post<{ message: string; new_users_added: boolean }>('/seed');
        const result = {
          message: data.message,
          newUsersAdded: data.new_users_added
        };
        this.seedResult = result;
        // Recharge la liste après le seed
        await this.fetchUsers();
        return result;
      } catch (err) {
        const error = err as AxiosError;
        this.error = `Erreur lors du seeding : ${error.message}`;
        console.error(error);
        throw error;
      } finally {
        this.loading = false;
      }
    }
  }
});
