import json
import base64
from io import BytesIO

class SimpleChartGenerator:
    def __init__(self):
        self.supported_types = ['bar', 'line', 'pie', 'table']
    
    def generate_chart(self, chart_data):
        """
        根据输入的JSON数据生成图表HTML
        
        Args:
            chart_data (dict): 包含图表配置的字典
            
        Returns:
            str: 生成的HTML字符串
        """
        chart_type = chart_data.get('chart_type', 'bar').lower()
        title = chart_data.get('title', '图表')
        
        if chart_type not in self.supported_types:
            raise ValueError(f"不支持的图表类型: {chart_type}")
        
        if chart_type == 'bar':
            return self._generate_bar_chart(chart_data)
        elif chart_type == 'line':
            return self._generate_line_chart(chart_data)
        elif chart_type == 'pie':
            return self._generate_pie_chart(chart_data)
        elif chart_type == 'table':
            return self._generate_table_chart(chart_data)
    
    def _generate_bar_chart(self, data):
        """生成柱状图 - 使用Chart.js"""
        x_axis = data.get('x_axis', [])
        series = data.get('series', [])
        title = data.get('title', '柱状图')
        
        # 生成颜色
        colors = ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40']
        
        datasets = []
        for i, serie in enumerate(series):
            datasets.append({
                'label': serie.get('name', f'数据{i+1}'),
                'data': serie.get('data', []),
                'backgroundColor': colors[i % len(colors)],
                'borderColor': colors[i % len(colors)],
                'borderWidth': 1
            })
        
        chart_config = {
            'type': 'bar',
            'data': {
                'labels': x_axis,
                'datasets': datasets
            },
            'options': {
                'responsive': True,
                'plugins': {
                    'title': {
                        'display': True,
                        'text': title
                    },
                    'legend': {
                        'display': True,
                        'position': 'top'
                    }
                },
                'scales': {
                    'y': {
                        'beginAtZero': True
                    }
                }
            }
        }
        
        return self._create_chartjs_html(chart_config, title)
    
    def _generate_line_chart(self, data):
        """生成折线图 - 使用Chart.js"""
        x_axis = data.get('x_axis', [])
        series = data.get('series', [])
        title = data.get('title', '折线图')
        
        colors = ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40']
        
        datasets = []
        for i, serie in enumerate(series):
            datasets.append({
                'label': serie.get('name', f'数据{i+1}'),
                'data': serie.get('data', []),
                'borderColor': colors[i % len(colors)],
                'backgroundColor': colors[i % len(colors)] + '20',
                'fill': False,
                'tension': 0.4
            })
        
        chart_config = {
            'type': 'line',
            'data': {
                'labels': x_axis,
                'datasets': datasets
            },
            'options': {
                'responsive': True,
                'plugins': {
                    'title': {
                        'display': True,
                        'text': title
                    },
                    'legend': {
                        'display': True,
                        'position': 'top'
                    }
                },
                'scales': {
                    'y': {
                        'beginAtZero': True
                    }
                }
            }
        }
        
        return self._create_chartjs_html(chart_config, title)
    
    def _generate_pie_chart(self, data):
        """生成饼图 - 使用Chart.js"""
        x_axis = data.get('x_axis', [])
        series = data.get('series', [])
        title = data.get('title', '饼图')
        
        colors = ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40', '#FF6B6B', '#4ECDC4']
        
        if series:
            serie = series[0]
            chart_data = serie.get('data', [])
            
            chart_config = {
                'type': 'pie',
                'data': {
                    'labels': x_axis,
                    'datasets': [{
                        'data': chart_data,
                        'backgroundColor': colors[:len(chart_data)],
                        'borderWidth': 2,
                        'borderColor': '#fff'
                    }]
                },
                'options': {
                    'responsive': True,
                    'plugins': {
                        'title': {
                            'display': True,
                            'text': title
                        },
                        'legend': {
                            'display': True,
                            'position': 'right'
                        }
                    }
                }
            }
        
        return self._create_chartjs_html(chart_config, title)
    
    def _generate_table_chart(self, data):
        """生成表格"""
        x_axis = data.get('x_axis', [])
        series = data.get('series', [])
        title = data.get('title', '数据表格')
        
        html = f"""
        <div style="font-family: Arial, sans-serif; margin: 20px;">
            <h2 style="text-align: center; color: #333;">{title}</h2>
            <table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
                <thead>
                    <tr style="background-color: #f8f9fa;">
                        <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">类别</th>
        """
        
        # 添加系列标题
        for serie in series:
            html += f'<th style="border: 1px solid #ddd; padding: 12px; text-align: center;">{serie.get("name", "数据")}</th>'
        
        html += """
                    </tr>
                </thead>
                <tbody>
        """
        
        # 添加数据行
        for i, category in enumerate(x_axis):
            html += f'<tr style="background-color: {"#f8f9fa" if i % 2 == 0 else "white"};">'
            html += f'<td style="border: 1px solid #ddd; padding: 12px; font-weight: bold;">{category}</td>'
            
            for serie in series:
                data_values = serie.get('data', [])
                value = data_values[i] if i < len(data_values) else '-'
                html += f'<td style="border: 1px solid #ddd; padding: 12px; text-align: center;">{value}</td>'
            
            html += '</tr>'
        
        html += """
                </tbody>
            </table>
        </div>
        """
        
        return html
    
    def _create_chartjs_html(self, chart_config, title):
        """创建Chart.js HTML"""
        config_json = json.dumps(chart_config, ensure_ascii=False)
        
        html = f"""
        <div style="width: 800px; height: 400px; margin: 20px auto;">
            <canvas id="myChart"></canvas>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <script>
            const ctx = document.getElementById('myChart').getContext('2d');
            const myChart = new Chart(ctx, {config_json});
        </script>
        """
        
        return html