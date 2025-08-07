import asyncio
import json
from mcp.server import Server
from mcp.types import Tool, TextContent
from chart_generator import ChartGenerator

# 创建MCP服务器实例
server = Server("quick-chart-generator")
chart_gen = ChartGenerator()

@server.list_tools()
async def list_tools():
    """列出可用的工具"""
    return [
        Tool(
            name="generate_chart",
            description="根据提供的数据生成可视化图表",
            inputSchema={
                "type": "object",
                "properties": {
                    "chart_type": {
                        "type": "string",
                        "enum": ["bar", "line", "pie", "scatter"],
                        "description": "图表类型: bar(柱状图), line(折线图), pie(饼图), scatter(散点图)"
                    },
                    "title": {
                        "type": "string",
                        "description": "图表标题"
                    },
                    "x_axis": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "X轴标签数组 (对饼图来说是分类名称)"
                    },
                    "series": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string", "description": "系列名称"},
                                "data": {
                                    "type": "array",
                                    "description": "数据数组，对于散点图是[[x1,y1],[x2,y2]]格式"
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
            
            return [
                TextContent(
                    type="text",
                    text=f"图表生成成功！HTML内容如下：\n\n{html_content}"
                )
            ]
        except Exception as e:
            return [
                TextContent(
                    type="text", 
                    text=f"生成图表时出错: {str(e)}"
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