#!/usr/bin/env python3
import xmind


def generate_project_feature_mindmap():
    workbook = xmind.load("闲鱼自动回复系统功能清单.xmind")
    sheet = workbook.getPrimarySheet()
    sheet.setTitle("闲鱼自动回复系统功能清单")
    
    root = sheet.getRootTopic()
    root.setTitle("闲鱼自动回复系统")
    
    # 主系统功能
    main_system = root.addSubTopic()
    main_system.setTitle("主系统功能")
    
    # 1. 多账号管理
    account_mgmt = main_system.addSubTopic()
    account_mgmt.setTitle("多账号管理")
    account_mgmt.addSubTopic().setTitle("账号登录与状态切换")
    account_mgmt.addSubTopic().setTitle("Cookie维护")
    account_mgmt.addSubTopic().setTitle("登录续期")
    account_mgmt.addSubTopic().setTitle("多账号状态管理")
    
    # 2. 自动回复
    auto_reply = main_system.addSubTopic()
    auto_reply.setTitle("自动回复")
    auto_reply.addSubTopic().setTitle("文本关键词回复")
    auto_reply.addSubTopic().setTitle("图片关键词回复")
    auto_reply.addSubTopic().setTitle("默认回复")
    auto_reply.addSubTopic().setTitle("商品专属回复")
    
    # 3. AI回复
    ai_reply = main_system.addSubTopic()
    ai_reply.setTitle("AI智能回复")
    ai_reply.addSubTopic().setTitle("大模型上下文对话")
    ai_reply.addSubTopic().setTitle("智能回复生成")
    ai_reply.addSubTopic().setTitle("AI回复配置")
    
    # 4. 自动发货
    auto_delivery = main_system.addSubTopic()
    auto_delivery.setTitle("自动发货")
    auto_delivery.addSubTopic().setTitle("卡券自动发货")
    auto_delivery.addSubTopic().setTitle("虚拟商品发货")
    auto_delivery.addSubTopic().setTitle("自动补发")
    auto_delivery.addSubTopic().setTitle("发货结果记录")
    auto_delivery.addSubTopic().setTitle("卡券管理")
    
    # 5. 在线聊天
    online_chat = main_system.addSubTopic()
    online_chat.setTitle("在线聊天")
    online_chat.addSubTopic().setTitle("会话列表")
    online_chat.addSubTopic().setTitle("消息收发")
    online_chat.addSubTopic().setTitle("聊天联动")
    online_chat.addSubTopic().setTitle("实时消息推送")
    
    # 6. 商品发布
    product_publish = main_system.addSubTopic()
    product_publish.setTitle("商品发布")
    product_publish.addSubTopic().setTitle("素材库管理")
    product_publish.addSubTopic().setTitle("地址库管理")
    product_publish.addSubTopic().setTitle("单品发布")
    product_publish.addSubTopic().setTitle("批量发布")
    product_publish.addSubTopic().setTitle("发布日志")
    
    # 7. 订单与评价
    orders_ratings = main_system.addSubTopic()
    orders_ratings.setTitle("订单与评价")
    orders_ratings.addSubTopic().setTitle("订单拉取")
    orders_ratings.addSubTopic().setTitle("自动评价")
    orders_ratings.addSubTopic().setTitle("求小红花")
    orders_ratings.addSubTopic().setTitle("状态跟踪")
    
    # 8. 商品采集与分销
    distribution = main_system.addSubTopic()
    distribution.setTitle("商品采集与分销")
    distribution.addSubTopic().setTitle("Goofish采集")
    distribution.addSubTopic().setTitle("货源管理")
    distribution.addSubTopic().setTitle("对接记录")
    distribution.addSubTopic().setTitle("结算链路")
    distribution.addSubTopic().setTitle("分销商管理")
    distribution.addSubTopic().setTitle("代理订单")
    
    # 9. 通知与风控
    notification_risk = main_system.addSubTopic()
    notification_risk.setTitle("通知与风控")
    notification_risk.addSubTopic().setTitle("消息通知")
    notification_risk.addSubTopic().setTitle("通知渠道配置")
    notification_risk.addSubTopic().setTitle("风控日志")
    notification_risk.addSubTopic().setTitle("系统反馈")
    notification_risk.addSubTopic().setTitle("公告管理")
    
    # 10. 系统管理
    system_mgmt = main_system.addSubTopic()
    system_mgmt.setTitle("系统管理")
    system_mgmt.addSubTopic().setTitle("用户管理")
    system_mgmt.addSubTopic().setTitle("角色权限")
    system_mgmt.addSubTopic().setTitle("系统设置")
    system_mgmt.addSubTopic().setTitle("菜单配置")
    system_mgmt.addSubTopic().setTitle("主题配置")
    system_mgmt.addSubTopic().setTitle("广告管理")
    system_mgmt.addSubTopic().setTitle("资金流水")
    
    # 11. 日志管理
    log_mgmt = main_system.addSubTopic()
    log_mgmt.setTitle("日志管理")
    log_mgmt.addSubTopic().setTitle("系统日志")
    log_mgmt.addSubTopic().setTitle("消息日志")
    log_mgmt.addSubTopic().setTitle("账号登录日志")
    log_mgmt.addSubTopic().setTitle("定时任务日志")
    log_mgmt.addSubTopic().setTitle("Cookie刷新日志")
    log_mgmt.addSubTopic().setTitle("API续期日志")
    log_mgmt.addSubTopic().setTitle("补发货日志")
    log_mgmt.addSubTopic().setTitle("补评价日志")
    log_mgmt.addSubTopic().setTitle("擦亮日志")
    log_mgmt.addSubTopic().setTitle("小红花日志")
    log_mgmt.addSubTopic().setTitle("消息通知关闭日志")
    
    # 12. 定时任务
    scheduled_tasks = main_system.addSubTopic()
    scheduled_tasks.setTitle("定时任务")
    scheduled_tasks.addSubTopic().setTitle("自动发货任务")
    scheduled_tasks.addSubTopic().setTitle("自动评价任务")
    scheduled_tasks.addSubTopic().setTitle("订单拉取任务")
    scheduled_tasks.addSubTopic().setTitle("Cookie刷新任务")
    scheduled_tasks.addSubTopic().setTitle("登录续期任务")
    scheduled_tasks.addSubTopic().setTitle("商品擦亮任务")
    scheduled_tasks.addSubTopic().setTitle("关闭通知任务")
    
    # 返佣子系统
    promotion_system = root.addSubTopic()
    promotion_system.setTitle("返佣子系统")
    
    # 1. 返佣账号
    promo_account = promotion_system.addSubTopic()
    promo_account.setTitle("返佣账号管理")
    promo_account.addSubTopic().setTitle("账号登录")
    promo_account.addSubTopic().setTitle("状态管理")
    promo_account.addSubTopic().setTitle("Cookie维护")
    
    # 2. 选品规则
    product_rules = promotion_system.addSubTopic()
    product_rules.setTitle("选品规则")
    product_rules.addSubTopic().setTitle("规则配置")
    product_rules.addSubTopic().setTitle("定时抓取")
    product_rules.addSubTopic().setTitle("自动写入素材库")
    
    # 3. 素材库
    material_lib = promotion_system.addSubTopic()
    material_lib.setTitle("素材库")
    material_lib.addSubTopic().setTitle("标题管理")
    material_lib.addSubTopic().setTitle("图片管理")
    material_lib.addSubTopic().setTitle("详情管理")
    material_lib.addSubTopic().setTitle("淘口令")
    material_lib.addSubTopic().setTitle("短链管理")
    material_lib.addSubTopic().setTitle("库存管理")
    material_lib.addSubTopic().setTitle("发布状态")
    
    # 4. 发布规则
    publish_rules = promotion_system.addSubTopic()
    publish_rules.setTitle("发布规则")
    publish_rules.addSubTopic().setTitle("定时发布")
    publish_rules.addSubTopic().setTitle("发布配置")
    publish_rules.addSubTopic().setTitle("发布日志")
    
    # 5. 删除规则
    delete_rules = promotion_system.addSubTopic()
    delete_rules.setTitle("删除规则")
    delete_rules.addSubTopic().setTitle("定时删除")
    delete_rules.addSubTopic().setTitle("删除配置")
    delete_rules.addSubTopic().setTitle("删除日志")
    
    # 6. 补偿任务
    repair_tasks = promotion_system.addSubTopic()
    repair_tasks.setTitle("补偿任务")
    repair_tasks.addSubTopic().setTitle("已发布商品ID回写")
    repair_tasks.addSubTopic().setTitle("短链修复")
    repair_tasks.addSubTopic().setTitle("卡券补偿")
    
    # 技术架构
    tech_arch = root.addSubTopic()
    tech_arch.setTitle("技术架构")
    
    # 后端技术
    backend_tech = tech_arch.addSubTopic()
    backend_tech.setTitle("后端技术栈")
    backend_tech.addSubTopic().setTitle("FastAPI")
    backend_tech.addSubTopic().setTitle("SQLAlchemy 2.0")
    backend_tech.addSubTopic().setTitle("MySQL 8.0")
    backend_tech.addSubTopic().setTitle("Redis 7")
    backend_tech.addSubTopic().setTitle("Playwright")
    backend_tech.addSubTopic().setTitle("APScheduler")
    backend_tech.addSubTopic().setTitle("Loguru")
    
    # 前端技术
    frontend_tech = tech_arch.addSubTopic()
    frontend_tech.setTitle("前端技术栈")
    frontend_tech.addSubTopic().setTitle("React 18")
    frontend_tech.addSubTopic().setTitle("TypeScript")
    frontend_tech.addSubTopic().setTitle("Vite")
    frontend_tech.addSubTopic().setTitle("TailwindCSS")
    frontend_tech.addSubTopic().setTitle("Zustand")
    frontend_tech.addSubTopic().setTitle("Lucide React")
    
    # 服务架构
    service_arch = tech_arch.addSubTopic()
    service_arch.setTitle("服务架构")
    service_arch.addSubTopic().setTitle("Frontend (端口9000)")
    service_arch.addSubTopic().setTitle("Backend-Web (端口8089)")
    service_arch.addSubTopic().setTitle("WebSocket (端口8090)")
    service_arch.addSubTopic().setTitle("Scheduler (端口8091)")
    service_arch.addSubTopic().setTitle("Promotion Backend (端口8092)")
    service_arch.addSubTopic().setTitle("Promotion Frontend (端口9001)")
    
    # 部署方式
    deployment = tech_arch.addSubTopic()
    deployment.setTitle("部署方式")
    deployment.addSubTopic().setTitle("Docker / Docker Compose")
    deployment.addSubTopic().setTitle("Nginx反向代理")
    deployment.addSubTopic().setTitle("Windows桌面启动器")
    
    # 部署方式
    deployment_modes = root.addSubTopic()
    deployment_modes.setTitle("部署方式")
    
    server_deploy = deployment_modes.addSubTopic()
    server_deploy.setTitle("服务器一键部署")
    server_deploy.addSubTopic().setTitle("curl部署脚本")
    server_deploy.addSubTopic().setTitle("自动配置生成")
    server_deploy.addSubTopic().setTitle("镜像拉取启动")
    
    git_deploy = deployment_modes.addSubTopic()
    git_deploy.setTitle("Git克隆部署")
    git_deploy.addSubTopic().setTitle("源码克隆")
    git_deploy.addSubTopic().setTitle("deploy.sh部署")
    git_deploy.addSubTopic().setTitle("update.sh更新")
    
    docker_build = deployment_modes.addSubTopic()
    docker_build.setTitle("本地Docker构建")
    docker_build.addSubTopic().setTitle("build.sh全量构建")
    docker_build.addSubTopic().setTitle("单独服务构建")
    docker_build.addSubTopic().setTitle("开发模式")
    
    exe_deploy = deployment_modes.addSubTopic()
    exe_deploy.setTitle("EXE打包部署")
    exe_deploy.addSubTopic().setTitle("Nuitka打包")
    exe_deploy.addSubTopic().setTitle("离线依赖打包")
    
    xmind.save(workbook, path="闲鱼自动回复系统功能清单.xmind")
    print("✅ 功能清单已成功生成: 闲鱼自动回复系统功能清单.xmind")


if __name__ == "__main__":
    generate_project_feature_mindmap()
