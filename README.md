## READ ME

## 起動方法

1. リポジトリ直下で下記コマンドを実行

```dockerfile
docker compose up -d
```

[Python]
http://localhost:8000

[Vue.js]
http://localhost:5173


2. `SECRET_KEY`を生成する（初回のみ）

  - Pythonコンテナの中に入り、下記実行
  - `SECRET_KEY`がないとエラーになるため、生成後はコンテナ再起動すること

```
cd ./devchatrecipe
python generate_secretkey_setting.py > local_settings.py
```


