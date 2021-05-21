# DCM_gen

# 概要

[こちらのサイト](https://note.com/happaeight/n/n3b60ccd6cd54) あるモデル作成を行い、それをライブラリstreamlitでwebGUIを実装したもの

# 構成

* Dockerfile-1 : モデルを作成するためのコンテナ
* Dockerfile-2 : モデルを用いたwebGUIを実行するためのコンテナ

# 環境構築

## 起動

1. `/DCM_gen`で`docker-compose up`を実行

2. [localhost:8888](localhost:8888) にアクセス

3. 下記画像のように `generateModel.ipynb` を開き、「▶▶」をクリックしてモデルを作成

![](./Graphics/DCM01.png)

4. モデルの作成が終わるまで待つ

## 実行

1. [localhost:808](localhpst:808)にアクセス

2. 入力欄に類似度の高い単語のリストが欲しい単語を入力すると、リストが表示される。動作例は下記のgifのとおり。

![](./Graphics/sample.gif)
