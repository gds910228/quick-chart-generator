import asyncio
import json
from mcp.server import Server
from mcp.types import Tool, TextContent
from simple_chart_generator import SimpleChartGenerator

# 创建MCP服务器实例
server = Server("quick-chart-generator")
chart_gen = SimpleChartGenerator()

@server.list_tools()
async def list_tools():
    """列出可用的工具"""
    return [
        Tool(
            name="generate_chart",
            description="根据提供的数据生成可视化图表，支持柱状图、折线图、饼图和表格",
            inputSchema={
                "type": "object",
                "properties": {
                    "chart_type": {
                        "type": "string",
                        "enum": ["bar", "line", "pie", "table"],
                        "description": "图表类型: bar(柱状图), line(折线图), pie(饼图), table(表格)"
                    },
                    "title": {
                        "type": "string",
                        "description": "图表标题"
                    },
                    "x_axis": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "X轴标签数组 (对饼图来说是分类名称，对表格来说是行标题)"
                    },
                    "series": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string", "description": "系列名称"},
                                "data": {
                                    "type": "array",
                                    "items": {"type": "number"},
                                    "description": "数据数组"
                                }
                            },
                            "required": ["name", "data"]
                        },
                        "description": "数据系列数组"
                    }
                },
                "required": ["chart_type", "title", "series"]
            }
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict):
    """处理工具调用"""
    if name == "generate_chart":
        try:
            # 生成图表HTML
            html_content = chart_gen.generate_chart(arguments)
            
            # 创建完整的HTML页面
            full_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{arguments.get('title', '图表')}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            padding: 20px;
        }}
        h1 {{
            color: #333;
            text-align: center;
            margin-bottom: 30px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{arguments.get('title', '图表')}</h1>
        {html_content}
    </div>
</body>
</html>"""
            
            return [
                TextContent(
                    type="text",
                    text=f"✅ 图表生成成功！\n\n📊 图表类型: {arguments.get('chart_type', '未知')}\n📝 标题: {arguments.get('title', '无标题')}\n\n完整的HTML内容如下：\n\n{full_html}"
                )
            ]
        except Exception as e:
            return [
                TextContent(
                    type="text", 
                    text=f"❌ 生成图表时出错: {str(e)}\n\n请检查输入数据格式是否正确。"
                )
            ]
    else:
        raise ValueError(f"未知工具: {name}")

async def main():
    """启动MCP服务器"""
    from mcp.server.stdio import stdio_server
    
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())