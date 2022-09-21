# iwata_machie_backend

## データベースのデータモデル

* **archives**(<u>id</u>, body, label, scale, date_and_time, e_mail)
* **posts**(<u>id</u>)
* **reactions**(<u>id</u>, thumbsup, heart, smile, astonished, e_mail)
* **trends**(<u>id</u>, thumbsup, heart, smile, astonished)

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