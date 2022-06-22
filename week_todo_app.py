###
#A weekly todo App (using tkinter, button, entry, listbox) with functions:
#add, delete events for selected weekday
#listbox is used to show events of selected day
###

from tkinter import *
from tkinter import messagebox

print('Launch App ====== ')



# --------- event functions ---------- #

def displayEvent(text,todo_this_week,whichday):
    """
    display events of selected day
    INPUT:
    text: indicate which day of the week
    todo_this_week: the dictionary contains every weekday's todo list
    whichday: a one-item list to keep track of which weekday, whichday will be updated to the selected day (text) once the button of this day is clicked. it will be used later for editing events
    """

    # determine which day (given by text) to work on, pull out this day's todo list
    if text == "MON":
      event_list = todo_this_week['MON']
    elif text == "TUE":
      event_list = todo_this_week['TUE']
    elif text == "WED":
      event_list = todo_this_week['WED']
    elif text == "THU":
      event_list = todo_this_week['THU']
    elif text == "FRI":
      event_list = todo_this_week['FRI']
    elif text == "SAT":
      event_list = todo_this_week['SAT']
    elif text == "SUN":
      event_list = todo_this_week['SUN']
    else:
      event_list = []

    #clear listbox and show this day's to do list
    lb.delete(0,END)
    #show events for selected day
    for item in event_list:
       iscomplete = " "
       if item["done"] == False:
          iscomplete = " "
       else:
          iscomplete = " DONE!"
       item_details = item["name"] + " from " + item["from"] + " to " + item["to"] + iscomplete
       lb.insert(END, item_details)
    
    #update whichday to the selected day, which is to be used for add and remove event
    whichday.pop(0)
    whichday.append(text)
   
#add event to select weekday
def newEvent(whichday,todo_this_week):
    #read event from entries
    event = event_entry.get()
    fromtime = from_entry.get()
    totime = to_entry.get()
    isdone = False
    if isdone == False:
       iscomplete = " "
    else:
       iscomplete = "DONE!"
    task = event + " from " + fromtime + " to " + totime + " " + iscomplete
    
    #update listbox (added to end) for this day
    if event != "":
        lb.insert(END, task)
        event_entry.delete(0, "end")
        from_entry.delete(0, "end")
        to_entry.delete(0, "end")
        #update todo list for this day in todo_this_week (append to end)
        thisday = whichday[0]
        ev = {"name":event, "from": fromtime, "to": totime, "done":isdone}
        todo_this_week[thisday].append(ev)
    else:
        messagebox.showwarning("warning", "Please enter some event.")
     

#remove event from select weekday
def deleteEvent(whichday,todo_this_week):
    #delete event from listbox and from todo_this_week
    thisday = whichday[0]
    for item in lb.curselection():
        lb.delete(item)
        todo_this_week[thisday].pop(item)
  

# --------------------------------------------- #
# initialize disctionary for todo list of the week
todo_this_week = {"MON": [], "TUE": [], "WED": [], "THU": [], "FRI": [], "SAT": [], "SUN": []}


# --------------------------------------------- #

#tkinter window

#window for App
app_win = Tk()
app_win.geometry('800x600')
app_win.title('Weekly ToDo Lists')
app_win.config(bg='gray')
app_win.resizable(width=False, height=False)

# --------------------------------------------- #

#Add listbox with scrollbar
frame = Frame(app_win)
frame.pack(pady=10)

#row 0: list box with scroll bar
lb = Listbox(
    frame,
    width=60,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='black',
    highlightthickness=0,
    selectbackground='green',
    activestyle="none",
)
lb.grid(row=0,column=0,columnspan=6,sticky=N+S)
sb = Scrollbar(frame)
sb.grid(row=0,column=7,sticky=N+S)
lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

# --------------------------------------------- #

#Add buttons for weekday selection
#row 1: week day buttons: Mon, Tue, ... , Sat, Sun
button_frame = Frame(app_win)
button_frame.pack(pady=20)

whichday = ["MON"] # for indicating which day of the week

addDay = Button(
    button_frame,
    text='MON',
    font=('times 14'),
    bg= 'white',
    fg = 'black',
    activebackground = 'black',
    activeforeground = 'green',
    padx=20,
    pady=10,
    command= lambda: displayEvent('MON',todo_this_week,whichday)
).grid(row=1,column=0)

addDay = Button(
    button_frame,
    text='TUE',
    font=('times 14'),
    bg= 'white',
    fg = 'black',
    activebackground = 'black',
    activeforeground = 'green',
    padx=20,
    pady=10,
    command= lambda: displayEvent('TUE',todo_this_week,whichday)
).grid(row=1,column=1)


addDay = Button(
    button_frame,
    text='WED',
    font=('times 14'),
    bg= 'white',
    fg = 'black',
    activebackground = 'black',
    activeforeground = 'green',
    padx=20,
    pady=10,
    command= lambda:  displayEvent('WED',todo_this_week,whichday)
).grid(row=1,column=2)


addDay = Button(
    button_frame,
    text='THU',
    font=('times 14'),
    bg= 'white',
    fg = 'black',
    activebackground = 'black',
    activeforeground = 'green',
    padx=20,
    pady=10,
    command= lambda:  displayEvent('THU',todo_this_week,whichday)
).grid(row=1,column=3)

addDay = Button(
    button_frame,
    text='FRI',
    font=('times 14'),
    bg= 'white',
    fg = 'black',
    activebackground = 'black',
    activeforeground = 'green',
    padx=20,
    pady=10,
    command= lambda:   displayEvent('FRI',todo_this_week,whichday)
).grid(row=1,column=4)


addDay = Button(
    button_frame,
    text='SAT',
    font=('times 14'),
    bg= 'white',
    fg = 'black',
    activebackground = 'black',
    activeforeground = 'green',
    padx=20,
    pady=10,
    command= lambda:  displayEvent('SAT',todo_this_week,whichday)
).grid(row=1,column=5)

addDay = Button(
    button_frame,
    text='SUN',
    font=('times 14'),
    bg= 'white',
    fg = 'black',
    activebackground = 'black',
    activeforeground = 'green',
    padx=20,
    pady=10,
    command= lambda:  displayEvent('SUN',todo_this_week,whichday)
).grid(row=1,column=6)

# --------------------------------------------- #

#Add entries for input event information

#enter event information
entry_frame = Frame(app_win)
entry_frame.pack(pady=20)

#enter event name
event_label = Label(entry_frame,text = "Event:")
event_entry = Entry(
    entry_frame,
    font=('times', 24),
    width = 20
    )
event_label.grid(row=2,column=0,sticky=W)
event_entry.grid(row=2,column=1,sticky=W)

#enter event starting time
from_label = Label(entry_frame,text = "From:")
from_entry = Entry(
    entry_frame,
    font=('times', 24),
    width = 20
    )
from_label.grid(row=3,column=0,sticky=W)
from_entry.grid(row=3,column=1,sticky=W)

#enter event finishing time
to_label = Label(entry_frame,text = "To:")
to_entry = Entry(
    entry_frame,
    font=('times', 24),
    width = 20
    )
to_label.grid(row=4,column=0,sticky=W)
to_entry.grid(row=4,column=1,sticky=W)

# --------------------------------------------- #

#Add button for adding and deleting event

#edit event: add, delete
button2_frame = Frame(app_win)
button2_frame.pack(pady=20)

addEvent_btn = Button(
    button2_frame,
    text='Add Event',
    font=('times 14'),
    bg='gray',
    fg='green',
    padx=20,
    pady=10,
    command=lambda:newEvent(whichday,todo_this_week)
)
addEvent_btn.grid(row=5,column=0,columnspan=3)



delEvent_btn = Button(
    button2_frame,
    text='Delete Event',
    font=('times 14'),
    bg='gray',
    fg='red',
    padx=20,
    pady=10,
    command=lambda:deleteEvent(whichday,todo_this_week)
)
delEvent_btn.grid(row=5,column=6,columnspan=3)

# --------------------------------------------- #

#mainloop
app_win.mainloop()
