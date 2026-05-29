#!/bin/bash
# 构建/更新WebSocket服务

cd "$(dirname "$0")"
DC="docker compose"

$DC down websocket 2>/dev/null || true
$DC build --no-cache websocket
$DC up -d websocket
echo "WebSocket服务已更新完成"
