#!/usr/bin/env bash
TIMENOW=`date +%y.%m.%d.%H%M`

# 进行docker镜像打包
# -f 指定文件 ， -t 指定生成镜像名称 , 冒号后为版本号 ， 各位大佬命名请不要冲突例子 ： docker_package:17.08.01.1311
# 注意修改tag: flask_demo
cd ..
docker build -f ./docker/flask_demo.build -t flask_demo:${TIMENOW} .