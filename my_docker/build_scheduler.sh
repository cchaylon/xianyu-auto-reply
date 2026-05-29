#!/bin/bash
# 构建/更新Scheduler服务

cd "$(dirname "$0")"
DC="docker compose"

$DC down scheduler 2>/dev/null || true
$DC build --no-cache scheduler
$DC up -d scheduler
echo "Scheduler服务已更新完成"
