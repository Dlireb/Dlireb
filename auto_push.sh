#!/bin/bash
# 自动 Git 推送脚本 - 每天 22:00 执行
# 用户名：qj | 项目：~/python-project

# 进入项目目录
cd /home/qj/python-project

# 拉取最新（避免冲突）
git pull origin main
git pull gitee main

# 提交所有改动
git add .
git commit -m "WSL 自动每日推送 $(date)"

# 推送到双平台
git push origin main
git push gitee main
