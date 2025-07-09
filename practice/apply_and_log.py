import subprocess
import os
import datetime

# 設定
yaml_dir = "/home/c0a22103/k8s-backup"  # YAMLファイルがあるディレクトリ
log_dir = "/home/c0a22103/k8s-logs"   # ログを保存するディレクトリ

# ログディレクトリを作成
os.makedirs(log_dir, exist_ok=True)

def apply_yaml(file_path):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(log_dir, f"{timestamp}_{os.path.basename(file_path)}.log")

    # `kubectl apply` を実行
    result = subprocess.run(["kubectl", "apply", "-f", file_path], capture_output=True, text=True)

    # YAML内容 + 実行結果を保存
    with open(log_file, "w") as f:
        f.write(f"=== Applied: {file_path} ===\n\n")
        f.write(f"=== YAML Content ===\n")
        with open(file_path, "r") as yaml_file:
            f.write(yaml_file.read())
        
        f.write("\n=== Kubectl Output ===\n")
        f.write(result.stdout)
        
        f.write("\n=== Kubectl Error ===\n")
        f.write(result.stderr)

    print(f"Applied {file_path}, log saved to {log_file}")

# 監視ディレクトリ内の **すべてのYAMLファイル** を処理
yaml_files = [os.path.join(yaml_dir, f) for f in os.listdir(yaml_dir) if f.endswith(".yaml")]

if yaml_files:
    for yaml_file in yaml_files:
        apply_yaml(yaml_file)
else:
    print(f"No YAML files found in {yaml_dir}")

