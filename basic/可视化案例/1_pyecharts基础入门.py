"""
pyecharts
安装：pip install pyecharts
Mac若报错pip未找到：执行 sudo python3 get-pip.py
https://pyecharts.org/
json格式化网站：ab173.com
"""
# 导包
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

# 创建一个折线图对象
line = Line()

# 给折线图对象添加x轴的数据
line.add_xaxis(["楚国", "齐国", "秦国", "鲁国", "晋国", "赵国"])

# 给折线图对象添加y轴的数据
line.add_yaxis("GDP", [60, 50, 40, 30, 20, 10])

# 设置全局配置项，set_global_opts
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)

# 通过render方法，将代码生成为图像
line.render()
