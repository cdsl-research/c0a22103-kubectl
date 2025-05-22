import subprocess
import sys

# コマンドライン引数を取得
args = sys.argv[1:]

# kubectl コマンドを実行
result = subprocess.run(["kubectl"] + args, capture_output=True, text=True)

# 結果を出力
print(result.stdout)

