###
#A weekly todo App (using tkinter, button, entry, listbox) with functions:
#add, delete events for selected weekday
#listbox is used to show events of selected day
###

from tkinter import *
from tkinter import messagebox
from tktimepicker import SpinTimePickerModern, constants # pip install tktimepicker

print('Launch App ====== ')



# --------- event functions ---------- #

def displayEvent(text, todo_this_week, day_dict, day_button):
    """
    display events of selected day
    INPUT:
    text: indicate which day of the week
    todo_this_week: the dictionary contains every weekday's todo list
    day_dict: a one-item list to keep track of which weekday, day_dict will be updated to the selected day (text) once the button of this day is clicked. it will be used later for editing events
    """

    # determine which day (given by text) to work on, pull out this day's todo list

    # CH there's really no way text can be anything other than MON, TUE, etc. so
    # you don't need to do all these checks to 
    event_list = todo_this_week[text]
    '''
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
    '''

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
    
    #update day_dict to the selected day, which is to be used for add and remove event
    day_dict["current"] = text

    # set the last active button to inactive
    last_day = day_dict["last"] 
    day_button[last_day].configure(bg="white")

    # Change color to show which day is currently active
    curr_day = day_dict["current"]
    day_button[curr_day].configure(bg="yellow")

    # update last day so the now current day will be set inactive
    # next time
    day_dict["last"] = curr_day 
   
#add event to select weekday
def newEvent(day_dict,todo_this_week):
    #read event from entries
    event = event_entry.get()

    # need to composite hours and minutes from time picker
    # you could improve this be always having 2 digit minutes (i.e. 6:00 instead of 6:0)
    fromtime = str(from_entry.hours()) + ":" + str(from_entry.minutes())
    totime = str(to_entry.hours()) + ":" + str(to_entry.minutes())
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
        
        # I don't think there's a need to reset the times
        #from_entry.delete(0, "end")
        #to_entry.delete(0, "end")

        #update todo list for this day in todo_this_week (append to end)
        thisday = day_dict["current"]
        ev = {"name":event, "from": fromtime, "to": totime, "done":isdone}
        todo_this_week[thisday].append(ev)
    else:
        messagebox.showwarning("warning", "Please enter some event.")
     

#remove event from select weekday
def deleteEvent(day_dict,todo_this_week):
    #delete event from listbox and from todo_this_week
    thisday = day_dict["current"]
    for item in lb.curselection():
        lb.delete(item)

        #todo_this_week[thisday].pop(item)
        del todo_this_week[thisday][item] # I think this better shows that the item go deleted (del)
  

# --------------------------------------------- #
# initialize dictionary for todo list of the week
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

# As we need to keep track of 2 tyes of days, I'm using a dict here instead of a list
day_dict = {"current":"MON", "last":"MON"} 

# storing the buttons in a dict here so we can change their appearance later 
day_button = {}

day_button["MON"] = Button(
    button_frame,
    text='MON',
    font=('times 14'),
    bg= 'white',
    fg = 'black',
    activebackground = 'black',
    activeforeground = 'green',
    padx=20,
    pady=10,
    command= lambda: displayEvent('MON',todo_this_week,day_dict, day_button)
)
day_button["MON"].grid(row=1,column=0)

day_button["TUE"] = Button(
    button_frame,
    text='TUE',
    font=('times 14'),
    bg= 'white',
    fg = 'black',
    activebackground = 'black',
    activeforeground = 'green',
    padx=20,
    pady=10,
    command= lambda: displayEvent('TUE',todo_this_week,day_dict, day_button)
)
day_button["TUE"].grid(row=1,column=1)


day_button["WED"] = Button(
    button_frame,
    text='WED',
    font=('times 14'),
    bg= 'white',
    fg = 'black',
    activebackground = 'black',
    activeforeground = 'green',
    padx=20,
    pady=10,
    command= lambda:  displayEvent('WED',todo_this_week,day_dict, day_button)
)
day_button["WED"].grid(row=1,column=2)


day_button["THU"] = Button(
    button_frame,
    text='THU',
    font=('times 14'),
    bg= 'white',
    fg = 'black',
    activebackground = 'black',
    activeforeground = 'green',
    padx=20,
    pady=10,
    command= lambda:  displayEvent('THU',todo_this_week,day_dict, day_button)
)
day_button["THU"].grid(row=1,column=3)

day_button["FRI"] = Button(
    button_frame,
    text='FRI',
    font=('times 14'),
    bg= 'white',
    fg = 'black',
    activebackground = 'black',
    activeforeground = 'green',
    padx=20,
    pady=10,
    command= lambda:   displayEvent('FRI',todo_this_week,day_dict, day_button)
)
day_button["FRI"].grid(row=1,column=4)


day_button["SAT"] = Button(
    button_frame,
    text='SAT',
    font=('times 14'),
    bg= 'white',
    fg = 'black',
    activebackground = 'black',
    activeforeground = 'green',
    padx=20,
    pady=10,
    command= lambda:  displayEvent('SAT',todo_this_week,day_dict, day_button)
)
day_button["SAT"].grid(row=1,column=5)

day_button["SUN"] = Button(
    button_frame,
    text='SUN',
    font=('times 14'),
    bg= 'white',
    fg = 'black',
    activebackground = 'black',
    activeforeground = 'green',
    padx=20,
    pady=10,
    command= lambda:  displayEvent('SUN',todo_this_week,day_dict, day_button)
)
day_button["SUN"].grid(row=1,column=6)

# set current day as active
day = day_dict["current"]
day_button[day].configure(bg="yellow")

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
# https://github.com/PaulleDemon/tkTimePicker/blob/master/examples/SpinTimePickerExample.py
from_entry = SpinTimePickerModern(entry_frame)
from_entry.set24Hrs(12)  # initial time to show
from_entry.setMins(0) 
from_entry.addAll(constants.HOURS24)  # adds hours clock, minutes and period
from_entry.configureAll(height=1, width=3,
                            font=("Times", 24),
                            #hovercolor="red", 
                            #clickedbg="white", 
                            clickedcolor="black")
#from_entry.configure_separator(bg="#404040", fg="#ffffff")
'''
from_entry = Entry(
    entry_frame,
    font=('times', 24),
    width = 20
    )
''' 


from_label.grid(row=3,column=0, columnspan=3, sticky=W)
from_entry.grid(row=3,column=1,sticky=W)

#enter event finishing time
to_label = Label(entry_frame,text = "To:")
to_entry = SpinTimePickerModern(entry_frame)  
to_entry.addAll(constants.HOURS24)  # adds hours clock, minutes and period
to_entry.set24Hrs(14)  # initial time to show
to_entry.setMins(0) 
to_entry.configureAll(height=1, width=3,
                            font=("Times", 24),
                            #hovercolor="red", 
                            #clickedbg="white", 
                            clickedcolor="black")
#to_entry.configure_separator(bg="#404040", fg="#ffffff")
'''
to_entry = Entry(
    entry_frame,
    font=('times', 24),
    width = 20
    )
'''
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
    command=lambda:newEvent(day_dict,todo_this_week)
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
    command=lambda:deleteEvent(day_dict,todo_this_week)
)
delEvent_btn.grid(row=5,column=6,columnspan=3)

# --------------------------------------------- #

#mainloop
app_win.mainloop()
