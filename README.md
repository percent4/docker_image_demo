Docker镜像打包服务说明

### 维护者

- jclian91

本项目持续维护更新。

### 代码结构说明

```
docker_image_demo/ # 项目文件夹
├── docker                  # docker项目文件
│ ├── build.sh              # docker打镜像入口脚本
│ ├── docker-compose.yml    # compose文件
│ ├── flask_demo.build      # Dockerfile
├── python_dev              # Python3.6.8软件，不用动
│ ├── pip-8.0.2.tar.gz
│ └── Python-3.6.8.tar.xz
├── README.md               # README文件
└── src                     # 源代码文件，注意生成requirements.txt
    ├── common              # 通用脚本
    │ ├── common.py
    │ ├── __init__.py
    ├── config              # 项目配置文件，方便外挂
    │ ├── global_conf.py
    │ ├── __init__.py
    │ ├── logging.conf
    ├── data                # 数据集
    ├── log                 # 日志
    │ └── root.log
    ├── models              # 模型文件
    ├── requirements.txt    # 第三方依赖文件
    ├── run.py              # 程序入口文件
    └── utils               # 基础脚本
        └── __init__.py
```

### 使用方法

可以在Linux机器上打镜像。


0. 查看src目录，如果没有log文件夹，则新建log文件夹。
1. 修改docker目录下的`build.sh`, `flask_demo.build`文件；
2. Docker镜像打包：

```shell script
cd docker
chmod u+x build.sh
sh build.sh
```

3. 修改docker-compose.yml文件，用以下命令启动服务：

```shell script
cd docker
docker-compose up -d # 启动服务
docker-compose down  # 停止服务
```

