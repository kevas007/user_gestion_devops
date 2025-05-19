FROM node:18-alpine as build-stage

WORKDIR /app

# Copier les fichiers package*.json et installer les dépendances
COPY package*.json ./
RUN npm install

# Copier les fichiers du projet et construire l'application
COPY . .
RUN npm run build

# Étape de production avec Nginx
FROM nginx:stable-alpine as production-stage

# Copier les fichiers de build
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Configurer Nginx pour le routing SPA
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]