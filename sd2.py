import tkinter as tk
from tkinter import *
import datetime
from tkinter.font import BOLD
from tkinter import font as tkfont
from turtle import bgcolor


class ClockApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Clock App")

        # Create new frame on top of the image
        self.main_frame = tk.Frame(self.master)
        self.main_frame.place(anchor=CENTER,relx = .5,rely=.5)
        self.main_frame.config(bg='black')
        # Initialize time
        self.current_time = datetime.datetime.now()
        # Initialize date
        self.current_date = datetime.datetime.now().date()

        self.width = root.winfo_screenwidth()
        self.height = root.winfo_screenheight()

        self.main_label = tk.Label(self.main_frame, text=self.current_time.strftime("%H:%M:%S"), font=("Arial", int(self.width/20),BOLD),bg='black',fg='white')
        self.main_label.pack(expand= True,fill=BOTH,pady=10)
        self.date_label = tk.Label(self.main_frame, text=self.current_date.strftime("%b %d, %Y"), font=("Arial", int(self.height/20),BOLD),bg='black',fg='white')
        self.date_label.pack(expand= True,fill=BOTH,pady=10)

        self.hour_entry2 = 0
        self.minute_entry2 = 0
        self.second_entry2 = 0

        self.start_timer()

    def change_time(self,x):
        # Create new window for changing time
        self.change_window = tk.Toplevel(self.master)
        self.change_window.title("Change Time")

        # Create labels and entries for hour, minute, and second
        tk.Label(self.change_window, text="Hour (0-23):").grid(row=0, column=0, padx=20, pady=10)
        self.hour_entry = tk.Entry(self.change_window)

        self.hour_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.change_window, text="Minute (0-59):").grid(row=1, column=0, padx=20, pady=10)
        self.minute_entry = tk.Entry(self.change_window)
        self.minute_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.change_window, text="Second (0-59):").grid(row=2, column=0, padx=20, pady=10)
        self.second_entry = tk.Entry(self.change_window)
        self.second_entry.grid(row=2, column=1, padx=10, pady=10)

        # Create button to update time
        tk.Button(self.change_window, text="Update Time", command=self.update_time).grid(row=3, column=1, padx=10, pady=10)



    def reset_time(self,x):
        hour = int(self.hour_entry2)
        minute = int(self.minute_entry2)
        second = int(self.second_entry2)

        # Replace current time with new time
        self.current_time = datetime.datetime.now().replace(hour=hour, minute=minute, second=second)

    def update_time(self):
        # Get new time from entries
        hour = int(self.hour_entry.get())
        minute = int(self.minute_entry.get())
        second = int(self.second_entry.get())
        self.hour_entry2 =hour
        self.minute_entry2 = minute
        self.second_entry2 = second
        # Replace current time with new time
        self.current_time = datetime.datetime.now().replace(hour=hour, minute=minute, second=second)

        # Close change time window
        self.change_window.destroy()


    def show_menu(self, x):
        # Create new window for menu options
        self.menu_window = tk.Toplevel(self.master)
        self.menu_window.title("Menu")

        # Create label for menu options
        tk.Label(self.menu_window, text="Menu Options:", font=("Arial", int(self.width/30), BOLD)).grid(row=0, column=0, padx=20, pady=10)

        # Create button to toggle fullscreen
        tk.Button(self.menu_window, text="Toggle Fullscreen", command=self.toggle_fullscreen).grid(row=1, column=0, padx=10, pady=10)

         # Create font size drop-down list
        tk.Label(self.menu_window, text="Font Size:").grid(row=2, column=0, padx=20, pady=10)
        size_var = tk.StringVar()
        size_var.set(str(int(self.width/20)))
        size_dropdown = tk.OptionMenu(self.menu_window, size_var, *["32", "64", "128", "256", "512"])
        size_dropdown.grid(row=2, column=0, padx=10, pady=10)

     # Create font dropdown list
        tk.Label(self.menu_window, text="Font:").grid(row=3, column=0, padx=20, pady=10)
        font_var = tk.StringVar()
        font_var.set("Arial")
        font_dropdown = tk.OptionMenu(self.menu_window, font_var, *tk.font.families())
        font_dropdown.grid(row=4, column=0, padx=10, pady=10)

        # Create button to change font size and font
        tk.Button(self.menu_window, text="Change Font", command=lambda: self.change_font(font_var.get(), int(size_var.get()))).grid(row=4, column=1, padx=10, pady=10)

        # Create button to change font size
        tk.Button(self.menu_window, text="Change Font Size", command=lambda: self.change_font_size(int(size_var.get()))).grid(row=2, column=1, padx=10, pady=10)

    def change_font(self, font_name, font_size):
        # Change the font and font size of the main label and date label
        font = tkfont.Font(family=font_name, size=font_size, weight=tkfont.BOLD)
        self.main_label.config(font=font)
        self.date_label.config(font=font)

    def change_font_size(self, size):
        self.main_label.config(font=("Arial", size, BOLD))

    def toggle_fullscreen(self):
        # Toggle fullscreen mode
        self.master.attributes('-fullscreen', not self.master.attributes('-fullscreen'))

    def reset_to_current_time(self, x):
        self.current_time = datetime.datetime.now()

    def start_timer(self):
        self.increment_time()
        self.master.after(1000, self.start_timer)

    def increment_time(self):
        self.current_time += datetime.timedelta(seconds=1)
        self.main_label.config(text=self.current_time.strftime("%H:%M:%S"))
    def close(self,x):
        root.quit()

root = tk.Tk()

clock_app = ClockApp(root)
root.config(bg='black')
root.geometry("1500x1000")
#KEYBINDS

#Reset time
root.bind('<r>', clock_app.reset_time)
#Change time
root.bind('<c>',clock_app.change_time)
#Close Application
root.bind('<q>',clock_app.close)
# Reset to current time
root.bind('<t>', clock_app.reset_to_current_time)
# Show menu
root.bind('<m>', clock_app.show_menu)

root.mainloop()
