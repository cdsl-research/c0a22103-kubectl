import sys

# コマンドライン引数を取得（最初の要素はスクリプト名なので除外）
args = sys.argv[1:]

# 引数を空白区切りで出力
print(" ".join(args))

