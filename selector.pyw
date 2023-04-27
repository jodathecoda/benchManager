import os
import sys
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
import datetime
from configparser import ConfigParser

parameter = sys.argv[1]

cwd = os.getcwd()

class CalendarSelector:
    def __init__(self, master):
        self.master = master
        self.master.title("Calendar Selector")
        self.start_date = None
        self.end_date = None

        self.start_label = ttk.Label(self.master, text="Select start date:")
        self.start_label.pack(pady=5)

        self.start_cal = Calendar(self.master, selectmode="day", date_pattern="yyyy-mm-dd", 
                                  cursor="hand1", year=datetime.date.today().year, 
                                  month=datetime.date.today().month, day=datetime.date.today().day)
        self.start_cal.pack(padx=10, pady=5)

        self.end_label = ttk.Label(self.master, text="Select end date:")
        self.end_label.pack(pady=5)

        self.end_cal = Calendar(self.master, selectmode="day", date_pattern="yyyy-mm-dd", 
                                cursor="hand1", year=datetime.date.today().year, 
                                month=datetime.date.today().month, day=datetime.date.today().day)
        self.end_cal.pack(padx=10, pady=5)

        self.save_button = ttk.Button(self.master, text="Save Dates", command=self.save_dates)
        self.save_button.pack(pady=10)

    def save_dates(self):
        #self.start_date = self.start_cal.get_date()
        self.start_date = datetime.datetime.strptime(self.start_cal.get_date(), '%Y-%m-%d').date()
        #self.end_date = self.end_cal.get_date()
        self.end_date = datetime.datetime.strptime(self.end_cal.get_date(), '%Y-%m-%d').date()
        if self.start_date is None or self.end_date is None:
            return
        # Write the dates to an INI file
        config = ConfigParser()
        folder_name = cwd +"\\benches\\bench" + str(parameter)
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        bench_file = folder_name + "\\bench" + str(parameter) + "_period.ini"
        f = open(bench_file, "w+")
        #f.write("Now the file has more content!")
        f.close()

        config.add_section('period')
        config.set('period', 'start_day', str(self.start_date.day))
        config.set('period', 'start_month', str(self.start_date.month))
        config.set('period', 'start_year', str(self.start_date.year))
        config.set('period', 'end_day', str(self.end_date.day))
        config.set('period', 'end_month', str(self.end_date.month))
        config.set('period', 'end_year', str(self.end_date.year))

        # save to a file
        with open(bench_file, 'w') as configfile:
            config.write(configfile)
        quit()    

root = Tk()
root.iconbitmap("icons\\Paste.ico")
app = CalendarSelector(root)
root.mainloop()
