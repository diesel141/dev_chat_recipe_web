FROM node:16.18-alpine
WORKDIR /app
RUN apk update
COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile
EXPOSE 5173
ENTRYPOINT yarn dev