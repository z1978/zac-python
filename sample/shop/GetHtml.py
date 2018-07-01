import re  
import urllib.request  
import urllib  
from collections import deque  
# 保存文件的后缀  
SUFFIX='.html'  
# 提取文章标题的正则表达式  
REX_TITLE=r'<title>(.*?)</title>'  
# 提取所需链接的正则表达式  
REX_URL=r'/python/(.+?).html'  
# 种子url，从这个url开始爬取  
BASE_URL='https://www.taobao.com/'  
  
  
# 将获取到的文本保存为html文件  
def saveHtml(file_name,file_content):  
#    注意windows文件命名的禁用符，比如 /  
    with open (file_name.replace('/','_')+SUFFIX,"wb") as f:  
#   写文件用bytes而不是str，所以要转码  
        f.write(bytes(file_content, encoding = "utf8"))  
#   获取文章标题  
def getTitle(file_content):  
    linkre = re.search(REX_TITLE,file_content)  
    if(linkre):  
        print('获取文章标题：'+linkre.group(1))  
        return linkre.group(1)  
   
#   爬虫用到的两个数据结构，队列和集合  
queue = deque()  
visited = set()  
#   初始化种子链接   
queue.append(BASE_URL)  
count = 0  
   
while queue:  
  url = queue.popleft()  # 队首元素出队  
  visited |= {url}  # 标记为已访问  
   
  print('已经抓取: ' + str(count) + '   正在抓取 <---  ' + url)  
  count += 1  
  urlop = urllib.request.urlopen(url)  
  # 只处理html链接  
  #if 'html' not in urlop.getheader('Content-Type'):  
  #  continue  
   
  # 避免程序异常中止  
  try:  
    data = urlop.read().decode('utf-8')  
    title=getTitle(data);  
    # 保存文件  
    saveHtml(title,data)  
  except:  
    continue  
   
  # 正则表达式提取页面中所有链接, 并判断是否已经访问过, 然后加入待爬队列  
  linkre = re.compile(REX_URL)  
  for sub_link in linkre.findall(data):  
      sub_url=BASE_URL+sub_link+SUFFIX;  
# 已经访问过，不再处理  
      if sub_url in visited:  
          pass  
      else:  
          # 设置已访问  
          visited |= {sub_url}  
          # 加入队列  
          queue.append(sub_url)  
          print('加入队列 --->  ' + sub_url)  
