# iwata_machie_backend

## データベースのデータモデル

### APIのモック

* **archives_mock**(<u>id</u>, body, scale, reaction_thumbsup, reaction_heart, reaction_smile, reaction_astonished, rank_highest_thumbsup, rank_highest_heart, rank_highest_smile, rank_highest_astonished, date_and_time, ip_address)
* **posts_mock**(<u>id</u>)
* **trends_mock**(<u>id</u>, rank_thumbsup, rank_heart, rank_smile, rank_astonished)

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