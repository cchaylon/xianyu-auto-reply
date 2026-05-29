# 闲鱼自动回复系统 - Docker部署指南

使用外部MySQL和Redis，本地源码构建方式部署。

## 📋 前置要求

- Docker 20.10+
- Docker Compose 2.0+
- 外部MySQL 8.0+（已部署好）
- 外部Redis 6+（已部署好）

## 🔧 配置

### 1. 修改环境变量

编辑 `.env` 文件，配置你的外部MySQL和Redis：

```env
# MySQL配置
MYSQL_HOST=你的MySQL服务器IP
MYSQL_PORT=3306
MYSQL_USER=用户名
MYSQL_PASSWORD=密码
MYSQL_DATABASE=xianyu_data

# Redis配置
REDIS_HOST=你的Redis服务器IP
REDIS_PORT=6379
REDIS_PASSWORD=密码（可选）
REDIS_DB=0
```

### 2. 创建数据库（首次部署）

在你的MySQL服务器上执行：

```sql
CREATE DATABASE IF NOT EXISTS xianyu_data CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

---

## 🚀 首次部署

依次执行四个脚本部署所有服务：

```bash
cd my_docker

# 1. 部署后端API
./build_backend_web.sh

# 2. 部署WebSocket（消息处理/自动回复）
./build_websocket.sh

# 3. 部署定时任务
./build_scheduler.sh

# 4. 部署前端
./build_frontend.sh
```

### 验证部署

```bash
# 查看服务状态
docker compose ps

# 查看日志
docker compose logs -f
```

### 访问地址

| 服务    | 地址                         |
| ----- | -------------------------- |
| 前端界面  | http://localhost:9000      |
| API文档 | http://localhost:8089/docs |

**默认账号**：admin / admin123

---

## 🔄 单个服务更新代码重新部署

修改代码后，只需执行对应服务的脚本：

### 更新前端

```bash
./build_frontend.sh
```

### 更新后端API

```bash
./build_backend_web.sh
```

### 更新WebSocket（自动回复核心）

```bash
./build_websocket.sh
```

### 更新定时任务

```bash
./build_scheduler.sh
```

---

## 📁 目录结构

```
my_docker/
├── .env                    # 环境变量配置
├── docker-compose.yml      # Docker Compose配置
├── build_frontend.sh       # 前端部署脚本
├── build_backend_web.sh    # 后端API部署脚本
├── build_websocket.sh      # WebSocket部署脚本
└── build_scheduler.sh      # 定时任务部署脚本
```

---

## 📝 常用命令

```bash
# 停止所有服务
docker compose down

# 重启所有服务
docker compose restart

# 查看指定服务日志
docker compose logs -f backend-web
docker compose logs -f websocket

# 进入容器
docker exec -it xianyu-backend-web bash
```

---

## 🔌 服务列表

| 服务          | 端口   | 说明           |
| ----------- | ---- | ------------ |
| frontend    | 9000 | 前端管理界面       |
| backend-web | 8089 | 后端API网关      |
| websocket   | 8090 | 消息处理、自动回复核心  |
| scheduler   | 8091 | 定时任务（发货、评价等） |
