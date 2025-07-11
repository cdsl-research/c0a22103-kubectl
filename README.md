# Kubicle

## 構成
```
/home/c0a22103/
├── monitor_k8s_yaml.py
├── apply_and_log.py
├── practice/
    ├── my-kubectl-1.py
    ├── my-kubectl-2.py
    └── my-kubectl-3.py
```
## 実行する環境
- Python version：3.12.3

## 各プログラム概要

### `my-kubectl-1.py`

- **説明**:このファイルをPythonで動かすことで、ファイル名のあとに記述したものが出力される。
- **使い方**:
  <img width="922" height="76" alt="image" src="https://github.com/user-attachments/assets/ab20809d-7e96-4f94-87e9-09c454831f2e" />


### `my-kubectl-2.py`

- **説明**: このファイルをPythonで動かすことで、kubectl get podが実行されて結果が出力される。
- **使い方**:
  <img width="1146" height="328" alt="image" src="https://github.com/user-attachments/assets/a19d897f-e519-49b6-80be-37ed59c1099b" />


### `my-kubectl-3.py`

- **説明**: aliasコマンドで「kubectl」コマンドを実行したらPythonファイルが動くように設定する。それ以降、開発者が「kubectl」コマンドを実行するとPythonファイルを動かしながらPodの状況を確認することができる。
- **使い方**:
<img width="1152" height="142" alt="image" src="https://github.com/user-attachments/assets/84d7bebf-a085-4f12-955f-fc740f50a498" />



### `monitor_k8s_yaml.py`

- **説明**:このファイルをPythonで動かし続けることで、YAMLファイルが「kubectl apply」されるまでを監視することができる。さらに、そのYAMLファイルが別のディレクトリに保存される
- **使い方**:
<img width="962" height="93" alt="image" src="https://github.com/user-attachments/assets/5f19896b-5abd-43e2-bd2a-041c460567a7" />


### `apply_and_log.py`

- **説明**: このファイルをPythonで動かし続けることで、YAMLファイルの内容と出力結果、「kubectl describe」コマンドの結果をログとして保存することができる。
- **使い方**:
<img width="1457" height="396" alt="image" src="https://github.com/user-attachments/assets/29ea42b0-b3ab-472a-9375-7456848ad9df" />

