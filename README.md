# iwata_machie_backend

## データベースのデータモデル

### モック

* **archives_mock**(<u>id</u>, body, scale, date_and_time, ip_address)
* **posts_mock**(<u>id</u>)
* **reactions_mock**(<u>id</u>, thumbsup, heart, smile, astonished, ip_address)
* **trends_mock**(<u>id</u>, thumbsup, heart, smile, astonished)

## 環境構築

### 環境変数を作成

* `./.devcontainer/.env.sample`を`./.devcontainer/.env`にコピーし、`./.devcontainer/.env`内の`MYSQL_ROOT_PASSWORD`にMySQLのルートユーザパスワード`password`を追記。

## 実行

### サービスを起動

```bash
docker-compose -f ./.devcontainer/docker-compose.yml up -d
```

### APIドキュメント

* [http://localhost:8000/docs/](http://localhost:8000/docs/)