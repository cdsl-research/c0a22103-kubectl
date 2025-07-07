import os
import time
import shutil
import datetime

# 監視するディレクトリ（kubectl apply の YAML）
watch_dir = "/home/c0a22103"

# バックアップ先ディレクトリ
backup_dir = "/home/c0a22103/k8s-backup"
os.makedirs(backup_dir, exist_ok=True)

# 変更を監視する辞書
file_cache = {}

def monitor_directory():
    while True:
        for filename in os.listdir(watch_dir):
            filepath = os.path.join(watch_dir, filename)
            
            # YAMLファイルのみ監視
            if filename.endswith(".yaml") and os.path.isfile(filepath):
                last_modified = os.path.getmtime(filepath)

                # 新規作成 or 更新された場合
                if filename not in file_cache or file_cache[filename] < last_modified:
                    file_cache[filename] = last_modified
                    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    backup_filepath = os.path.join(backup_dir, f"{timestamp}_{filename}")
                    
                    shutil.copy(filepath, backup_filepath)
                    print(f"Backup created: {backup_filepath}")

        # 監視間隔（10秒ごとにチェック）
        time.sleep(10)

if __name__ == "__main__":
    print(f"Monitoring {watch_dir} for changes...")
    monitor_directory()

