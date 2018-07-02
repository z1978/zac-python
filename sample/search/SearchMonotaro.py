# encoding:utf-8
import re  # 使用正则 匹配想要的数据
import requests  # 使用requests得到网页源码
from bs4 import BeautifulSoup

# 得到主函数传入的链接
def getHtmlText(url):
    try:  # 异常处理
        #  得到你传入的URL链接  设置超时时间3秒
        r = requests.get(url, timeout=3)
        # 判断它的http状态码
        r.raise_for_status()
        # 设置它的编码 encoding是设置它的头部编码 apparent_encoding是从返回网页中分析它的编码格式
        r.encoding = r.apparent_encoding
        # 返回源代码
        return r.text
    except: # 发生异常返回空
        return ''

# 解析你的网页信息
def parsePage(ilt, html):
    # 异常处理
    try:
        soup = BeautifulSoup(html, 'html.parser')
        sub_list = soup.select('span.price')
        for sub in sub_list:
            print('找到商品的价格')
            print(sub.string)
    except:  # 放生异常输出空字符串
        print('')


# 得到主函数传入的列表
def printGoodsList(ilt):
    # 每个列之间用tplt的放是隔开
    tplt = '{:4}\t{:8}\t{:16}\t{:32}'
    # 这个是整个的标题
    print(tplt.format('序号', '价格', '商品名称','地址', '图片地址'))
    count = 0 # 统计有多少的序号
    for g in ilt:
        count = count + 1  # 循环一遍加一
        print(tplt.format(count, g[0], g[1], g[2]), g[3])  # 输出你得到的数据

# 定义主函数 main
def main():
    goods = 'FR-A720-75K' # 你要搜索的东西
    print(goods + ' Search ...')
    depth = 1  # 你想要得到几页的东西
    start_url = 'https://www.monotaro.com/s/?c=&q=' + goods # 你搜索的网址加上你的搜索东西
    infoList = [] # 自定义的空列表用来存放你的到的数据
    for i in range(depth): # 循环你的页数
        try: # 异常处理
            url = start_url + '&s' + str(44 * i) # 得到你的网址
            html = getHtmlText(url) # 得到url传入到你要得到url的函数中
            parsePage(infoList, html) # 得到你的html源码 放入解析的网页中
        except: # 发生异常跳过
            continue
    # 把列表中的数据放入解析的函数中
    printGoodsList(infoList)

# 代码调试片段
if __name__ == '__main__':
    main() # 调用主函数
