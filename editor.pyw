import os
import tkinter as tk
from configparser import ConfigParser
from os.path import exists
from PIL import Image, ImageTk

global country
country = 'bg'

global photo_bg
global photo_fr
global photo_eu

cwd = os.getcwd()

# Create the GUI window
root = tk.Tk()
root.title("Editor")
root.geometry("200x120")
root.iconbitmap("icons\\Options.ico")

image_bg = Image.open("flags\\bg.png")
photo_bg = ImageTk.PhotoImage(image_bg)

image_fr = Image.open("flags\\fr.png")
photo_fr = ImageTk.PhotoImage(image_fr)

image_eu = Image.open("flags\\eu.png")
photo_eu = ImageTk.PhotoImage(image_eu)

img = image_eu

def change_button_locale():
    global country
    global photo_bg
    global photo_fr
    global photo_eu   

    if country == 'bg':
        locale_button.config(image=photo_bg)
    elif country == 'fr':
        locale_button.config(image=photo_fr)
    else:
        locale_button.config(image=photo_eu)

def country_change():
    global country

    if country == 'bg':
        country = 'fr'
    elif country == 'fr':
        country = 'eu'
    else:
        country = 'bg'
    change_button_locale()


# Create a function to submit the data
def submit_data():
    config = ConfigParser()
    print("submitted")
    # save to a file
    folder_name = cwd +"\\benches\\bench" + str(id_entry.get())
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    bench_file = folder_name +"\\bench" + str(id_entry.get()) + ".ini"
    f = open(bench_file, "w+")
    #f.write("Now the file has more content!")
    f.close()
    config.read(bench_file)

    # add a new section and some values
    config.add_section('bench')
    #config.set('bench', 'id', str(id_entry.get()))
    config.set('bench', 'pc', str(pc_entry.get()))
    config.set('bench', 'oem', str(oem_entry.get()))
    #config.set('bench', 'status', str(status_entry.get()))
    config.set('bench', 'duts', str(duts_entry.get()))
    #config.set('bench', 'can', str(can_entry.get()))
    #config.set('bench', 'dmm', str(dmm_entry.get()))
    #config.set('bench', 'psu', str(psu_entry.get()))
    #config.set('bench', 'loc', str(loc_entry.get()))

    #config.add_section('engineers')
    #config.set('engineers', 'tde', str(tde_entry.get()))
    #config.set('engineers', 'ev', str(ev_entry.get()))
    #config.set('engineers', 'pdtl', str(pdtl_entry.get()))

    config.add_section('notes')
    config.set('notes', 'note', text_field.get("1.0", tk.END))

    # save to a file
    with open(bench_file, 'w') as configfile:
        config.write(configfile)

    
if country == 'bg':
    img = image_bg
elif country == 'fr':
    img = image_fr
else:
    img = image_eu

pc_label = tk.Label(root, text="pc:")
pc_label.grid(row=0, column=0)
pc_entry = tk.Entry(root)
#id_entry.insert(0,"bench number")
pc_entry.grid(row=0, column=1)

oem_label = tk.Label(root, text="project:")
oem_label.grid(row=1, column=0)
oem_entry = tk.Entry(root)
#oem_entry.insert(0, "oem")
oem_entry.grid(row=1, column=1)


duts_label = tk.Label(root, text="duts:")
duts_label.grid(row=2, column=0)
duts_entry = tk.Entry(root)
duts_entry.grid(row=2, column=1)


# create a Text widget with a height of 4 and width of 50
text_label = tk.Label(root, text="notes:")
text_label.grid(row=3, column=0)
notes_entry = tk.Entry(root)
notes_entry.grid(row=3, column=1)

locale_button = tk.Button(root,image=photo_eu, command=country_change)
locale_button.grid(row=4, column=0)

submit_button = tk.Button(root, text="SUBMIT", command=submit_data)
submit_button.grid(row=4, column=1)


root.mainloop()
