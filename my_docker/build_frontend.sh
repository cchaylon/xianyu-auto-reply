#!/bin/bash
# 构建/更新前端服务

cd "$(dirname "$0")"
DC="docker compose"

$DC down frontend 2>/dev/null || true
$DC build --no-cache frontend
$DC up -d frontend
echo "前端服务已更新完成"
