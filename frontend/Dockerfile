FROM node:16.18-alpine
WORKDIR /app
RUN apk update
COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile
RUN npm install eslint
RUN npm install --save-dev @typescript-eslint/parser
EXPOSE 5173
ENTRYPOINT yarn dev