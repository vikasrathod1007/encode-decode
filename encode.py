from tkinter import *
import random

A=Tk()
A.title("Encoding Decoding")
master=Label(A,bg="orange")
master.pack()




         
Label(master,text="Enter the key = ",bg="orange",font="Bahnschrift").grid(row=0,column=0)
Label(master,text="Enter your message:",bg="orange",font="Bahnschrift").grid(row=1,column=0)
Label(master,text="Your encrypted message is:",bg="orange",font="Bahnschrift").grid(row=3,column=0)
Label(master,text="Enter the key = ",bg="orange",font="Bahnschrift").grid(row=4,column=0)
Label(master,text="Enter your message:",bg="orange",font="Bahnschrift").grid(row=5,column=0)
Label(master,text="Your decrypted message is:",bg="orange",font="Bahnschrift").grid(row=7,column=0)

alphabet = "abcdefghijklmnopqrstuvwxyz"

var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
var5 = IntVar()
var6 = IntVar()

e=Entry(master,textvariable=var5,width=4).grid(row=0,column=1)
e1=Entry(master,textvariable=var1,width=40).grid(row=1,column=1)
e2=Entry(master,textvariable=var2,width=40).grid(row=3,column=1)
e5=Entry(master,textvariable=var6,width=4).grid(row=4,column=1)
e3=Entry(master,textvariable=var3,width=40).grid(row=5,column=1)
e4=Entry(master,textvariable=var4,width=40).grid(row=7,column=1)

#vcmd = master.register(self.validate)
#self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))


def encrypt():
     try:
        key = var5.get()
        newmessage = ''
        mystring = var1.get()
        for character in mystring:
               if character in alphabet:
                 position = alphabet.find(character)
                 newposition = (position + int(key)) % 26
                 newcharacter = alphabet[newposition]
                 newmessage += newcharacter
               else:
                newmessage += character
        var2.set(newmessage)
        return
     except:
          print("Enter Encoding key")

def decrypt():
        try:
             key = var6.get()
             newmessage = ''
             mystring = var3.get()
             for character in mystring:
                 if character in alphabet:
                     position = alphabet.find(character)
                     newposition = (position - int(key)) % 26
                     newcharacter = alphabet[newposition]
                     newmessage += newcharacter
                 else:
                     newmessage += character
             var4.set(newmessage)

             return
        except:
             print("Enter Decoding key")
          
def Exit():
     A.destroy()
     exit()
     return


b1=Button(master,text="Encrypt",command=encrypt).grid(row=2,column=1)
b2=Button(master,text="Decrypt",command=decrypt).grid(row=6,column=1)
b3=Button(master,text="Close",command=Exit).grid(row=8,column=1)



mainloop()
