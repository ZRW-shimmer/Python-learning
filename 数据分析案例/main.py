from file_define import *
from data_define import Record
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType


text_file_reader=TextFileReader(r"D:\BaiduNetdiskDownload\2011年1月销售数据.txt")
json_file_reader=JsonFileReader(r"D:\BaiduNetdiskDownload\2011年2月销售数据JSON.txt")

text_list=text_file_reader.read_data()
json_list=json_file_reader.read_data()
all_list=text_list+json_list

data_dict={}
for record in all_list:
    if record.date in data_dict.keys():
        data_dict[record.date] += record.money
    else:
        data_dict[record.date]=record.money

bar=Bar()
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("销售额",list(data_dict.values()),label_opts=LabelOpts(is_show=False))

bar.render("数据分析.html")
