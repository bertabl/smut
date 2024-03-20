#!/usr/bin/env python3
usage='python WaveformInspector path/data_file.root'

hotkeys='''
   --- List of key bindings ---
0-7:        toggle channel 0 to 7
<Space>:    next event
b:          previous event
q:          quit
'''

# # give focus to the GUI window in Mac
# # https://stackoverflow.com/questions/17774859
# from os import system
# from platform import system as platform
# if platform() == 'Darwin':  # How Mac OS X is identified by Python
#     system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')


# get run folder
from sys import argv
if len(argv)<2: print(usage); exit()
folder=argv[1]

print("check ROOT files in "+folder+":")
from os import path
import uproot
nfile=0; nevt=0
if path.exists(folder):
    branches=uproot.open(folder)['Data_F'].arrays()
    nevt=len(branches)
    print(folder+" contains "+str(nevt)+" events")
    if nevt>0: nfile+=1
if nfile<1: print("no valid root file in "+folder+", quit"); exit()

title="There are "+str(nevt)+" events in run folder "+folder
title+=" (press h for help, q to quit)"
from tkinter import Tk, Label, Entry, END, TOP, LEFT, BOTH
root = Tk(); root.wm_title(title)

timestamp_old=0

# canvas
from matplotlib.figure import Figure
fig=Figure(); ax1=fig.add_subplot(121); ax2=fig.add_subplot(122) 

line=0
if nevt>0: 
    line,=ax1.plot(branches['Samples'][0],label="channel "+str(branches['Channel'][0]))   
    ax2.text(0.1,0.8, "Energy (ADC channel) " + str(branches['Energy'][0]))
    timestamp_old = branches['Timestamp'][0]/1000000000000
    ax2.text(0.1,0.6, "Timestamp(sec) " + str(timestamp_old))
    ax2.text(0.1,0.2, "channel # " + str(branches['Channel'][0]))
ax1.legend()
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
canvas = FigureCanvasTkAgg(fig, master=root); canvas.draw()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)



# tool bar
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
toolbar=NavigationToolbar2Tk(canvas, root)

Label(toolbar, text="Event:").pack(side=LEFT)
evtSpecifier=Entry(toolbar, width=8)
evtSpecifier.insert(0, '0')
evtSpecifier.pack(side=LEFT)
# https://stackoverflow.com/a/42194708/1801749
def discard_modification(event): canvas.get_tk_widget().focus_force()
evtSpecifier.bind('<Escape>', discard_modification)

# functions and associated key bindings
def jump_to_event(event=None):
    global timestamp_old
    evt = evtSpecifier.get()
    if not evt.isdigit(): return
    if int(evt) < 0: evt='0'
    if int(evt) > nevt: evt=str(nevt-1)
    evtSpecifier.delete(0, END); evtSpecifier.insert(0, evt);
    # update canvas
    if line.get_visible():
        line.set_ydata(branches['Samples'][int(evt)])
    ax1.relim(); ax1.autoscale_view(); ax1.set_label("channel "+str(branches['Channel'][int(evt)])); ax1.legend(); 
    #update second canvas with values
    ax2.clear()
    ax2.text(0.1,0.8, "Energy (ADC channel) " + str(branches['Energy'][int(evt)]))
    timestamp_new = branches['Timestamp'][int(evt)]/1000000000000
    ax2.text(0.1,0.6, "Timestamp_new (sec) " +str(timestamp_new))     
    timestamp_dif = timestamp_new - timestamp_old
    ax2.text(0.1,0.4, "timestamp_dif (sec) " +str(timestamp_dif))
    timestamp_old = timestamp_new
    ax2.text(0.1,0.2, "channel # " + str(branches['Channel'][int(evt)]))
    canvas.draw()
# https://stackoverflow.com/questions/47475783
evtSpecifier.bind('<Return>', jump_to_event)

def show_previous_event():
    evt = evtSpecifier.get()
    if not evt.isdigit(): return
    evt = str(int(evt)-1)
    evtSpecifier.delete(0, END); evtSpecifier.insert(0, evt);
    jump_to_event()

def show_next_event():
    evt = evtSpecifier.get()
    if not evt.isdigit(): return
    evt = str(int(evt)+1)
    evtSpecifier.delete(0, END); evtSpecifier.insert(0, evt);
    jump_to_event()

def toggle_ch(event):
    ch=int(event.key)
    if ch>7 or ch<0: return
    if line==0: return
    if line.get_visible(): line.set_visible(False)
    else: line.set_visible(True)
    ax.legend(); canvas.draw()

from matplotlib.backend_bases import key_press_handler
def handle_key_press(event):
    if event.key=="q": root.quit(); root.destroy()
    elif event.key.isdigit(): toggle_ch(event)
    elif event.key=="h": print(hotkeys)
    elif event.key==" ": show_next_event()
    elif event.key=="b": show_previous_event()
    else: key_press_handler(event, canvas) # handle default matplotlib hotkeys
canvas.mpl_connect("key_press_event", handle_key_press)

# give focus to the GUI window in Mac
# https://stackoverflow.com/questions/17774859
#from os import system
#from platform import system as platform
#if platform() == 'Darwin':  # How Mac OS X is identified by Python
 #   system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')

# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.
root.mainloop()
