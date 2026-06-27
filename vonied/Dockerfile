FROM node:lts-alpine

WORKDIR /app

COPY package.json pnpm-lock.yaml ./

RUN corepack enable; corepack install; pnpm install

COPY . .

RUN pnpm run build
