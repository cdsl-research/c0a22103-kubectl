# YAMLファイル収集プロジェクト

## 📁 構成
```
/home/c0a22103/
├── monitor_k8s_yaml.py
├── apply_and_log.py
├── practice/
    ├── my-kubectl-1.py
    ├── my-kubectl-2.py
    └── my-kubectl-3.py
```

## 各プログラム概要

### `my-kubectl-1.py`

- **説明**:このファイルをPythonで動かすことで、ファイル名のあとに記述したものが出力される。
- **使い方**:
  ```bash
  c0a22103@c0a22103-practice:~/c0a22103-kubectl/practice$ python3 my-kubectl-1.py apple banana
  apple banana 
  ```

### `my-kubectl-2.py`

- **説明**: このファイルをPythonで動かすことで、kubectl get podが実行されて結果が出力される。
- **使い方**:
  ```bash
  c0a22103@c0a22103-practice:~/c0a22103-kubectl/practice$ python3 my-kubectl-2.py
    NAMESPACE     NAME                                      READY   STATUS      RESTARTS       AGE
    default       nginx-deployment-96b9d695-5l8hc           1/1     Running     1 (2d8h ago)   47d
    default       nginx-deployment-96b9d695-clb8q           1/1     Running     1 (2d8h ago)   47d
    default       nginx-deployment-96b9d695-wpxxp           1/1     Running     1 (2d8h ago)   47d
    kube-system   coredns-697968c856-dm6vm                  1/1     Running     1 (2d8h ago)   48d
    kube-system   helm-install-traefik-7zqbf                0/1     Completed   1              48d
    kube-system   helm-install-traefik-crd-cls5g            0/1     Completed   0              48d
    kube-system   local-path-provisioner-774c6665dc-dw5rk   1/1     Running     1 (2d8h ago)   48d
    kube-system   metrics-server-6f4c6675d5-dbjzp           1/1     Running     2 (2d8h ago)   48d
    kube-system   svclb-nginx-service-e7005459-rthcf        0/1     Pending     0              47d
    kube-system   svclb-traefik-46a37599-jm4tl              2/2     Running     2 (2d8h ago)   48d
    kube-system   traefik-c98fdf6fb-nk94c                   1/1     Running     1 (2d8h ago)   48d
  ```

### `my-kubectl-3.py`

- **説明**: このファイルをPythonで動かして、「kubectl」の代わりに実行することで、「get pods」を入力するとPodの状況を確認することができる。
- **使い方**:
  ```bash
  c0a22103@c0a22103-practice:~/c0a22103-kubectl/practice$ python3 my-kubectl-3.py get pods
    NAME                              READY   STATUS    RESTARTS       AGE
    nginx-deployment-96b9d695-5l8hc   1/1     Running   1 (2d8h ago)   47d
    nginx-deployment-96b9d695-clb8q   1/1     Running   1 (2d8h ago)   47d
    nginx-deployment-96b9d695-wpxxp   1/1     Running   1 (2d8h ago)   47d
  ```

### `monitor_k8s_yaml.py`

- **説明**:このファイルをPythonで動かして続けることで、YAMLファイルが「kubectl apply」されるまでを監視することができる。さらに、そのYAMLファイルが別のディレクトリに保存される
- **使い方**:
  ```bash
  c0a22103@c0a22103-practice:~/c0a22103-kubectl$ python3 monitor_k8s_yaml.py
    Monitoring /home/c0a22103 for changes...
    Backup created: /home/c0a22103/k8s-backup/20250709_091533_nginx-deployment.yaml
    Backup created: /home/c0a22103/k8s-backup/20250709_091533_nginx-service.yaml
  ```

### `apply_and_log.py`

- **説明**: このファイルをPythonで動かして続けることで、YAMLファイルの内容と出力結果、「kubectl describe」コマンドの結果をログとして保存することができる。
- **使い方**:
  ```bash
  c0a22103@c0a22103-practice:~/c0a22103-kubectl$ python3 apply_and_log.py
    Applied /home/c0a22103/k8s-backup/20250523_034537_nginx-service.yaml, log saved to               /home/c0a22103/k8s-logs/20250709_091930_20250523_034537_nginx-service.yaml.log
    Applied /home/c0a22103/k8s-backup/20250707_005739_nginx-deployment.yaml, log saved to            /home/c0a22103/k8s-logs/20250709_091931_20250707_005739_nginx-deployment.yaml.log
    Applied /home/c0a22103/k8s-backup/20250523_034537_nginx-deployment.yaml, log saved to            /home/c0a22103/k8s-logs/20250709_091931_20250523_034537_nginx-deployment.yaml.log
    Applied /home/c0a22103/k8s-backup/20250709_091533_nginx-service.yaml, log saved to               /home/c0a22103/k8s-logs/20250709_091931_20250709_091533_nginx-service.yaml.log
    Applied /home/c0a22103/k8s-backup/20250709_091533_nginx-deployment.yaml, log saved to            /home/c0a22103/k8s-logs/20250709_091932_20250709_091533_nginx-deployment.yaml.log
    Applied /home/c0a22103/k8s-backup/20250707_005739_nginx-service.yaml, log saved to               /home/c0a22103/k8s-logs/20250709_091932_20250707_005739_nginx-service.yaml.log
  ```
