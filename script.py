import numpy as np
import pandas as pd
from tkinter import *

#import data from csv file.
df = pd.read_csv("Data.csv")
df = np.array(df)


#doTranslate function.
def doTranslate():
    string = word.get()
    string = string.capitalize()
    print(string)
    res=model.check(string)
    if res == -1:
        print("not found")
        result.set("not found")
    else:
        #res=res.split("::")
        #res.join("\n") 
        print(res)
        result.set(res)

#Trie class
class Trie:
    def __init__(self):
        self.nodes=0
        self.statusNode=[-1]
        self.table=[[-1]*128]
    def insert(self,string,tran):
        cnt=0
        for ch in string:
            if self.table[cnt][ord(ch)] != -1 :
                cnt=self.table[cnt][ord(ch)]
            else:
                self.nodes+=1
                self.table.append([-1]*128)
                self.statusNode.append(-1)
                self.table[cnt][ord(ch)]=self.nodes
                cnt = self.table[cnt][ord(ch)]
            #print(cnt)
        self.statusNode[cnt]=tran
        #print("DONE...")                
    

    def check(self,string):
        cnt=0
        for ch in string:
            if self.table[cnt][ord(ch)] != -1 :
                cnt=self.table[cnt][ord(ch)]
            else:
                return -1
        return self.statusNode[cnt]            


print("loading...")

#create object from Trie class.
model = Trie()

for t in df:
    #print(t)
    string = t[1].strip()
    model.insert(string,t[2])
    
print("Done")
    

#set GUI for app
app = Tk()
app.title("transilation app english to arabic")
app.geometry("500x300")

word = StringVar()
result=StringVar()


the_text = Label(app,height=2,font = ("Arial",20),text="Enter a word : ")
the_text.pack()

word_input = Entry(app,width=10,font=("Arial",30),textvariable = word)
word_input.pack()

btn = Button(app,text="translate",width=20,height=2,bg="#e91e63",fg="white",borderwidth=0,command=doTranslate)
btn.pack()

the_res = Label(app,textvariable=result,height=2,font = ("Arial",20))
the_res.pack()

app.mainloop()
