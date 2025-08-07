from simple_chart_generator import SimpleChartGenerator
import json

def create_demo_charts():
    """创建演示图表"""
    chart_gen = SimpleChartGenerator()
    
    # 演示数据集
    demos = [
        {
            "name": "销售业绩对比",
            "filename": "demo_sales.html",
            "data": {
                "chart_type": "bar",
                "title": "2024年各季度销售业绩对比",
                "x_axis": ["Q1", "Q2", "Q3", "Q4"],
                "series": [
                    {"name": "北京", "data": [320, 450, 380, 520]},
                    {"name": "上海", "data": [280, 380, 420, 480]},
                    {"name": "广州", "data": [200, 280, 350, 400]}
                ]
            }
        },
        {
            "name": "网站流量趋势",
            "filename": "demo_traffic.html", 
            "data": {
                "chart_type": "line",
                "title": "网站月度访问量趋势",
                "x_axis": ["1月", "2月", "3月", "4月", "5月", "6月"],
                "series": [
                    {"name": "PC端", "data": [1200, 1350, 1100, 1400, 1600, 1800]},
                    {"name": "移动端", "data": [800, 950, 1200, 1500, 1800, 2100]}
                ]
            }
        },
        {
            "name": "市场份额分布",
            "filename": "demo_market.html",
            "data": {
                "chart_type": "pie", 
                "title": "2024年智能手机市场份额",
                "x_axis": ["苹果", "三星", "华为", "小米", "OPPO", "其他"],
                "series": [
                    {"name": "市场份额", "data": [28.5, 22.3, 15.8, 12.4, 8.7, 12.3]}
                ]
            }
        },
        {
            "name": "数据汇总表格",
            "filename": "demo_summary.html",
            "data": {
                "chart_type": "table",
                "title": "各部门年度KPI完成情况",
                "x_axis": ["销售部", "市场部", "技术部", "客服部"],
                "series": [
                    {"name": "目标值", "data": [1000, 800, 600, 400]},
                    {"name": "完成值", "data": [1200, 750, 680, 450]},
                    {"name": "完成率(%)", "data": [120, 94, 113, 113]}
                ]
            }
        }
    ]
    
    print("🎨 开始创建演示图表...")
    
    for demo in demos:
        try:
            html_content = chart_gen.generate_chart(demo["data"])
            
            full_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{demo["data"]["title"]}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
            padding: 30px;
            backdrop-filter: blur(10px);
        }}
        h1 {{
            color: #333;
            text-align: center;
            margin-bottom: 30px;
            font-size: 2.2em;
            font-weight: 300;
        }}
        .info {{
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
            border-left: 4px solid #007bff;
        }}
        .footer {{
            text-align: center;
            margin-top: 30px;
            color: #666;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{demo["data"]["title"]}</h1>
        <div class="info">
            <strong>📊 图表类型:</strong> {demo["data"]["chart_type"].upper()} | 
            <strong>🎯 演示项目:</strong> {demo["name"]} | 
            <strong>⚡ 生成工具:</strong> 快速图表生成器 MCP
        </div>
        {html_content}
        <div class="footer">
            <p>🚀 由快速图表生成器 MCP 服务生成 | 基于 Chart.js 技术</p>
        </div>
    </div>
</body>
</html>"""
            
            with open(demo["filename"], 'w', encoding='utf-8') as f:
                f.write(full_html)
            
            print(f"✅ {demo['name']} - 已保存为 {demo['filename']}")
            
        except Exception as e:
            print(f"❌ {demo['name']} 生成失败: {e}")
    
    print(f"\n🎉 演示图表创建完成！共生成 {len(demos)} 个图表文件")
    print("📁 生成的文件:")
    for demo in demos:
        print(f"   - {demo['filename']}")

if __name__ == "__main__":
    create_demo_charts()