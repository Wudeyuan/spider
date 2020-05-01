###### 流程：requests— xpath、css定位（文本）—定位并下载（非文本）— 动态加载（selenium）—post网站—selenium爬取post
##### 准备工作
- 安装python，推荐直接安装anoconda或者miniconda，不用折腾
- 编辑器推荐VS code，轻便且功能强大，不推荐sublime（配置较麻烦），较不推荐pycharm（代码提示能力很强，但是有种看用ps看图片的感觉，不适合日常使用）
- 下载chromedriver，并置于系统环境
##### 1.最常用的requests
###### 优先考虑requests爬取
```python
import requests
url='http://car.bitauto.com/aodia3-3999/peizhi/'
head=dict() # 设置agent
head['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'  # 添加代理，有些网站回识别requests，加浏览器代理，百利无害
rq=requests.get(url=url,headers=head)  # 爬取
rq.encoding="utf-8"  # 或者用rq.content.decode('utf-8'),需要看网页是用什么编码写的，乱码了考虑utf-8换成gbk
print(rq.text)
# VScode输出中文乱码推荐看(https://www.jianshu.com/p/e634bff989f2)
f = open("spider.txt","w",encoding="utf-8")
f.write(rq.text) # 爬取的东西写到文本里
f.close() # 记得关闭
```
##### 2.网页内容定位(文本)
###### xpath定位或者css定位，不推荐beautifulsoup(较麻烦且较前者无显著优势)
```python
# 注意该代码块紧跟上一个代码块
import lxml.html as path
tree = path.fromstring(rq.text) # 编译
# htl = path.tostring(tree) # 编译回string
tdcss=tree.cssselect('body > header > div.middle-nav-box > div > div.brand-info > h1 > a:nth-child(2)')[0].text_content()  # css定位
tdxpath=tree.xpath('/html/body/header/div[2]/div/div[1]/h1/a[2]')[0].text_content() # xpath定位
# 文本处理
print(tdxpath[-2:]) # 直接取倒数第二及之后
print(tdxpath.replace("奥迪","")) # replace函数
print(tdxpath.split("迪")[1]) # split切片
import re
print("".join(re.findall('[A-Z0-9]',tdxpath))) # findall函数非常重要，可以自己学习
```
##### 2.网页内容定位并下载(非文本)
```python
# 注意该代码块紧跟上一个代码块
# 下载图片
td=tree.xpath('/html/body/header/div[2]/div/div[1]/h1/a[1]/img/@src')[0] # 用@取属性
url1='http:'+td # 构造完整url
img = requests.get(url=url1).content # 图片内容
with open('a.jpg','wb') as f:
    f.write(img) # 下载图片，用with open()就不需要f.close()
```
##### 3.不能直接定位（动态加载）
```python
# 注意该代码块紧跟上一个代码块
td=tree.xpath('//*[@id="tr2,2,2_0,1,2"]/td[1]')
print(td) # 无法定位详细数据，动态加载，解析或者考虑Selenium
```
##### 4.selenium爬取（动态加载）
###### 一般通过js或xhr实现动态加载，有兴趣的可以解析后用requests，没兴趣或者很难解析的直接用selenium
```python
from selenium import webdriver

f = open("spider.txt","w",encoding="utf-8")
opt=webdriver.ChromeOptions()
opt.add_argument('-headless') # 无界面
prefs = {"profile.managed_default_content_settings.images":2}  # 无图加载，更快
opt.add_experimental_option("prefs",prefs)
driver=webdriver.Chrome(chrome_options=opt) # 作者将chromedriver.exe放在系统环境下了
url='http://car.bitauto.com/aodia3-3999/peizhi/'
driver.get(url)
t=len(driver.find_elements_by_xpath('//*[@id="tr2,2,2_0,1,2"]/td')) # 计算有多少个td标签
for num in range(1,(t+1)):
    A0=driver.find_element_by_xpath('//*[@id="draggcarbox_%s"]/dl/dd[1]/a' % str(num-1)).text
    A1=driver.find_element_by_xpath('//*[@id="tr2,2,2_0,1,2"]/td[%s]' % str(num)).text # %s代表一个字符串，str表示转换成字符串，text表示取文字部分
    # print(driver.find_element_by_xpath('//*[@id="CarCompareContent"]/table/tbody/tr[20]/td[%s]' % str(num)).text)
    # print(driver.find_element_by_xpath('//*[@id="tr2,2,2_0,1,2"]/following-sibling::tr[1]/td[%s]'% str(num)).text) # 以id为准，变一个，翻页爬虫时更加稳定
    A2=driver.find_element_by_xpath("//*[text()='轴距[mm]']/following-sibling::td[%s]" % str(num)).text  # 以文字为准，变一个，翻页爬虫时更加稳定，following-sibling表示下兄弟节点
    print(A0+'\t'+A1+'\t'+A2)  # 、t表示制表符tab,\n表示分行
    f.write(A0+'\t'+A1+'\t'+A2+'\n') # 只写入第一页
    f.close() # 记得关
driver.quit()
```
##### 5.post网页爬取
###### post网站，网页内容变化但是网址不变
```python
import requests

f = open("spider.txt", "w", encoding="utf-8")
url = 'http://www.chinanpo.gov.cn/search/orgcx.html'
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    'Referer':'http://www.chinanpo.gov.cn/search/orgcx.html'
} #request headers部分，Cookie有时候是必要的，这里没加上
## 注意requests.get也可以用上述字典，比只加agent效果可能会更好！！！！！
formdata = dict(tabIndex=2,
               t=2,
               orgName=r'%E5%8C%BB%E9%99%A2', # 医院的网页解码
               regDate='2014-12-01',
               regDateEnd='2018-07-28') # formdata部分
a = requests.post(url,data=formdata,headers=header)
f.write(a.text)
a.close()  # 关闭访问,养成好习惯​
```
##### 6.selenium爬取post网站
###### 有些post网页中会有动态加载，不想解析的话可以用selenium一并解决
```python
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common import keys

f = open("spider.txt", "w", encoding="utf-8")
opt=webdriver.ChromeOptions()
opt.add_argument('-headless')  # 无界面
driver = webdriver.Chrome(chrome_options=opt)
url='http://kns.cnki.net/kns/brief/default_result.aspx'
driver.implicitly_wait(4)  # 隐性等待，最多等4秒来加载
driver.get(url)
s = Select(driver.find_element_by_css_selector('#txt_1_sel'))
s.select_by_visible_text('篇名')  # 选择篇名
# driver.maximize_window() # 最大化窗口
driver.find_element_by_xpath('//*[@id="txt_1_value1"]').send_keys('urbanization economic')  # 输入关键词
driver.find_element_by_xpath('//*[@id="txt_1_value1"]').send_keys(keys.Keys.RETURN)  # 回车
# 后续可以根据需要继续driver爬取
print(driver.find_element_by_xpath('//*[@id="SCDB"]/a').text) # 用.text来取文本部分
print(driver.find_element_by_xpath('//*[@id="HeaderDiv"]/div[1]/div[2]/a/img[1]').get_attribute("src")) # 用.get_attribute来获取属性
```
###### 附（for myself）：pdf处理比较麻烦，pdf可以用pdfminer包来转文本，但是建议用adobe acrobat来直接转，后者转换能力更强。
