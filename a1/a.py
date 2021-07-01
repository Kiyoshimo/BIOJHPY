import os
import re
import pyecharts

cmd = 'ping www.google.com -n 1'
res = os.popen(cmd)
output_str = res.read()   # 获得输出字符串
#print(output_str)

str1=output_str.split("\n")
n=str1[2]
#print(n)
n=n.split(" ")
time_str=n[4]
time_str="时间=702ms" #时间=7ms test
time_list=(re.findall(r"\d+", time_str))
time_int=int(time_list[0])
print(time_int)  # 输出数字

from pyecharts.charts import Bar
from pyecharts import options as opts
 
# V1 版本开始支持链式调用
bar = (
    Bar()
    .add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
    .add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
    .set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))
)
#bar.render()
bar.render_notebook()