"""
演示全国疫情可视化地图开发
"""
import json
from pyecharts.charts import Map
from pyecharts.options import *

# 读取数据文件
f = open('/Users/lizhenghang/workspace/python/PythonStudy/basic/可视化案例/疫情.txt', 'r', encoding='UTF-8')
data = f.read()
# 关闭文件
f.close()
# 取到各省数据
# 将字符串JSON转换为py字典
data_dict = json.loads(data)
# 从字典中取出省份的数据
province_data_list = data_dict['areaTree'][0]['children']

data_list = []
# 组装每个省份和确诊人数为元组，并各个省的数据都封装入列
for province_data in province_data_list:
    # 省份名称
    province_name = province_data["name"]
    # 确诊人数
    province_confirm = province_data["total"]["confirm"]
    data_list.append((province_name, province_confirm))

print(data_list)
# 创建地图对象
map1 = Map()
# 添加数据
map1.add("各省份确诊人数", data_list, "china")

# 设置全局配置，定制分段的视觉映射
map1.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "label": '1-99人', 'color': '#CCFFFF'},
            {"min": 100, "max": 999, "label": '100-999人', 'color': '#FFFF99'},
            {"min": 1000, "max": 4999, "label": '1000-4999人', 'color': '#FF9966'},
            {"min": 5000, "max": 9999, "label": '5000-9999人', 'color': '#FF6666'},
            {"min": 10000, "max": 99999, "label": '10000-99999人', 'color': '#CC3333'},
            {"min": 100000, "label": '100000+人', 'color': '#990033'}
        ]
    )
)

# 绘图
map1.render("全国疫情地图.html")
