# 個人的なお気に入り音楽を聴くためのウェブアプリ

曲名とアーティスト名をデータベースに登録して表示するウェブアプリ。
ローカルにアーティスト名と曲名からYouTubeのリンクをとってくるスクリプトがあり、
それを用いてリンクを張る。
ただしAPIの仕様上、短期間に複数回APIを叩くととまずいので自動化はしていない。

# デプロイ

herokuにデプロイしています。
[リンク](https://nikutto.herokuapp.com/music_spot/)。