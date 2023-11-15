## READ ME

## 起動方法

1. リポジトリ直下で下記コマンドを実行

```dockerfile
docker compose up -d
```

2. `SECRET_KEY`を生成する（初回のみ）

  - Pythonコンテナの中に入り、下記実行
  - `SECRET_KEY`がないとエラーになるため、生成後はコンテナ再起動すること

```
cd ./devchatrecipe
python generate_secretkey_setting.py > local_settings.py
```

3. `API_KEY`の設定

  - 生成された`local_settings.py`にChatGPTAPIのAPI_KEYを設定する

```
API_KEY = ""
```

4. `.frontend/.env.exapmle`を`frontend/.env.local`にリネームする

### URL
[Python]
http://localhost:8000

[Vue.js]
http://localhost:5173

## Attention

### `AttributeError: 'NoneType' object has no attribute 'group'`への対応について

- ChatGPTAPIへのリクエスト、レスポンスは翻訳している
  -  リクエスト（日→英）
  -  レスポンス（英→日）
  -  APIの利用料金を下げるため
- 翻訳については[googletrans](https://pypi.org/project/googletrans/)を使用している
- ライブラリが安定していないようでエラーが発生したり、しなかったりする
- 現在、バージョンは`4.0.0-rc1`固定にしている
- エラーが発生するようであれば、ライブラリのバージョンを変える、GitHubのIssuesを確認する等で対応すること
