import pygame
from pygame import mixer
from tkinter import *
import os
def playsong():
  currentsong=playlist.get(ACTIVE)
  print(currentsong)
  mixer.music.load(currentsong)
  songstatus.set("Playing")
  mixer.music.play()
def pausesong():
  songstatus.set("Paused")
  mixer.music.pause()
def stopsong():
  songstatus.set("Stopped")
  mixer.music.stop()
def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()
def exit():
  root.destroy()    
root=Tk()
root.title('Music player project')
root.attributes('-fullscreen',True)
mixer.init()
songstatus=StringVar()
songstatus.set("choosing")
#playlist---------------
playlist=Listbox(root,selectmode=SINGLE,bg="black",fg="white",font=('arial',15),width=40)
playlist.place(x=0,y=26,relwidth=1,height=624)
os.chdir(r'C:\Users\Jheel\Desktop\songs')
songs=os.listdir()
for s in songs:
  playlist.insert(END,s)
title=Label(root,text="Music Player",font=("arial",20),bg="#006400",fg="white").place(x=0,y=0,relwidth=1,height=26)
bottom=Label(root,font=("arial",20),bg="#006400").place(x=0,y=650,relwidth=1,height=70)
#click_btn= PhotoImage(r'C:\Users\Jheel\Desktop\python\play.png')
#img_label= Label(image=click_btn)
play = PhotoImage(file = r"C:\Users\Jheel\Desktop\python\play.png")
pause = PhotoImage(file = r"C:\Users\Jheel\Desktop\python\pause.png")
stop = PhotoImage(file = r"C:\Users\Jheel\Desktop\python\stop.png")
resume = PhotoImage(file = r"C:\Users\Jheel\Desktop\python\resume.png")
playbtn=Button(root,text="play", image=play,command=playsong,font=('arial',20),padx=7,pady=7).place(x=550,y=665,width=40,height=40)
pausebtn=Button(root,text="Pause", image=pause,command=pausesong,font=('arial',20),padx=7,pady=7).place(x=600,y=665,width=40,height=40)
stopbtn=Button(root,text="Stop", image=stop,command=stopsong,font=('arial',20),padx=7,pady=7).place(x=650,y=665,width=40,height=40)
Resumebtn=Button(root,text="Resume", image=resume,command=resumesong,font=('arial',20),padx=7,pady=7).place(x=700,y=665,width=40,height=40)
exitbtn=Button(title,text="X",bg="#ff6347",fg="white",command=exit,width=5,font=("arial",9,"bold")).pack(side=TOP,anchor=NE)
mainloop()