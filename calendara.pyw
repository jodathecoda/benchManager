import os
from tkcalendar.calendar_ import Calendar
from tkinter import Tk
import datetime
from configparser import ConfigParser
import datetime
import sys
import tkinter as tk

parameter = sys.argv[1]

cwd = os.getcwd()

global start_day
global start_month
global start_year
global end_day
global end_month
global end_year
global click_on_today_to_clear

start_day = 0
start_month = 0
start_year = 0
end_day = 0
end_month = 0
end_year = 0

click_on_today_to_clear = 0
double_click_selected_day = 0
previous_clicked_day = datetime.date.today()

class MyCalendar(Calendar):

    def _next_month(self):
        Calendar._next_month(self)
        self.event_generate('<<CalendarMonthChanged>>')

    def _prev_month(self):
        Calendar._prev_month(self)
        self.event_generate('<<CalendarMonthChanged>>')

    def _next_year(self):
        Calendar._next_year(self)
        self.event_generate('<<CalendarMonthChanged>>')

    def _prev_year(self):
        Calendar._prev_year(self)
        self.event_generate('<<CalendarMonthChanged>>')

    def get_displayed_month_year(self):
        return self._date.month, self._date.year

# instantiate
config = ConfigParser()

def get_dates():
    global start_day
    global start_month
    global start_year
    global end_day
    global end_month
    global end_year
    global click_on_today_to_clear

    input_file = cwd +"\\benches\\bench" + str(parameter) + "\\bench" + str(parameter) + "_period.ini"

    if os.path.isfile(input_file):
        config.read(input_file)
        start_day   = config.getint('period', 'start_day')
        start_month = config.getint('period', 'start_month')
        start_year  = config.getint('period', 'start_year')
        end_day     = config.getint('period', 'end_day')
        end_month   = config.getint('period', 'end_month')
        end_year    = config.getint('period', 'end_year')      
    else:
        today = datetime.date.today()
        start_day   = today.day
        start_month = today.month
        start_year  = today.year
        end_day   = today.day
        end_month = today.month
        end_year  = today.year



def on_change_month(event):
    # remove previously displayed events
    #cal.calevent_remove('all')
    #day24  = datetime.date(2023, 3, 24)
    #day28 = datetime.date(2023, 3, 28)
    #cal.calevent_create(day27, "", tags="hi")
    #cal.calevent_create(day28, "", tags="hi")
    #cal.tag_config("hi", background="red")
    year, month = cal.get_displayed_month_year()
    # display the current month events 
    # ...
    #print(year, month)

def on_date_click(event):
    global start_day
    global start_month
    global start_year
    global end_day
    global end_month
    global end_year
    global click_on_today_to_clear
  

    get_dates()
    # Get the selected date from the calendar widget
    today = datetime.date.today()
    day = cal.selection_get()

    if day == today:
        click_on_today_to_clear += 1
        if click_on_today_to_clear == 3:
            click_on_today_to_clear = 0
            cal.calevent_remove('all')

root = Tk()
root.title("Calendar")
root.iconbitmap("icons\\Finder.ico")
cal = MyCalendar(root)
cal.config(weekendbackground='green', weekendforeground='white')

get_dates()

start_date = datetime.date(start_year, start_month, start_day)
end_date = datetime.date(end_year, end_month, end_day)

delta = datetime.timedelta(days=1)
date_list = []

today = datetime.date.today()

while start_date <= end_date:
    date_list.append(start_date)
    start_date += delta

print(date_list)

for day in date_list:
    if day != today:
        cal.calevent_create(day, "", tags="hi")

cal.tag_config("hi", background="red")
cal.pack()

cal.bind('<<CalendarMonthChanged>>', on_change_month)
cal.bind("<<CalendarSelected>>", on_date_click)

root.mainloop()