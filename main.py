#coding:utf-8
__author__ = 'm9Kun'

from Tkinter import *
import tkMessageBox #python3的话直接集成在tkinter
from ScrolledText import ScrolledText
import requests
from bs4 import BeautifulSoup

root = Tk()
#root.wm_attributes('-topmost',1) 置顶显示
root.resizable(False,False) #不允许更改窗口大小
#标题
root.title(u'快递物流查询')

#单选框
choice_list1 = [('顺丰快递',1),
                ('申通快递',2),
                ('韵达快递',3),
                ('中通快递',4),
                ('圆通快递',5),
                ('天天快递',6),
                ('百世汇通',7),
                ('宅急送',8),
                ('EMS',9)]
lf1 = LabelFrame(root,text='请选择要查询的快递公司:',padx=5,pady=5)
lf1.pack(padx=10,pady=10)
var1 = IntVar()
for cl1,num in choice_list1:
    rb1 = Radiobutton(lf1,text=cl1,value=num,variable=var1)
    rb1.pack(anchor=W,side=LEFT)

frame1 = Frame(root)
label1 = Label(frame1,text="运单号：").grid(row=0,column=0)
str_var_yundanhao = StringVar()

entry_yundanhao = Entry(frame1,textvariable=str_var_yundanhao,validate='focusout')
entry_yundanhao.grid(row=0,column=1,padx=10,pady=5)

def showMessage(title,message):
    tkMessageBox.showinfo(title,message)

def go_search(express,yundanhao):
    st1.insert(1.0,'正在查询...')
    url = 'http://wap.kuaidi100.com/wap_result.jsp?rand=20120517&id=%s&fromWeb=null&&postid=%s'%(express,yundanhao)
    try:
        html = requests.get(url,timeout=25).text
        #print html
        soup = BeautifulSoup(html,'lxml')
        st1.delete(1.0,END)
        pos = 1.0
        str_len = len(soup.find_all('p')[3:-1])
        for item in soup.find_all('p')[3:-1]:
            if int(pos) != str_len: #强迫症：最后一行不加换行
                st1.insert(pos,item.get_text()+'\r\n')
            else:
                st1.insert(pos,item.get_text())
            pos += 1.0
            #print item.get_text()
    except Exception as e:
        showMessage('发生异常',e)


def search_express():
    yundanhao = entry_yundanhao.get()
    radio_value = var1.get()
    express = ''
    if yundanhao.isdigit() == True:
        if radio_value == 0:
            showMessage('错误','请选择快递公司!')
        elif radio_value == 1:
            express = 'shunfeng'
        elif radio_value == 2:
            express = 'shentong'
        elif radio_value == 3:
            express = 'yunda'
        elif radio_value == 4:
            express = 'zhongtong'
        elif radio_value == 5:
            express = 'yuantong'
        elif radio_value == 6:
            express = 'tiantian'
        elif radio_value == 7:
            express = 'huitongkuaidi'
        elif radio_value == 8:
            express = 'zhaijisong'
        elif radio_value == 9:
            express = 'ems'
        else:
            showMessage('出错','程序出现BUG，请尝试重新运行。')
        #查询快递
        go_search(express,yundanhao)
    else:
        showMessage('错误','运单号必须为纯数字!')

btn_yundanhao = Button(frame1,text='查询快递',command=search_express).grid(row=0,column=2,padx=10,pady=5)
frame1.pack()


st1 = ScrolledText(root,
    width=55,height=10,
    font=('微软雅黑',10),
    fg='black',bg='white')#.grid(row=0,column=3)
st1.pack()

mainloop()

