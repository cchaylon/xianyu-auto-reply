#!/usr/bin/env python3
import xmind


def generate_xmind_mindmap():
    # 创建新的工作簿
    workbook = xmind.load("my_mindmap.xmind")
    
    # 获取第一个画布
    sheet = workbook.getPrimarySheet()
    sheet.setTitle("项目规划")
    
    # 获取中心主题
    root_topic = sheet.getRootTopic()
    root_topic.setTitle("产品开发路线图")
    
    # 添加子主题
    feature_topic = root_topic.addSubTopic()
    feature_topic.setTitle("核心功能开发")
    
    # 添加更详细的子主题
    frontend_topic = feature_topic.addSubTopic()
    frontend_topic.setTitle("前端开发")
    frontend_topic.addSubTopic().setTitle("用户界面")
    frontend_topic.addSubTopic().setTitle("响应式设计")
    
    backend_topic = feature_topic.addSubTopic()
    backend_topic.setTitle("后端开发")
    backend_topic.addSubTopic().setTitle("API设计")
    backend_topic.addSubTopic().setTitle("数据库优化")
    
    # 添加另一个主分支
    test_topic = root_topic.addSubTopic()
    test_topic.setTitle("测试与部署")
    test_topic.addSubTopic().setTitle("单元测试")
    test_topic.addSubTopic().setTitle("集成测试")
    test_topic.addSubTopic().setTitle("部署上线")
    
    # 保存文件
    xmind.save(workbook, path="my_mindmap.xmind")
    print("XMind文件已成功生成: my_mindmap.xmind")


if __name__ == "__main__":
    generate_xmind_mindmap()

