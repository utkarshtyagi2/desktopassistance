import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import *
from tkinter import filedialog, Text
import os

url ='https://www.sarkariresult.com/latestjob.php'
res=[]
def getdata(url):
    r= requests.get(url)
    return r.text
def getinfo():
    htmldata = getdata(url)
    soup = BeautifulSoup(htmldata, 'html.parser')
    result =""
    
    for li in soup.find_all("div", id="post"):
        
        result += (li.get_text())
    res.set(result)

# tkinter to make gui
root=tk.Tk()

canvas = tk.Canvas(root, height=500, width= 800, bg="black")
canvas.pack()

frame = tk.Frame(canvas, bg="light grey")

frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
# variable classes in tkinter
res=StringVar()
Label(frame, text="List of the jobs :",bg="light grey",font="100").grid(row=0, sticky=W)
Label(frame, text="",textvariable=res, bg="light grey").grid(row=3,column=0, sticky=W)
openFile = tk.Button(root, text="open file", padx="5", pady="10" ,fg="white", bg="red" )
getinfo()
openFile.pack()


root.mainloop()
