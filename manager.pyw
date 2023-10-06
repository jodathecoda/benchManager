import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
from os.path import exists
from configparser import ConfigParser
import subprocess
from tkinter import filedialog
import shutil
import configparser

cwd = os.getcwd()

def submit_data(param, pc, oem, duts, notes, test, status, window):
    config = ConfigParser()  

    folder_name = cwd + "\\benches\\bench" + str(param)
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    bench_file = folder_name +"\\bench" + str(param) + ".ini"
    f = open(bench_file, "w+")
    #f.write("Now the file has more content!")
    f.close()
    config.read(bench_file)

    config.add_section('bench')
    config.set('bench', 'pc', str(pc))
    config.set('bench', 'oem', str(oem))
    config.set('bench', 'duts', str(duts))
    config.set('bench', 'test', str(test))
    config.set('bench', 'status', str(status))

    config.add_section('notes')
    config.set('notes', 'note', str(notes))

    # save to a file
    with open(bench_file, 'w') as configfile:
        config.write(configfile)
    window.destroy()

def button_edit_handler(param):
        print("edit:", param)
        config = ConfigParser()

        #pop up edit window
        editor = tk.Tk()
        editor.title("Editor")
        #editor.geometry("200x120+800+300")
        editor.geometry("210x150+800+300")
        editor.iconbitmap("icons\\Options.ico")

        #check if file exists to enter prompt text
        #clear prompts
        pc_prompt = ""
        oem_prompt = ""
        duts_prompt = ""
        notes_prompt = ""
        testON_prompt = ""
        benchOK_prompt = ""

        filename = "benches\\bench" + str(param) + "\\bench" + str(param) + ".ini"

        if os.path.isfile(filename):
            #print(filename + " exists")
            config.read(filename)
            pc_prompt = config.get('bench', 'pc')
            oem_prompt = config.get('bench', 'oem')
            duts_prompt = config.get('bench', 'duts')
            notes_prompt = config.get('notes', 'note')
            testON_prompt = config.get('bench', 'test')
            benchOK_prompt = config.get('bench', 'status')
        else:
            pass
            #print(filename + " does not exists")

        pc_label = tk.Label(editor, text="pc:")
        pc_label.grid(row=0, column=0)
        pc_entry = tk.Entry(editor)
        pc_entry.insert(0, pc_prompt)
        pc_entry.grid(row=0, column=1)

        oem_label = tk.Label(editor, text="project:")
        oem_label.grid(row=1, column=0)
        oem_entry = tk.Entry(editor)
        oem_entry.insert(0, oem_prompt)
        oem_entry.grid(row=1, column=1)

        duts_label = tk.Label(editor, text="duts:")
        duts_label.grid(row=2, column=0)
        duts_entry = tk.Entry(editor)
        duts_entry.insert(0, duts_prompt)
        duts_entry.grid(row=2, column=1)

        test_label = tk.Label(editor, text="testing:")
        test_label.grid(row=3, column=0)
        test_entry = tk.Entry(editor)
        test_entry.insert(0, testON_prompt)
        test_entry.grid(row=3, column=1)

        bench_label = tk.Label(editor, text="status:")
        bench_label.grid(row=4, column=0)
        bench_entry = tk.Entry(editor)
        bench_entry.insert(0, benchOK_prompt)
        bench_entry.grid(row=4, column=1)

        # create a Text widget with a height of 4 and width of 50
        text_label = tk.Label(editor, text="DMM:")
        text_label.grid(row=5, column=0)
        notes_entry = tk.Entry(editor)
        notes_entry.insert(0, notes_prompt)
        notes_entry.grid(row=5, column=1)

        submit_button = tk.Button(editor, text="SUBMIT", command=lambda: submit_data(param, pc_entry.get(), oem_entry.get(), duts_entry.get(), notes_entry.get(), test_entry.get(), bench_entry.get(), editor))

        submit_button.grid(row=6, column=1)


        editor.mainloop()

def button_view_handler(param):
    config = ConfigParser()
    filename = "benches\\bench" + str(param) + "\\bench" + str(param) + ".ini"
    if os.path.isfile(filename):
        config.read(filename)
        pc = config.get('bench', 'pc')
        oem = config.get('bench', 'oem')
        duts = config.get('bench', 'duts')
        testON = config.get('bench', 'test')
        benchStatus = config.get('bench', 'status')
        notes = config.get('notes', 'note')
        viewer = tk.Tk()
        viewer.title("bench" + str(param))
        viewer.geometry("300x150+800+300")
        viewer.iconbitmap("icons\\Find.ico")

        pc_label = tk.Label(viewer, text="pc: " + pc, anchor='w', justify='left')
        pc_label.grid(row=0, column=0, sticky='w')

        oem_label = tk.Label(viewer, text="oem: " + oem, anchor='w', justify='left')
        oem_label.grid(row=1, column=0, sticky='w')

        duts_label = tk.Label(viewer, text="duts: " + duts, anchor='w', justify='left')
        duts_label.grid(row=2, column=0, sticky='w')

        test_label = tk.Label(viewer, text="Test ON: " + testON, anchor='w', justify='left')
        test_label.grid(row=3, column=0, sticky='w')

        benchStatus_label = tk.Label(viewer, text="Status: " + benchStatus, anchor='w', justify='left')
        benchStatus_label.grid(row=4, column=0, sticky='w')

        notes_label = tk.Label(viewer, text=" ------ notes ------", anchor='w', justify='left')
        notes_label.grid(row=5, column=0, sticky='w')

        actualnotes_label = tk.Label(viewer, text=notes, anchor='w', justify='left', wraplength=280)
        actualnotes_label.grid(row=6, column=0, sticky='w')

        viewer.mainloop()

def button_calendar_handler(param):
            print("calendar:", param)
            creationflags = subprocess.CREATE_NO_WINDOW
            subprocess.Popen(["python", "selector.pyw", param], creationflags=creationflags)

def button_viewcalendar_handler(param):
            print("viewcalendar:", param)
            creationflags = subprocess.CREATE_NO_WINDOW
            subprocess.Popen(["python", "calendara.pyw", param], creationflags=creationflags)

def button_folder_handler(param):
    print("file:", param)
    folder_path = os.path.join(cwd, "benches", f"bench{param}", "configs")

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Open a file dialog to select a file
    selected_file = filedialog.askopenfilename(initialdir=folder_path, title="Select File")

    if selected_file:
        print(f"Selected file path: {selected_file}")
        os.startfile(selected_file)
    else:
        pass

def button_pics_handler(param):
            print("pics:", param)
            folder_path = os.path.join(cwd, "benches", f"bench{param}", "pics")

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Open a file dialog to select a file
            selected_file = filedialog.askopenfilename(initialdir=folder_path, title="Select File")

            if selected_file:
                print(f"Selected file path: {selected_file}")
                os.startfile(selected_file)
            else:
                pass

def yess(param,window):
    folder_name = cwd + "\\benches\\bench" + str(param)
    # Delete the folder with the given parameter
    folder_path = os.path.join(cwd, "benches", f"bench{param}")
    shutil.rmtree(folder_path)
    window.destroy()

def noo(param, window):
    window.destroy()

def button_delete_handler(param):
            print("delete:", param)
            pop = tk.Tk()
            pop.title("Delete")
            pop.iconbitmap("icons\\Delete.ico")
            pop.geometry("100x50+800+300")
            pop_label = tk.Label(pop, text="DELETE BENCH ?", anchor='w', justify='left')
            pop_label.grid(row=0, column=0, sticky='w', columnspan=2) # Set columnspan=2 here

            yes_button = tk.Button(pop, text="YES", command=lambda: yess(param,pop))
            yes_button.grid(row=1, column=0)
            no_button = tk.Button(pop, text="NO", command=lambda: noo(param, pop))
            no_button.grid(row=1, column=1)
            pop.mainloop()

def dumb_handler(param):
    pass

def button_remotepc_handler(param):
    print("remotepc:", param)
    config = ConfigParser()
    filename = "benches\\bench" + str(param) + "\\bench" + str(param) + ".ini"
    if os.path.isfile(filename):
        config.read(filename)
        pc = config.get('bench', 'pc')
        subprocess.Popen(["mstsc", "/v:" + pc])
    else:
        pass

def get_fg_color(oem_str):
    #print("fg: "+ oem_str)
    colorr = 'blue'
    if 'gmc' in oem_str or 'GMC' in oem_str or 'Porsche' in oem_str or 'PORSCHE' in oem_str or 'Porsche'in oem_str:
        colorr = 'red'
    elif 'VOLVO' in oem_str or 'volvo' in oem_str or 'Volvo' in oem_str or 'PSA' in oem_str or 'psa' in oem_str:
        colorr = 'white'
    elif 'Daimler' in oem_str or 'daimler' in oem_str or 'Mercedes' in oem_str or 'mercedes' in oem_str or 'mfa' in oem_str or 'mra' in oem_str or 'MRA' in oem_str or 'mopf' in oem_str or 'br' in oem_str or 'BR' in oem_str or 'opel' in oem_str or 'Opel' in oem_str or 'OPEL' in oem_str:
        colorr = 'white'
    elif 'RSA' in oem_str or 'rsa' in oem_str:
        colorr = 'black'
    elif 'BMW' in oem_str or 'bmw' in oem_str:
        colorr = 'blue'
    elif 'AUDI' in oem_str or 'audi'in oem_str or 'Audi' in oem_str:
        colorr = 'black'
    elif 'Maseratti' in oem_str or 'maseratti' in oem_str or 'MASERATTI' in oem_str:
        colorr = 'red'
    elif 'evo' in oem_str or 'Evo' in oem_str or 'EVO' in oem_str:
         colorr = 'white'
    elif 'GSR' in oem_str or 'gsr' in oem_str or 'GLSR' in oem_str or 'glsr' in oem_str:
        colorr = 'blue'
    else:
        colorr = 'black'
    #print("fg: " + colorr)
    return colorr

def get_bg_color(oem_str):
    #print("bg: "+ oem_str)
    colorr = 'yellow'
    if 'br206' in oem_str or 'BR206' in oem_str:
        colorr = 'purple'
    elif 'gmc' in oem_str or 'GMC' in oem_str:
        colorr = 'black'
    elif 'Porsche' in oem_str or 'PORSCHE' in oem_str or 'Porsche' in oem_str:
        colorr = 'yellow'
    elif 'VOLVO' in oem_str or 'volvo' in oem_str or 'Volvo' in oem_str or 'PSA' in oem_str or 'psa' in oem_str:
        colorr = 'blue'
    elif 'Daimler' in oem_str or 'daimler' in oem_str or 'Mercedes' in oem_str or 'mercedes' in oem_str or 'mfa' in oem_str or 'mra' in oem_str or 'MRA' in oem_str or 'mopf' in oem_str or 'br' in oem_str or 'BR' in oem_str or 'opel' in oem_str or 'Opel' in oem_str or 'OPEL' in oem_str:
        colorr = 'black'
    elif 'RSA' in oem_str or 'rsa' in oem_str:
        colorr = 'yellow'
    elif 'BMW' in oem_str or 'bmw' in oem_str:
        colorr = 'lightblue'
    elif 'AUDI' in oem_str or 'audi' in oem_str or 'Audi' in oem_str:
        colorr = 'red'
    elif 'Maseratti' in oem_str or 'maseratti' in oem_str or 'MASERATTI' in oem_str:
        colorr = 'blue'
    elif 'evo' in oem_str or 'Evo' in oem_str or 'EVO' in oem_str or 'GSR' in oem_str or 'gsr' in oem_str or 'GLSR' in oem_str or 'glsr' in oem_str:
         colorr = 'green'
    elif 'mopf' in oem_str or 'MOPF' in oem_str or 'Mopf' in oem_str:
        colorr = 'brown'
    else:
        colorr = 'orange'
    #print("bg: " + colorr)
    return colorr


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Benches")
        self.geometry("450x360")
        self.iconbitmap("icons\\Home.ico")

        self.image_edit = Image.open("pics\\edit.png")
        self.photo_edit = ImageTk.PhotoImage(self.image_edit)

        self.image_calendar = Image.open("pics\\calendar.png")
        self.photo_calendar = ImageTk.PhotoImage(self.image_calendar)

        self.image_view = Image.open("pics\\view.png")
        self.photo_view = ImageTk.PhotoImage(self.image_view)

        self.image_folder = Image.open("pics\\folder.png")
        self.photo_folder = ImageTk.PhotoImage(self.image_folder)

        self.image_pics = Image.open("pics\\pics.png")
        self.photo_pics = ImageTk.PhotoImage(self.image_pics)

        self.image_calendarview = Image.open("pics\\calendarview.png")
        self.photo_calendarview = ImageTk.PhotoImage(self.image_calendarview)

        self.image_remotepc = Image.open("pics\\remotepc.png")
        self.photo_remotepc = ImageTk.PhotoImage(self.image_remotepc)

        self.image_delete = Image.open("pics\\delete.png")
        self.photo_delete = ImageTk.PhotoImage(self.image_delete)

        self.image_bench_ready = Image.open("pics\\Ok.png")
        self.photo_bench_ready = ImageTk.PhotoImage(self.image_bench_ready)

        self.image_bench_not_ready = Image.open("pics\\Stop.png")
        self.photo_bench_not_ready = ImageTk.PhotoImage(self.image_bench_not_ready)

        self.image_bench_status_unknown = Image.open("pics\\Help.png")
        self.photo_bench_status_unknown = ImageTk.PhotoImage(self.image_bench_status_unknown)

        self.image_test_stopped = Image.open("pics\\Unlock.png")
        self.photo_test_stopped = ImageTk.PhotoImage(self.image_test_stopped)

        self.image_test_running = Image.open("pics\\Lock.png")
        self.photo_test_running = ImageTk.PhotoImage(self.image_test_running)

        self.image_delete = Image.open("pics\\delete.png")
        self.photo_delete = ImageTk.PhotoImage(self.image_delete)

        # Create the notebook widget to hold the tabs
        self.notebook = ttk.Notebook(self, style="Custom.TNotebook")
        self.notebook.pack(fill="both", expand=True)

        # Create a custom style for the notebook tabs
        self.style = ttk.Style()
        self.style.theme_create("CustomTheme", parent="alt", settings={
            "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0]}},
            "TNotebook.Tab": {
                "configure": {"padding": [10, 5], "background": "#f0f0f0"},
                "map": {"background": [("selected", "orange"), ("active", "yellow")],
                        "foreground": [("selected", "#fff"), ("active", "#000")],
                        "expand": [("selected", [1, 1, 1, 0])]}}})
        self.style.theme_use("CustomTheme")

        # Create 10 tabs and add them to the notebook
        for i in range(1, 11):
            tab = tk.Frame(self.notebook)
            #self.notebook.add(tab, text=f"{i} - {i+10}")
            if i == 10:
                self.notebook.add(tab, text=f"OTHER")
            else:
                self.notebook.add(tab, text=f"{i*10}")

            # Add 10 buttons to each tab
            for j in range(1, 11):

                oem_label = ""
                bench_ready = 0 # 0 = unknown, 1 = OK, 2 = Not Ready
                test_running = 0 # 0 = not running ; 1 = test running
                config = ConfigParser()

                colourr = "grey"
                back_colourr = "white"

                file_path = "benches\\" + f"bench{i*10+j-10}" + "\\" + f"bench{i*10+j-10}" + ".ini"
                if os.path.exists(file_path):
                    config.read(file_path)
                    oem_label = config.get('bench', 'oem')
                    #colourr = "blue"
                    print("oem label: ------------------------> " + oem_label)
                    colourr = get_fg_color(oem_label)
                    back_colourr = get_bg_color(oem_label)
                    try:
                        bench_ready = int(config.get('bench', 'status'))
                    except:
                        bench_ready = 0

                    try:
                        test_running = int(config.get('bench', 'test'))
                    except:
                        test_running = 0
                else:
                    colourr = "grey"
                    back_colourr = "white"
                #button_text = f"bench{i*10+j-10}"
                button_text = f"bench{i*10+j-10}"
                if button_text == "bench91":
                    button_text = "TDE 1"
                if button_text == "bench92":
                    button_text = "TDE 2"
                if button_text == "bench93":
                    button_text = "TDE 3"
                if button_text == "bench94":
                    button_text = "ELEC 1"
                if button_text == "bench95":
                    button_text = "ELEC 2"
                if button_text == "bench96":
                    button_text = "ELEC 3"
                if button_text == "bench97":
                    button_text = "EMC 1"
                if button_text == "bench98":
                    button_text = "EMC 2"
                if button_text == "bench99":
                    button_text = "EMC 3"
                if button_text == "bench100":
                    button_text = "OPTICS"
                button = tk.Button(tab, text=button_text, fg =colourr, bg = back_colourr,
                                   command=lambda text=button_text: self.print_name(text))
                button.grid(row=j-1, column=0)
    

                #button_edit_text = f"edit {i*10+j-10}"
                button_text = f"{i*10+j-10}"
                button_edit = tk.Button(tab, image=self.photo_edit, command=lambda text=button_text: button_edit_handler(text))
                button_edit.grid(row=j-1, column=1)
                # create the button with the image and the command

                button_view = tk.Button(tab, image=self.photo_view, command=lambda text=button_text: button_view_handler(text))
                button_view.grid(row=j-1, column=2)

                #button_calendar_text = f"calendar {i*10+j-10}"
                button_calendar = tk.Button(tab, image=self.photo_calendar, command=lambda text=button_text: button_calendar_handler(text))
                button_calendar.grid(row=j-1, column=3)
                # create the button with the image and the command

                button_calendarview = tk.Button(tab, image=self.photo_calendarview, command=lambda text=button_text: button_viewcalendar_handler(text))
                button_calendarview.grid(row=j-1, column=4)

                button_folder = tk.Button(tab, image=self.photo_folder, command=lambda text=button_text: button_folder_handler(text))
                button_folder.grid(row=j-1, column=5)

                button_pics = tk.Button(tab, image=self.photo_pics, command=lambda text=button_text: button_pics_handler(text))
                button_pics.grid(row=j-1, column=6)

                
                # add test running 7
                if test_running == 0:
                    #bench is free, test not running
                    button_test_running = tk.Button(tab, image=self.photo_test_stopped, command=lambda text=button_text: dumb_handler(text))
                    button_test_running.grid(row=j-1, column=7)
                elif test_running == 1:
                    #bench is busy, test is running
                    button_test_running = tk.Button(tab, image=self.photo_test_running, command=lambda text=button_text: dumb_handler(text))
                    button_test_running.grid(row=j-1, column=7)
                else:
                    #bench is free, test not running
                    button_test_running = tk.Button(tab, image=self.photo_test_stopped, command=lambda text=button_text: dumb_handler(text))
                    button_test_running.grid(row=j-1, column=7)

                # add bench status 8
                if bench_ready == 0:
                    #bench is not ready
                    button_test_ready = tk.Button(tab, image=self.photo_bench_not_ready, command=lambda text=button_text: dumb_handler(text))
                    button_test_ready.grid(row=j-1, column=8)
                elif bench_ready == 1:
                    #bench is status unknown
                    button_test_ready = tk.Button(tab, image=self.photo_bench_status_unknown, command=lambda text=button_text: dumb_handler(text))
                    button_test_ready.grid(row=j-1, column=8)
                elif bench_ready == 2:
                    #bench is ready
                    button_test_ready = tk.Button(tab, image=self.photo_bench_ready, command=lambda text=button_text: dumb_handler(text))
                    button_test_ready.grid(row=j-1, column=8)
                else:
                    #bench is status unknown
                    #bench is status unknown
                    button_test_ready = tk.Button(tab, image=self.photo_bench_status_unknown, command=lambda text=button_text: dumb_handler(text))
                    button_test_ready.grid(row=j-1, column=8)

                button_remote = tk.Button(tab, image=self.photo_remotepc, command=lambda text=button_text: button_remotepc_handler(text))
                button_remote.grid(row=j-1, column=9)

                button_delete = tk.Button(tab, image=self.photo_delete, command=lambda text=button_text: button_delete_handler(text))
                button_delete.grid(row=j-1, column=10)

                oem_label = tk.Label(tab, text=oem_label)
                oem_label.grid(row=j-1, column=11)

    def print_name(self, name):
        print(name)

if __name__ == "__main__":
    app = App()
    app.mainloop()
