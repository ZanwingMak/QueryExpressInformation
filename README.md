# QueryExpressInformation
查询快递物流信息

先选择快递公司然后输入运单号即可查询到快递的物流信息，使用的是快递100的API。前面说到用户友好度，在运单号输入框这里应该先把用户输入的运单号去掉前后的空格，因为有时候用户复制的时候经常会有个空格，这就会导致查询失败，甚至程序会因此崩溃，还有“请先选择快递公司”、“运单号应该为数字”这样子的用户提示。

API: http://wap.kuaidi100.com/wap_result.jsp?rand=20120517&id=快递公司&fromWeb=null&&postid=运单号

主要使用库：requests、BeautifulSoup、PyQt4

【EXE打包】链接: http://pan.baidu.com/s/1sjwzVzB 密码: mn84

![image](http://i13.tietuku.com/ec763ddb2cb029b8.png)
