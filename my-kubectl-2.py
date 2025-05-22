import subprocess

# kubectl get pod を実行
result = subprocess.run(["kubectl", "get", "pod", "-A"], capture_output=True, text=True)

# 結果を出力
print(result.stdout)

