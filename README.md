# spider
学习爬虫总结的一些东西
### 一、普通爬虫：[spider_not_scrapy ](https://github.com/Wudeyuan/spider/blob/master/Spider_not_scrapy.md)包含两个部分，第一是<kbd>requests</kbd>，第二是<kbd>selenium</kbd>。
><i>requests</i> 包含获取网页、网页内容定位、网页内容下载  
><i>selenium</i> 包含获取网页、网页内容定位
### 二、Scrapy框架爬虫：[spider_scrapy ](https://github.com/Wudeyuan/spider/tree/master/Spider_scrapy/wheather),具体代码在<kbd>wheather</kbd>文件夹下
1. 生成框架，cmd中依次运行以下代码：
```cmd
:: scrapy包用conda来安装
:: 路径根据情况自己修改
cd C:\Users\Wudey\Documents\GitHub\spider\Spider_scrapy
:: 创建项目
scrapy startproject wheather
cd wheather
:: 爬取真气网为例
scrapy genspider Wheather www.aqistudy.cn
:: 查看网址，是否能进入，若不能进入，修改settings.py文件，如加入agent、修改robot等
scrapy shell https://www.aqistudy.cn/historydata/
:: 查看scrapy显示的界面是否与浏览器一致，并以此页面作为定位依据
view(response)
```
2. 修改各个文件（具体修改见文件）
> 修改*items*，定义好需要爬取的变量  
> 编辑*Pipelines*，增加输出格式，也可以不改  
> 编辑*settings*文件，案例用了selenium，需要下载好chromedriver.exe  
> 编辑爬虫文件*Wheather* 
3. 运行代码
```cmd
cd wheather
:: 输出为csv格式
scrapy crawl Wheather -o books.csv
```
