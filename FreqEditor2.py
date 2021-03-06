# Notice this code is python 2.7
from Tkinter import *
import os
import struct
from array import *
import tkSimpleDialog

freq_array = array('f', [])
def about():
   filewin = Toplevel(root)
   button = Button(filewin, text="made by\n unclejed613 & OromisGlaedr")
   button.pack()


def FreqHelp():
    filewin = Toplevel(root)
    button = Button(filewin,  text = '''Frequency Editor for the Gnuradio Scanner
        This program loads the freqtest.dat file,
        and is capable of editing it. There are 3
        editing functions:
        Delete, deletes an entry
        Change, changes an entry
        Append, appends an entry
        There are 4 file functions:
        New, adds as many entrys as you want
        Open, opens the file
        Save, saves the current array
        Show refreshes the list on screen. ''')
    button.pack()


def RemoveFreq():
#    fm = int(input('freq to modify: '))  #we want to modify a particular frequency
    fm = tkSimpleDialog.askinteger('remove entry',  'remove entry:', parent = root)
#    current_freq = freq_array[fm-1]
#    print('current freq is: ', + current_freq)
#    print('removing freq')
    freq_array.pop(fm-1)
#    print('current freq is: ', + current_freq)          #we want to replace it with a new value
 #   new_freq = float(input('new frequency:  '))
    DisplayFreqs()


def AppendFreqs():
#    fm = tkSimpleDialog.askinteger('new entry',  'new entry:', parent = root)
    new_freq = tkSimpleDialog.askinteger('new entry',  'new entry:', parent = root)
    freq_array.append(new_freq)                         #except we append the frequency at the end
    for indx in range(len(freq_array)):                 #and as before print the modified list
        print(indx+1, +freq_array[indx])
        DisplayFreqs()


def MakeNewFile():
    freq_array = array('f', [])
#    entries=input("How Many Entries?  ")
    entries = tkSimpleDialog.askinteger('entries', 'How many entries?',  parent = root)
#x<11
#print ("Enter frequencies in Hz, with no decimal points")
#fout = open("freq.dat", "a")
#while True:
    for i in range(0,entries):
#        print i
#      freq=input("Frequency ")
        freq = tkSimpleDialog.askfloat('entry', 'enter frequency ' + str(i+1), parent = root)
        freq_array=array("f",[freq])
#fout.write(freq)
 #         frq=float(freq)
        with open("freqtest.dat", "ab") as x:
#                 pickle.dump(frq, x)p
            freq_array.tofile(x)
    x.close()
    DisplayFreqs()



def GetFreqs():
    stats = os.stat('freqtest.dat')
    file_size = stats.st_size
    for a in range(0, file_size, 4):
#        print(a)        #read the entries sequentially from the file
        with open('freqtest.dat', 'rb') as f:
            f.seek(a)
            bytes = f.read(4)
            freq = struct.unpack('<f', bytes)
#            b = (a/4) +1
#           frq(b) = str(freq[0])
            print('Frequency: ' + str((a/4)+1) + ' ' + str(freq[0]))  #print the entries as they are read
            freq_array.append(freq[0])                                #and add them to the array
#            f.close()
            DisplayFreqs()

def DisplayFreqs():
    for index in range(len(freq_array)+1):
        Label(text = '', relief = RIDGE, width = 30).grid(row = index,  column = 0)
        Label(text = '', bg = '#aaaacc', relief = SUNKEN, width = 20).grid(row = index,  column = 1)
    for index in range(len(freq_array)):
        Label(text = index+1, relief = RIDGE, width = 30).grid(row = index,  column = 0)
        Label(text = str(freq_array[index]), bg = '#aaaabb', relief = SUNKEN, width = 20).grid(row = index,  column = 1)
 #       Entry(text = freq_array[index], bg = 'grey', relief = SUNKEN, width = 20).grid(row = index,  column = 2)
 #       freq_array[]


def DumpFreqs():
    print('writing...  ')
    print(freq_array)
    f = open('freqtest.dat', 'wb')                          #everything done? dump the array to the file (overwrites
    f.write(freq_array)                                    #the old one)
#    freq_array.tofile(f)
#    f.close()
    DisplayFreqs()


def ModifyFreqs():
    fm = tkSimpleDialog.askinteger('change entry',  'change entry:', parent = root)
    current_freq = freq_array[fm-1]
    new_freq = tkSimpleDialog.askfloat('new freq', current_freq,  parent = root)
    freq_array[fm-1] = new_freq
    for indx in range(len(freq_array)):                 #print the modified list
        print(indx+1, +freq_array[indx])
        DisplayFreqs()


root = Tk()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=MakeNewFile)
filemenu.add_command(label="Open", command=GetFreqs())
filemenu.add_command(label="Save", command=DumpFreqs)
filemenu.add_command(label="Show", command=DisplayFreqs())

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)

editmenu.add_command(label="Delete", command=RemoveFreq)
editmenu.add_command(label="Append", command=AppendFreqs)
editmenu.add_command(label="Change", command=ModifyFreqs)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=FreqHelp)
helpmenu.add_command(label="About...", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)


root.config(menu=menubar)
root.mainloop()

