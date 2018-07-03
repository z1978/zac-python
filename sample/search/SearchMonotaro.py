# encoding:utf-8
import re  # 使用正则 匹配想要的数据
import requests  # 使用requests得到网页源码
from bs4 import BeautifulSoup

def writeData3(strings):
    # r只读，w可写，a追加
    with open("datas.txt", "a", encoding="utf-8") as f:
        f.write("\n".join(strings))

def writeData2():
    strings = ["test", "string", "No.2"]
    # r只读，w可写，a追加
    with open("datas.txt", "a", encoding="utf-8") as f:
        f.write("\n".join(strings))
def writeData(data):
    # r只读，w可写，a追加
    file_object = open('datas.txt', 'a', encoding="utf-8")
    try:
        file_object.write(data +'\n')
    finally:
        file_object.close()

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
    # print(html)
    # 异常处理
    try:
        arr = []
        soup = BeautifulSoup(html, 'html.parser')

        sub_list = soup.findAll("h1", {"class": "main_title"})
        for sub in sub_list:
            print(sub.string)
            mydata = sub.string
            arr.append(sub.string)
        print('找到商品的名称')
        # sub_list = soup.select('a.product_name')
        # for sub in sub_list:
        #     print(sub.string)
        sub_list = soup.findAll("a", {"class": "product_name"})
        for sub in sub_list:
            print(sub.string)
            mydata = mydata + ' ' + sub.string
            arr.append(sub.string)
            # writeData(sub.string)
            # writeData("\n".join(sub.string))
        print('==========')
        print('找到商品的厂家')
        sub_list = soup.select('span.brand')
        for sub in sub_list:
            print(sub.string)
            # writeData(sub.string)
            mydata = mydata + ' ' + sub.string
            arr.append(sub.string)

        print('找到商品的价格')
        sub_list = soup.select('span.price')
        for sub in sub_list:
            print(sub.string)
            mydata = mydata + ' ' + sub.string
            arr.append(sub.string)

        writeData(mydata)
        # writeData(sub.string)
        # writeData2()
        print('==========')
        # writeData3(arr)
        print('==========')
    except:  # 放生异常输出空字符串
        print('放生异常输出空字符串')


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
def serach(key):
    # key = 'FR-A820-0.4K-1' # 你要搜索的东西
    print(key + ' Search ...')
    depth = 1  # 你想要得到几页的东西
    start_url = 'https://www.monotaro.com/s/?c=&q=' + key # 你搜索的网址加上你的搜索东西
    print(start_url)
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

def main():
    file_object = open('list.txt', 'rU')
    try:
        for line in file_object:
            serach(line)
    finally:
        file_object.close()


# 代码调试片段
if __name__ == '__main__':
    main() # 调用主函数
