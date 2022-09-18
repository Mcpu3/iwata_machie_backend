# iwata_machie_backend

## 環境構築

### 環境変数を作成

* `./.devcontainer/.env.sample`を`./.devcontainer/.env`にコピーし、`./.devcontainer/.env`内の`MYSQL_ROOT_PASSWORD`にMySQLのルートユーザパスワード`password`を追記。

## 実行

### サービスを起動

```bash
docker-compose -f ./.devcontainer/docker-compose.yml up -d
```

### サイトにアクセス

* APIドキュメント
```
http://localhost:8000/docs/
```