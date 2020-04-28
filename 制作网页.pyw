import os,sys,random
from tkinter import*
from tkinter.ttk import*
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
# from tkinter import message
from tkinter.scrolledtext import ScrolledText
import webbrowser;from tkinter import*;from tkinter import messagebox;from tkinter.ttk import*
def bubble_sort(list111):
    count = len(list111)
    for i in range(count):
        for j in range(i + 1, count):
            if eval(list111[i]["score"]) < eval(list111[j]["score"]):
                list111[i], list111[j]= list111[j], list111[i]
    return list111

mo="""     <div class="item">
        		<div class="animate-box">
	        		<a href="{url}" title="{H}" target="_blank"><img src="{img}" alt="{H}"></a>
        		</div>
        		<h3 style="font-size:20px;text-align: center;color: black">{H}</h1>
				<h6 style="text-align: center;color:darkgrey">作者:{name}</h6>
				<h5 style="text-align: center;color:darkblue">评分:{S}</h5>
        	</div>
        	"""
def replace(strname,*w):
    for x in w:
        strname=strname.replace(x[0],x[1])
    return strname


def saveFile():
    global filename,mo,data

    filename="index.html"
    dta=bubble_sort(data)


    with open(filename,"w",encoding="utf-8") as f:
        with open("base.html","r",encoding="utf-8") as z:
            kkk=z.read()
        k=""
        for x in dta:
            k+=replace(mo,("{H}",x["name"]),("{name}",x["user_name"]),("{img}",x["img"]),("{S}",x["score"]),("{url}",x["url"]))
        kkk=kkk.replace("{wen}",k)
        f.write(str(kkk))
        root.title(filename)
    sava_data()
def add():
    global data
    dic={"name":H.get(),"user_name":name.get(),"img":img.get(),"score":S.get(),"url":url.get()}
    tree.insert("", index=END, text=dic["name"],
        values=(dic["user_name"],dic["img"],dic["score"],dic["url"]))

    data.append(dic)

def sava_data():
    with open("data.txt", "w", encoding="utf-8") as f:
        f.write(str(data))
filename="未命名"

try:
    k=open("data.txt","r", encoding="utf-8")
    data=eval(k.read())
    k.close()
except:
    data=[]

root=Tk()
root.title(filename)
root.geometry("680x770")

#menu====================
menubar=Menu(root)
filemenu=Menu(menubar,tearoff=False)
menubar.add_cascade(label="文件",menu=filemenu)
filemenu.add_command(label="保存数据",command=sava_data)
filemenu.add_command(label="导出html",command=saveFile)
filemenu.add_separator()
filemenu.add_command(label="退出",command=root.destroy)
root.config(menu=menubar)
#end======================


#tree======================
tree=Treeview(root,columns=("H","name","img","S","url"))
tree.heading("#0",text="名字")
tree.heading("#1",text="用户名")
tree.heading("#2",text="图片")
tree.heading("#3",text="分数")
tree.heading("#4",text="url")
try:
    for dic in data:
        tree.insert("", index=END, text=dic["name"],
                    values=(dic["user_name"], dic["img"], dic["score"], dic["url"]))
except:
    print("no dta")
    pass

#end======================

#entry====================
H=Entry(root)
name=Entry(root)
img=StringVar()
combox=Combobox(root,textvariable=img,value=("images/python.png","images/C++.png",))
S=Entry(root)
url=Entry(root)
add_option_bu=Button(root,text="插入",command=add).pack(fill=X)
#end======================
H.pack(fill=X)
name.pack(fill=X)
combox.pack(fill=X)
S.pack(fill=X)
url.pack(fill=X)

tree.pack(fill=BOTH,expand=True)
root.mainloop()








