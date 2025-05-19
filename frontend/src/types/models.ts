export interface User {
  id?: number;
  username: string;
}

export interface UserState {
  users: User[];
  loading: boolean;
  error: string | null;
}
