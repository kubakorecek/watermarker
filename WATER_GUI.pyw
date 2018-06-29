import tkinter as tk
import subprocess
import sys

from tkinter import ttk
from tkinter import TOP,CENTER,LEFT,RIGHT,HORIZONTAL,BOTTOM,W
from PIL import ImageTk, Image

from watermarker import WATERMARKER as WK

import os


class Styles:

    LARGE_FONT = ("Verdana", 12)


class APP_GUI(tk.Tk):
    '''API GUI FUNCTION GENERAL'''
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default="icon_z.ico")
        tk.Tk.wm_title(self, "VODOZNAKOVAČ")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for FRAME in (
                StartPage,
                WaterPage,
                SizerPage,
                MenuPage
                     ):
        
            frame = FRAME(container, self)
            
            self.frames[FRAME] = frame
        
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(StartPage)
        
        
        
    def show_frame(self, cont):
    
        frame=self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    '''STARTING PAGE'''
    def __init__(self,parent,controller):
    
        
        tk.Frame.__init__(self,parent)
        self.label=ttk.Label(
            self,text="""Vodaznakování je pouze na vlastní riziko""", 
            font=Styles.LARGE_FONT
            )
        self.label.pack(pady=10,padx=10)
        
        self.button1=ttk.Button(self, 
                text="Souhlasím" ,
                width=40,
                command=lambda:controller.show_frame(MenuPage))
        self.button1.pack(side=TOP,anchor=CENTER, pady=10)
        
        self.button2=ttk.Button(self, 
            text="Nesouhlasím" , 
            width=40,
            command=sys.exit)
            
        self.button2.pack(side=TOP,anchor=CENTER, pady=10)
        
class MenuPage(tk.Frame):
    '''menu Page'''
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.label=ttk.Label(
            self,text='''Menu ''',
            font=Styles.LARGE_FONT
            )
        self.label.pack(pady=10,padx=10)
        from watermarker import WATERMARKER as WK
        
        
        self.button1=ttk.Button(self, 
            text="Vodoznakování" , 
            width=40,
            command=lambda:controller.show_frame(WaterPage))
        self.button1.pack(side=TOP,anchor=CENTER,pady=10)
        
        self.button3=ttk.Button(self, 
            text="Velikosti" , 
            width=40,
            command=lambda:controller.show_frame(SizerPage))
        self.button3.pack(side=TOP,anchor=CENTER,pady=10)
        self.button2=ttk.Button(
        
            self, text="Konec" , 
            width=40,
            command=sys.exit)
            
        self.button2.pack(side=TOP,anchor=CENTER,pady=10)
        
class SizerPage(tk.Frame):
    '''start Page'''

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
        self.label=ttk.Label(
            self,text='''Velikost''',
            font=Styles.LARGE_FONT
            )
        self.label.pack(pady=10,padx=10)
        
        self.button5=ttk.Button(self, 
            text="ZJISTI VELIKOST" ,
            width=40,
            command=self.JED_V)
        self.button5.pack(side=TOP,anchor=CENTER,pady=10)
        
        
        
        self.button4=ttk.Button(self, 
            text="MENU" ,
            width=40,
            command=lambda:controller.show_frame(MenuPage))
        self.button4.pack(side=TOP,anchor=CENTER,pady=10)
        
        self.button2=ttk.Button(
                            self, text="KONEC" , 
                            command=sys.exit,
                            width=40
                            )
            
        self.button2.pack(side=TOP,anchor=CENTER,pady=10)
        
        self.slider1=tk.Scale(
                        self,length=550,
                        tickinterval=100,
                        from_=1960,
                        to=1,
                        label="Min.Výška"
                        )
                        
        self.slider1.set(500)
        self.slider1.pack(side=LEFT)
        
        self.slider2=tk.Scale(
                        self,from_=1,
                        to=1960,
                        length=550,
                        tickinterval=100,
                        orient=HORIZONTAL,
                        label="Min.Šířka"
                        )
                        
        self.slider2.set(500)
        self.slider2.pack(side=BOTTOM)
    def SCALES_V(self):

        data=[]
        data.append(self.slider1.get())
        data.append(self.slider2.get())

        return data
    
    def JED_V(self):
        a=self.SCALES_V()
        b=WK()
        b.check_size(a[1],a[0])
        subprocess.Popen(('explorer "%s"' %b.routDIR))
        subprocess.Popen(('explorer "%s"' %b.resizeDIR))

        
class WaterPage(tk.Frame):
    '''water marker page'''
    def __init__(self,parent,controller):
        
        tk.Frame.__init__(self,parent)
        
        self.label=ttk.Label(
            self,text='''Vodoznakování ''',
            font=Styles.LARGE_FONT
            )
            
        self.label.pack(pady=10,padx=10)
        
        from watermarker import WATERMARKER as WK
        
        WKc=WK()
        size=100,100
        

        self.button1=ttk.Button(self, text="VODOZNAKUJ A ZANECH VELIKOST" , 
            width=40,
            command=lambda:self.JED('keep'))
        
        self.button3=ttk.Button(self, text="VODOZNAKUJ A ZMĚŇ VELIKOST" , 
            width=40,
            command=lambda:self.JED('change'))
        
        self.button4=ttk.Button(self, text="MENU" , 
            width=40,
            command=lambda:controller.show_frame(MenuPage))
        
        self.button2=ttk.Button(
                            self, text="KONEC" , 
                            width=40,
                            command=sys.exit,
                            
                            )
        
        self.slider1=tk.Scale(
                        self,length=550,
                        tickinterval=100,
                        from_=1960,
                        to=1,
                        label="Min.Výška"
                        )
        
        
        self.slider3=tk.Scale(
                        self,from_=0,
                        to=255,
                        length=550,
                        tickinterval=10,
                        orient=HORIZONTAL,
                        label="Průhlednost"
                        )
        
        self.slider2=tk.Scale(
                        self,from_=1,
                        to=1960,
                        length=550,
                        tickinterval=100,
                        orient=HORIZONTAL,
                        label="Min.Šířka"
                        )
        self.label1=ttk.Label(
            self,text='''Doporučená velikost je 500x500 ''',
            font=Styles.LARGE_FONT
            )
            
        self.slider1.set(500)
        self.slider3.set(35)
        self.slider2.set(500)
        
        self.slider3.pack(side=BOTTOM)
            
        
        
        
        self.button1.pack(anchor=W,pady=10,padx=10)
        self.button3.pack(anchor=W,pady=10,padx=10)
        self.button4.pack(anchor=W,pady=10,padx=10)
        self.button2.pack(anchor=W,pady=10,padx=10)
        
        self.slider1.pack(side=LEFT)
        self.slider2.pack(side=BOTTOM)
        
        self.v = tk.IntVar()
        self.v.set(0)

        for i,item in enumerate(WKc.LOGO,0):

            img=Image.open(os.path.join(str(WKc.logoDIR),str(item)))
            img.thumbnail(size, Image.ANTIALIAS)
            im=ImageTk.PhotoImage(img)
            print(self.v,i,item)
            self.panel =tk.Radiobutton(self, image=im ,
                variable=self.v,command=self.ShowChoice,value=i)
            self.panel.image=im
            self.panel.pack(anchor=CENTER)
        
        self.label1.pack(pady=10,padx=10)
        self.SCALES
        self.ShowChoice()
        
    def ShowChoice(self):
    

    
        return self.v.get()
        
    def SCALES(self):
    
        data=[]
        data.append(self.slider1.get())
        data.append(self.slider2.get())
        data.append(self.slider3.get())
        data.append(self.ShowChoice())

        return data
        
    def JED(self,mode):
        a=self.SCALES()

        b=WK()
        b.watermark_done(a[3],a[2],mode,a[1],a[0])
        subprocess.Popen(('explorer "%s"' %b.routDIR))
        if mode=='keep':
        
            subprocess.Popen(('explorer "%s"' %b.outDIR))
       
        elif mode=='change':


            subprocess.Popen(('explorer "%s"' %b.resizeWDIR))
        
ST=APP_GUI()
ST.mainloop()