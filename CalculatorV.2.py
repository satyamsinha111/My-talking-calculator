# Smart interactive calculator build with fun
# Author :------> Satyam sinha
# notice please read its readme file before executing


import tkinter  #tkinter module imported for making the graphical user interface
from gtts import gTTS  #this import one of the google library google text to speech for converting our text to speech
import playsound  #this library will play the speech

class myDisplay:   # class is defined which containts all the variables widgets of the calculator
    def __init__(self,master): #__init__ fuction initialises some of the widgets and functions
        label=tkinter.Label(master,text="Smart Calculator",bg="#DAE0E2",fg="#2C3335",height=3,width=50) #this gives the main heading to my calculator
        label.config(font=('monospace',12,'bold')) #set font style of label to monospace size to 12pixels and weight is bold
        label.pack()
        self.frm=tkinter.Frame(master,width=50) # frame is initialised
        self.frm.pack()
        self.mainWindow=master
    def __One(self):
        self.display['state']='normal'
        self.display.insert(tkinter.END,self.btn1['text'])
        self.display['state'] = 'disabled'
    def __Two(self):
        self.display['state']='normal'
        self.display.insert(tkinter.END,self.btn2['text'])
        self.display['state'] = 'disabled'
    def __Three(self):
        self.display['state']='normal'
        self.display.insert(tkinter.END,self.btn3['text'])
        self.display['state'] = 'disabled'
    def __Four(self):
        self.display['state']='normal'
        self.display.insert(tkinter.END,self.btn5['text'])
        self.display['state'] = 'disabled'
    def __Five(self):
        self.display['state']='normal'
        self.display.insert(tkinter.END,self.btn6['text'])
        self.display['state'] = 'disabled'
    def __Six(self):
        self.display['state']='normal'
        self.display.insert(tkinter.END,self.btn7['text'])
        self.display['state'] = 'disabled'
    def __Seven(self):
        self.display['state']='normal'
        self.display.insert(tkinter.END,self.btn9['text'])
        self.display['state'] = 'disabled'
    def __Eight(self):
        self.display['state']='normal'
        self.display.insert(tkinter.END,self.btn10['text'])
        self.display['state'] = 'disabled'
    def __Nine(self):
        self.display['state']='normal'
        self.display.insert(tkinter.END,self.btn11['text'])
        self.display['state'] = 'disabled'
    def __Add(self):
        self.display['state']='normal'
        self.display.insert(tkinter.END,self.btn13['text'])
        self.display['state'] = 'disabled'
    def __Subtract(self):
        self.display['state']='normal'
        self.display.insert(tkinter.END,self.btn14['text'])
        self.display['state'] = 'disabled'
    def __Percent(self):
        self.display['state']='normal'
        self.display.insert(tkinter.END,self.btn4['text'])
        self.display['state'] = 'disabled'
    def __Multiply(self):
        self.display['state']='normal'
        self.display.insert(tkinter.END,self.btn15['text'])
        self.display['state'] = 'disabled'
    def __Divide(self):
        self.display['state']='normal'
        self.display.insert(tkinter.END,self.btn8['text'])
        self.display['state'] = 'disabled'
    def __Clear(self):
        self.display['state']='normal'
        self.display.delete(0,tkinter.END)
        self.display['state'] = 'disabled'
    def __Result(self):
        self.display['state']='normal'
        str=self.display.get()
        self.display.delete(0,tkinter.END)
        if '+' in str:
            pos=str.find('+')
            num1=str[0:pos]
            num2=str[pos+1:]
            result=float(num1)+float(num2)
            r1=gTTS(f"Sum of {num1} and {num2} is {result}")
            r1.save('r1.mp3')
            playsound.playsound('r1.mp3')
            self.display.insert(0,result)
        elif '-' in str:
            pos=str.find('-')
            num1=str[0:pos]
            num2=str[pos+1:]
            result=float(num1)-float(num2)
            r2=gTTS(f"Difference of {num1} and {num2} is {result}")
            r2.save('r2.mp3')
            playsound.playsound('r2.mp3')
            self.display.insert(0,result)
        elif '/' in str:
            pos=str.find('/')
            num1=str[0:pos]
            num2=str[pos+1:]
            result=float(num1)/float(num2)
            r3=gTTS(f" {num1} divides {num2} is equal {result}")
            r3.save('r3.mp3')
            playsound.playsound('r3.mp3')
            self.display.insert(0,result)
        elif 'x' in str:
            pos=str.find('x')
            num1=str[0:pos]
            num2=str[pos+1:]
            result=float(num1)*float(num2)
            r4=gTTS(f"Product of {num1} and {num2} is {result}")
            r4.save('r5.mp3')
            playsound.playsound('r5.mp3')
            self.display.insert(0,result)
        elif '%' in str:
            pos=str.find('+')
            num1=str[0:pos]
            result=float(num1)/100
            r5=gTTS(f"{num1} percent is {result}")
            r5.save('r5.mp3')
            playsound.playsound('r5.mp3')
            self.display.insert(0,result)
        else:
            self.display.delete(0,tkinter.END)
            self.display.insert(0,"Error occured")
        self.display['state'] = 'disabled'

    def intro(self): #this function is called by the object atfirst
        self.root=tkinter.Tk()
        self.root.geometry('200x200')
        self.root.config(bg="#8395A7")
        welcome="Welcome!  What is your name?"
        introduction=gTTS(welcome)
        introduction.save('WEl.mp3')
        playsound.playsound('WEl.mp3')
        self.name=tkinter.Entry(self.root)
        self.name.pack()
        btn=tkinter.Button(self.root,text="Proceed",command=self.__display).pack() #this buttion onclick will execute the private function __display


    def __display(self): # this is the function which will execute the body of the calculator
        #below this I defined the buttons display etc of the calculator using widgets
        str=self.name.get()
        speech1=gTTS(str)
        speech1.save('Buffer.mp3')
        speech=gTTS(f"hello {str} welcome to smart calculator")
        speech.save('name.mp3')
        playsound.playsound('name.mp3') 
        self.root.destroy()
        self.display=tkinter.Entry(self.frm,state='disabled',width=30,text="Do your calculations here")
        self.display.grid(row=0,columnspan=4)
        self.btn1=tkinter.Button(self.frm,text="1",bg="#2B2B52",fg="#EAF0F1",width=5,height=2,command=self.__One)
        self.btn1.grid(row=1,column=0)
        self.btn2 = tkinter.Button(self.frm, text="2", bg="#2B2B52", fg="#EAF0F1", width=5, height=2,command=self.__Two)
        self.btn2.grid(row=1, column=1)
        self.btn3 = tkinter.Button(self.frm, text="3", bg="#2B2B52", fg="#EAF0F1", width=5, height=2,command=self.__Three)
        self.btn3.grid(row=1, column=2)
        self.btn4 = tkinter.Button(self.frm, text="%", bg="#2B2B52", fg="#EAF0F1", width=5, height=2,command=self.__Percent)
        self.btn4.grid(row=1, column=3)

        self.btn5 = tkinter.Button(self.frm, text="4", bg="#2B2B52", fg="#EAF0F1", width=5, height=2,command=self.__Four)
        self.btn5.grid(row=2, column=0)
        self.btn6 = tkinter.Button(self.frm, text="5", bg="#2B2B52", fg="#EAF0F1", width=5, height=2,command=self.__Five)
        self.btn6.grid(row=2, column=1)
        self.btn7 = tkinter.Button(self.frm, text="6", bg="#2B2B52", fg="#EAF0F1", width=5, height=2,command=self.__Six)
        self.btn7.grid(row=2, column=2)
        self.btn8 = tkinter.Button(self.frm, text="/", bg="#2B2B52", fg="#EAF0F1", width=5, height=2,command=self.__Divide)
        self.btn8.grid(row=2, column=3)

        self.btn9 = tkinter.Button(self.frm, text="7", bg="#2B2B52", fg="#EAF0F1", width=5, height=2,command=self.__Seven)
        self.btn9.grid(row=3, column=0)
        self.btn10 = tkinter.Button(self.frm, text="8", bg="#2B2B52", fg="#EAF0F1", width=5, height=2,command=self.__Eight)
        self.btn10.grid(row=3, column=1)
        self.btn11 = tkinter.Button(self.frm, text="9", bg="#2B2B52", fg="#EAF0F1", width=5, height=2,command=self.__Nine)
        self.btn11.grid(row=3, column=2)
        self.btn12 = tkinter.Button(self.frm, text="=", bg="#2B2B52", fg="#EAF0F1", width=5, height=2,command=self.__Result)
        self.btn12.grid(row=3, column=3)

        self.btn13 = tkinter.Button(self.frm, text="+", bg="#2B2B52", fg="#EAF0F1", width=5, height=2,command=self.__Add)
        self.btn13.grid(row=4, column=0)
        self.btn14 = tkinter.Button(self.frm, text="-", bg="#2B2B52", fg="#EAF0F1", width=5, height=2,command=self.__Subtract)
        self.btn14.grid(row=4, column=1)
        self.btn15= tkinter.Button(self.frm, text="x", bg="#2B2B52", fg="#EAF0F1", width=5, height=2,command=self.__Multiply)
        self.btn15.grid(row=4, column=2)
        self.btn16 = tkinter.Button(self.frm, text="cls", bg="#2B2B52", fg="#EAF0F1", width=5, height=2,command=self.__Clear)
        self.btn16.grid(row=4, column=3)


#This initialises the basic window

win=tkinter.Tk()
win.geometry('180x247')#this sets it to a cross section of 180x247
win.config(bg='#7B8788')#sets background to a specific color code

md=myDisplay(win)# Our class is called with an argument of window widget
md.intro()#this calles one of the fuction in class which gives you introduction
win.mainloop()#this prevents the window from closing unless we close it
