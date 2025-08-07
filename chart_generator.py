from pyecharts import options as opts
from pyecharts.charts import Bar, Line, Pie, Scatter
from pyecharts.globals import ThemeType
import json

class ChartGenerator:
    def __init__(self):
        self.supported_types = ['bar', 'line', 'pie', 'scatter']
    
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
        elif chart_type == 'scatter':
            return self._generate_scatter_chart(chart_data)
    
    def _generate_bar_chart(self, data):
        """生成柱状图"""
        chart = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        
        x_axis = data.get('x_axis', [])
        series = data.get('series', [])
        title = data.get('title', '柱状图')
        
        chart.add_xaxis(x_axis)
        
        for serie in series:
            chart.add_yaxis(
                serie.get('name', '数据'),
                serie.get('data', []),
                label_opts=opts.LabelOpts(is_show=False)
            )
        
        chart.set_global_opts(
            title_opts=opts.TitleOpts(title=title),
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
            yaxis_opts=opts.AxisOpts(),
            toolbox_opts=opts.ToolboxOpts(),
            legend_opts=opts.LegendOpts(pos_top="5%")
        )
        
        return chart.render_embed()
    
    def _generate_line_chart(self, data):
        """生成折线图"""
        chart = Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        
        x_axis = data.get('x_axis', [])
        series = data.get('series', [])
        title = data.get('title', '折线图')
        
        chart.add_xaxis(x_axis)
        
        for serie in series:
            chart.add_yaxis(
                serie.get('name', '数据'),
                serie.get('data', []),
                is_smooth=True,
                label_opts=opts.LabelOpts(is_show=False)
            )
        
        chart.set_global_opts(
            title_opts=opts.TitleOpts(title=title),
            xaxis_opts=opts.AxisOpts(),
            yaxis_opts=opts.AxisOpts(),
            toolbox_opts=opts.ToolboxOpts(),
            legend_opts=opts.LegendOpts(pos_top="5%")
        )
        
        return chart.render_embed()
    
    def _generate_pie_chart(self, data):
        """生成饼图"""
        chart = Pie(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        
        title = data.get('title', '饼图')
        series = data.get('series', [])
        
        # 饼图数据格式转换
        pie_data = []
        if series:
            serie = series[0]  # 饼图通常只有一个系列
            names = data.get('x_axis', [])
            values = serie.get('data', [])
            
            for i, name in enumerate(names):
                if i < len(values):
                    pie_data.append([name, values[i]])
        
        chart.add(
            series_name=series[0].get('name', '数据') if series else '数据',
            data_pair=pie_data,
            radius=["40%", "75%"]
        )
        
        chart.set_global_opts(
            title_opts=opts.TitleOpts(title=title),
            legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%")
        )
        
        chart.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c} ({d}%)"))
        
        return chart.render_embed()
    
    def _generate_scatter_chart(self, data):
        """生成散点图"""
        chart = Scatter(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        
        title = data.get('title', '散点图')
        series = data.get('series', [])
        
        for serie in series:
            # 散点图数据格式: [[x1, y1], [x2, y2], ...]
            scatter_data = serie.get('data', [])
            chart.add_yaxis(
                serie.get('name', '数据'),
                scatter_data,
                label_opts=opts.LabelOpts(is_show=False)
            )
        
        chart.set_global_opts(
            title_opts=opts.TitleOpts(title=title),
            xaxis_opts=opts.AxisOpts(type_="value"),
            yaxis_opts=opts.AxisOpts(type_="value"),
            toolbox_opts=opts.ToolboxOpts(),
            legend_opts=opts.LegendOpts(pos_top="5%")
        )
        
        return chart.render_embed()