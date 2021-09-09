from tkinter import *
import controller
import checkbox

class frameChild:
    def __init__(self,location,width,text,row=0,column=0,initial=0):
        self.loca=location
        self.width=width
        self.text=text
        self.field = Entry(self.loca, width=self.width)
        checkbox.checkBoxT(self.field,location)
        self.label = Label(self.loca, text=self.text)
        self.row = row
        self.col=column
        self.initial = initial

    def value(self):
        return self.field.get()

    def grids(self):
        self.field.grid(row=self.row,column=self.col*3)
        self.field.insert(0, str(self.initial))
        self.label.grid(row=self.row,column=self.col*3+1)
        Label(self.loca, text="  ").grid(row=self.row,column=self.col*3+2)


def userInput(target,location):
    target.update()
    myLabel = Label(location, text=target.value)
    myLabel.grid()
def cte(obj):
    return obj.resizable(width=FALSE, height=FALSE)


root = Tk()
root.title('Auto Clicker ver 1.0')
root.geometry('460x325')
root.resizable(width=FALSE, height=FALSE)
root.grid_columnconfigure(1, weight=0,minsize=265)
root.grid_rowconfigure(1, weight=0,minsize=100)

#all frames
frame1 = LabelFrame(root,text="Click interval",padx=5,pady=10,width= 400)
frame1.grid(columnspan=12,padx=10,row=0,sticky='ew')

frame2 = LabelFrame(root,text="Click options",padx=5,pady=2)
frame2.grid(rowspan=2,padx=10,pady=5,row=1,column=0,sticky='nsew')
frame2.grid_columnconfigure(0,minsize=80)
frame3 = LabelFrame(root,text="Click repeat",padx=5,pady=10)
frame3.grid(rowspan=2,padx=10,pady=5,row=1,column=1,sticky='nsew')

frame4 = LabelFrame(root,text="Cursor position",padx=5,pady=10)
frame4.grid(columnspan=8,padx=10,row=3,sticky='ew')


#frame1
eWidth=8
i1= frameChild(frame1,eWidth,"hours",column=0)
i1.grids()
i2= frameChild(frame1,eWidth,"mins",column=1)
i2.grids()
i3= frameChild(frame1,eWidth,"secs",column=2)
i3.grids()
i4= frameChild(frame1,eWidth,"milleseconds",column=3,initial=100)
i4.grids()


#frame2
label1f2 = Label(frame2,text='Mouse button:')
label1f2.grid(row=0,column=0,sticky='w')

label2f2 = Label(frame2,text='Click type:')
label2f2.grid(row=1,column=0,sticky='w')

li1 = ['Left','Right','Middle']
clickButton=StringVar()
clickButton.set(li1[0])
drop1=OptionMenu(frame2,clickButton,*li1)
drop1.config(width = 6)
drop1.grid(row=0,column=1,sticky='w')

li2 = ['Single','Double']
clickType=StringVar()
clickType.set(li2[0])
drop2=OptionMenu(frame2,clickType,*li2)
drop2.config(width = 6)
drop2.grid(row=1,column=1)

'''label1f3 =Label(frame3,text='Repeat')
label2f3 = Label(frame3,text='Repeat until stopped')
label1f3.grid(row=0,column=0)
label2f3.grid(row=1,column=0)'''


#frame3
choose=IntVar()
choose.set("1")
Radiobutton(frame3,text='Repeat',variable=choose,value=1).grid(row=0,column=0,sticky='w') #i dont know why it is not working
Radiobutton(frame3,text='Repeat until stopped',variable=choose,value=2).grid(row=1,column=0,sticky='w')
box3=Spinbox(frame3, from_=1, to=10000,width=8)
box3.grid(row=0,column=1)

#frame4
ji=0
Label(frame4,text='Click location').grid(row=0,column=ji,sticky='e')
Label(frame4,text="    ").grid(row=0,column=ji+1)
l1f4 = Label(frame4,text="X").grid(row=0,column=ji+2,sticky='e')
e1f4 = Entry(frame4,width=8)
e1f4.insert(0,0)
e1f4.grid(row=0,column=ji+3,sticky='e')


l2f4 = Label(frame4,text="Y").grid(row=0,column=ji+4,sticky='e')
e2f4 = Entry(frame4,width=8)
e2f4.insert(0,0)
e2f4.grid(row=0,column=ji+5,sticky='e')
Label(frame4,text="                   ").grid(row=0,column=ji+6)
Button(frame4,text="Pick location").grid(row=0,column=ji+7,sticky='e')

#control button

def endButton():
    pass

def startButton():
    numberOfClick = 1
    if str(choose.get()) == '1':
        numberOfClick = int(box3.get())
    elif str(choose.get()) == '2':
        numberOfClick = 1000000000
    xc=e1f4.get()
    yc=e2f4.get()
    interval = int(i1.value())*3600+int(i2.value())*60+int(i3.value())+int(i4.value())/1000
    controller.repeatClick(xc,yc,numberOfClick,interval,type=str(clickType.get()),button=str(clickButton.get()))
Button(root,text="Start",pady=30,command=startButton).grid(row=5,column=0, sticky='nesw',padx=10,pady=10)
Button(root,text="End",pady=30).grid(row=5,column=1, sticky='nesw',padx=10,pady=10)

root.mainloop()
