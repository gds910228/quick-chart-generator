from chart_generator import ChartGenerator
import json

def test_bar_chart():
    """测试柱状图生成"""
    chart_gen = ChartGenerator()
    
    test_data = {
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
    
    html = chart_gen.generate_chart(test_data)
    
    # 保存为HTML文件以便查看
    with open('test_bar_chart.html', 'w', encoding='utf-8') as f:
        f.write(f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>测试柱状图</title>
</head>
<body>
    {html}
</body>
</html>
        """)
    
    print("柱状图测试完成，已保存为 test_bar_chart.html")

def test_line_chart():
    """测试折线图生成"""
    chart_gen = ChartGenerator()
    
    test_data = {
        "chart_type": "line",
        "title": "网站访问量趋势",
        "x_axis": ["周一", "周二", "周三", "周四", "周五", "周六", "周日"],
        "series": [
            {
                "name": "PC端",
                "data": [820, 932, 901, 934, 1290, 1330, 1320]
            },
            {
                "name": "移动端",
                "data": [620, 732, 701, 734, 1090, 1130, 1120]
            }
        ]
    }
    
    html = chart_gen.generate_chart(test_data)
    
    with open('test_line_chart.html', 'w', encoding='utf-8') as f:
        f.write(f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>测试折线图</title>
</head>
<body>
    {html}
</body>
</html>
        """)
    
    print("折线图测试完成，已保存为 test_line_chart.html")

def test_pie_chart():
    """测试饼图生成"""
    chart_gen = ChartGenerator()
    
    test_data = {
        "chart_type": "pie",
        "title": "市场份额分布",
        "x_axis": ["Chrome", "Safari", "Firefox", "Edge", "其他"],
        "series": [
            {
                "name": "浏览器份额",
                "data": [65.2, 18.7, 9.1, 4.3, 2.7]
            }
        ]
    }
    
    html = chart_gen.generate_chart(test_data)
    
    with open('test_pie_chart.html', 'w', encoding='utf-8') as f:
        f.write(f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>测试饼图</title>
</head>
<body>
    {html}
</body>
</html>
        """)
    
    print("饼图测试完成，已保存为 test_pie_chart.html")

if __name__ == "__main__":
    print("开始测试图表生成器...")
    test_bar_chart()
    test_line_chart() 
    test_pie_chart()
    print("所有测试完成！")