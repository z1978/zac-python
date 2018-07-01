# encoding:utf-8
#! python3

import requests, sys, webbrowser, bs4

print('Searching....')

# google 検索(sys.argv は、コマンドラインから受け取った引数)
# python search.py "test" と打ち込むと test が取得できる
get_url_info = requests.get('http://google.com/search?q=' + ''.join(sys.argv[1:]))

# ステータスチェック
get_url_info.raise_for_status()

# 検索結果をもとに BeautifulSoup オブジェクトを作成し、検索結果一覧を取得
bs4Obj = bs4.BeautifulSoup(get_url_info.text, 'html.parser')

# 検索結果に表示されるURLリンクのリストを取得する(class r の 配下の a タグ)
linkElems = bs4Obj.select('.r a')

# webbrowser で開くページの最大を 5 ページまでに指定
num = min(5, len(linkElems))

# 検索結果を基に Web ページを開く
[webbrowser.open('http://google.com' + linkElems[i].get('href')) for i in range(num)]

print('end search')