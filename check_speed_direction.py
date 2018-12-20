import tkinter
from tkinter import messagebox
import os
def check2():
    textfile=open("count.txt","r")
    count2=textfile.read()
    count=int(count2)
    if count>0:
        textfile=open("vertical_record.txt","r")
        vertical=textfile.read().split(',')
        textfile.close()
        textfile=open("horizontal_record.txt","r")
        horizontal=textfile.read().split(',')
        textfile.close()
        if vertical[count]==' ' or horizontal[count]==' ':
            print("image not clear")
            return
        if int(vertical[count])-int(vertical[count-1])>0 and int(horizontal[count])-int(horizontal[count-1])>0:
            print("->(increasing)")
        if int(vertical[count])-int(vertical[count-1])<0 and int(horizontal[count])-int(horizontal[count-1])>0:
            print("->(decreasing)")
        if int(vertical[count])-int(vertical[count-1])>0 and int(horizontal[count])-int(horizontal[count-1])<0:
            print("<-(increasing)")
        if int(vertical[count])-int(vertical[count-1])<0 and int(horizontal[count])-int(horizontal[count-1])>0:
            print("<-(decreasing)")
        if int(vertical[count])-int(vertical[count-1])>0 and int(horizontal[count])-int(horizontal[count-1])==0:
            print("(increasing)")
        if int(vertical[count])-int(vertical[count-1])<0 and int(horizontal[count])-int(horizontal[count-1])==0:
            print("(decreasing)")
        if count>6 and int(vertical[count])-int(vertical[count-1])/3>8:

            duration = 7 #
            freq = 440  # Hz
            os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
        if count>6 and int(vertical[count])-int(vertical[count-1])/3>7:
            messagebox.showwarning("Warning","Vehicle above speed limits")
            #continue
