"""
演示地图可视化的基本使用
"""
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

# 准备地图对象
map = Map()

# 准备数据
data = [
    ("北京市", 99),
    ("宁夏回族自治区", 199),
    ("内蒙古自治区", 299),
    ("新疆维吾尔自治区", 399),
    ("西藏自治区", 499),
    ("广西壮族自治区", 599)
]

# 添加数据
map.add("测试地图", data, "china")

# 设置全局选项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": '1-9', 'color': '#CCFFFF'},
            {"min": 10, "max": 99, "label": '10-99', 'color': '#FF6666'},
            {"min": 100, "max": 600, "label": '10-600', 'color': '#990033'}
        ]
    )
)

# 绘图
map.render()
