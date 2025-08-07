from simple_chart_generator import SimpleChartGenerator
import json

def test_simple_charts():
    """测试简化版图表生成器"""
    chart_gen = SimpleChartGenerator()
    
    # 测试柱状图
    bar_data = {
        "chart_type": "bar",
        "title": "每月销售额对比",
        "x_axis": ["一月", "二月", "三月", "四月", "五月"],
        "series": [
            {
                "name": "产品A",
                "data": [120, 200, 150, 80, 70]
            },
            {
                "name": "产品B", 
                "data": [80, 90, 110, 130, 95]
            }
        ]
    }
    
    bar_html = chart_gen.generate_chart(bar_data)
    
    with open('simple_bar_chart.html', 'w', encoding='utf-8') as f:
        f.write(f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>简单柱状图测试</title>
</head>
<body>
    <h1 style="text-align: center;">简单柱状图测试</h1>
    {bar_html}
</body>
</html>
        """)
    
    # 测试表格
    table_data = {
        "chart_type": "table",
        "title": "销售数据汇总",
        "x_axis": ["一月", "二月", "三月", "四月", "五月"],
        "series": [
            {
                "name": "产品A销量",
                "data": [120, 200, 150, 80, 70]
            },
            {
                "name": "产品B销量", 
                "data": [80, 90, 110, 130, 95]
            },
            {
                "name": "总销量",
                "data": [200, 290, 260, 210, 165]
            }
        ]
    }
    
    table_html = chart_gen.generate_chart(table_data)
    
    with open('simple_table.html', 'w', encoding='utf-8') as f:
        f.write(f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>简单表格测试</title>
</head>
<body>
    <h1 style="text-align: center;">简单表格测试</h1>
    {table_html}
</body>
</html>
        """)
    
    print("✅ 简单柱状图测试完成，已保存为 simple_bar_chart.html")
    print("✅ 简单表格测试完成，已保存为 simple_table.html")
    print("\n🎯 图表生成器基础功能测试成功！")

if __name__ == "__main__":
    print("开始测试简化版图表生成器...")
    test_simple_charts()