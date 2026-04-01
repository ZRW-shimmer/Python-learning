from pyecharts.charts import Bar,Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType


bar1=Bar()
bar1.add_xaxis(["美国","英国","中国"])
bar1.add_yaxis("GDP",[20,40,50],label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2=Bar()
bar2.add_xaxis(["美国","英国","中国"])
bar2.add_yaxis("GDP",[30,50,60],label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3=Bar()
bar3.add_xaxis(["美国","英国","中国"])
bar3.add_yaxis("GDP",[50,60,70],label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

timeline=Timeline(
    {"Theme":ThemeType.WHITE,}
)

timeline.add(bar1,"2020年GDP")
timeline.add(bar2,"2021年GDP")
timeline.add(bar3,"2022年GDP")

timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True,


)


timeline.render("基础时间柱状图.html")




