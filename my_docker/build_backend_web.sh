#!/bin/bash
# 构建/更新后端API服务

cd "$(dirname "$0")"
DC="docker compose"

$DC down backend-web 2>/dev/null || true
$DC build --no-cache backend-web
$DC up -d backend-web
echo "后端API服务已更新完成"
