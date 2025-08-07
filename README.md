# 快速图表生成器 (Quick Chart Generator)

一个基于 MCP (Model Context Protocol) 的可视化图表生成服务，可以根据 JSON 数据快速生成美观的交互式图表。

## 功能特性

- 🎯 **多种图表类型**：支持柱状图、折线图、饼图、散点图
- 🎨 **美观交互**：基于 ECharts 生成可交互的图表
- 🚀 **简单易用**：通过 JSON 配置即可生成图表
- 🔌 **MCP 兼容**：完全符合 MCP 协议标准

## 支持的图表类型

### 1. 柱状图 (Bar Chart)
适用于比较不同类别的数据

### 2. 折线图 (Line Chart)  
适用于展示数据随时间的变化趋势

### 3. 饼图 (Pie Chart)
适用于展示数据的占比关系

### 4. 散点图 (Scatter Chart)
适用于展示两个变量之间的关系

## 安装和使用

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 运行测试
```bash
python test_chart.py
```

### 3. 启动 MCP 服务器
```bash
python mcp_server.py
```

## 数据格式

### 基本格式
```json
{
  "chart_type": "bar|line|pie|scatter",
  "title": "图表标题",
  "x_axis": ["标签1", "标签2", "标签3"],
  "series": [
    {
      "name": "系列名称",
      "data": [数据数组]
    }
  ]
}
```

### 柱状图/折线图示例
```json
{
  "chart_type": "bar",
  "title": "每月销售额",
  "x_axis": ["一月", "二月", "三月"],
  "series": [
    {
      "name": "产品A",
      "data": [120, 200, 150]
    },
    {
      "name": "产品B", 
      "data": [80, 90, 110]
    }
  ]
}
```

### 饼图示例
```json
{
  "chart_type": "pie",
  "title": "市场份额",
  "x_axis": ["Chrome", "Safari", "Firefox"],
  "series": [
    {
      "name": "浏览器份额",
      "data": [65.2, 18.7, 9.1]
    }
  ]
}
```

### 散点图示例
```json
{
  "chart_type": "scatter",
  "title": "身高体重关系",
  "series": [
    {
      "name": "男性",
      "data": [[170, 65], [175, 70], [180, 75]]
    },
    {
      "name": "女性", 
      "data": [[160, 50], [165, 55], [170, 60]]
    }
  ]
}
```

## 技术栈

- **Python 3.7+**
- **Flask**: Web 框架
- **PyECharts**: 图表生成库
- **MCP**: Model Context Protocol

## 项目结构

```
quick-chart-generator/
├── chart_generator.py    # 核心图表生成逻辑
├── mcp_server.py        # MCP 服务器实现
├── test_chart.py        # 测试脚本
├── requirements.txt     # 依赖包列表
└── README.md           # 项目说明
```

## 贡献

欢迎提交 Issue 和 Pull Request 来改进这个项目！

## 许可证

MIT License