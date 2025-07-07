import subprocess
import os
import datetime

# 設定
yaml_dir = "/home/c0a22103/k8s-backup"  # YAMLファイルがあるディレクトリ
log_dir = "/home/c0a22103/k8s-logs"   # ログを保存するディレクトリ

# ログディレクトリを作成
os.makedirs(log_dir, exist_ok=True)

def apply_yaml(file_path):
    # ファイル名を取得してログファイルを設定
    yaml_filename = os.path.basename(file_path)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(log_dir, f"{timestamp}_{yaml_filename}.log")

    # `kubectl apply` を実行
    apply_result = subprocess.run(["kubectl", "apply", "-f", file_path], capture_output=True, text=True)

    # `kubectl describe` を実行（リソースの詳細を記録）
    resource_name = yaml_filename.replace(".yaml", "")  # 仮のリソース名推測（変更が必要なら適宜修正）
    describe_result = subprocess.run(["kubectl", "describe", "-f", file_path], capture_output=True, text=True)

    # ログファイルに結果を記録
    with open(log_file, "w") as f:
        f.write(f"=== Applied: {file_path} ===\n\n")
        
        # YAMLの内容を記録
        f.write("=== YAML Content ===\n")
        with open(file_path, "r") as yaml_file:
            f.write(yaml_file.read())
        
        # `kubectl apply` の結果を記録
        f.write("\n=== Kubectl Apply Output ===\n")
        f.write(apply_result.stdout)
        
        f.write("\n=== Kubectl Apply Error ===\n")
        f.write(apply_result.stderr)

        # `kubectl describe` の結果を記録
        f.write("\n=== Kubectl Describe Output ===\n")
        f.write(describe_result.stdout)

        f.write("\n=== Kubectl Describe Error ===\n")
        f.write(describe_result.stderr)

    print(f"Applied {file_path}, log saved to {log_file}")

# 監視ディレクトリ内の **すべてのYAMLファイル** を処理
yaml_files = [os.path.join(yaml_dir, f) for f in os.listdir(yaml_dir) if f.endswith(".yaml")]

if yaml_files:
    for yaml_file in yaml_files:
        apply_yaml(yaml_file)
else:
    print(f"No YAML files found in {yaml_dir}")

