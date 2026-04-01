from pyecharts.charts import Bar,Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType



f=open(r"C:\Users\86156\Desktop\1960-2019全球GDP数据.csv","r",encoding="ANSI")
data_line=f.readlines()
f.close()
#删除第一条数据
data_line.pop(0)
#将数据转化为字典
data_dict={}

for line in data_line:
    year=int(line.split(",")[0])
    country=line.split(",")[1]
    GDP=float(line.split(",")[2])
    try:
        data_dict[year].append([country,GDP])
    except KeyError:
        data_dict[year]=[]
        data_dict[year].append([country,GDP])
#创建时间线
timeline = Timeline({"theme":ThemeType.LIGHT})
sorted_year_list=sorted(data_dict.keys())

for year in sorted_year_list:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    year_data=data_dict[year][0:8]
    x_data=[]
    y_data=[]
    for country_Gdp in year_data:
        x_data.append(country_Gdp[0])
        y_data.append(country_Gdp[1]/100000000)

        #创建柱状表
    bar=Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("Gdp(亿)",y_data,label_opts=LabelOpts(position="right"))
    bar.reversal_axis()
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年世界前八Gdp排名")
    )
    timeline.add(bar,str(year))

timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True,
)

timeline.render("1960-2016年全球Gdp排名前八国家.html")






