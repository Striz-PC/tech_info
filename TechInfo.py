# Importing libraries
from tkinter import *
import cpuinfo
import psutil
import platform

# Creating window
window = Tk()
window.geometry("450x350")
window.title("TechInfo - Инфо о ПК")
window.config(bg="gray18")
window.resizable(False, False)

cpu_brand = cpuinfo.get_cpu_info()["brand_raw"]
cpu_cores = psutil.cpu_count(logical=False)
logical_cpu_cores = psutil.cpu_count(logical=True)
max_cpu_freq = f"{psutil.cpu_freq().max}GHz"
avg_cpu_freq = f"{psutil.cpu_freq().current}GHz"
min_cpu_freq = f"{psutil.cpu_freq().min}GHz"
architecture = platform.architecture()
windows_ver = platform.release()
pc_name = platform.node()
os_version = platform.version()
system = platform.system()

# Texts
label = Label(height=1, width=20, text="PROCESSOR INFO", font="Courier 22", bg="gray18", fg="white")
label.pack()

label = Label(width=0, text=f"CPU: {cpu_brand}", font="Courier 12", bg="gray18", fg="white")
label.pack()

label = Label(width=0, text=f"CPU's: {cpu_cores}", font="Courier 12", bg="gray18", fg="white")
label.pack()

label = Label(width=0, text=f"Logical CPU's: {logical_cpu_cores}", font="Courier 12", bg="gray18", fg="white")
label.pack()

label = Label(width=0, text=f"CPU Frequency (Min): {min_cpu_freq}", font="Courier 12", bg="gray18", fg="white")
label.pack()

label = Label(width=0, text=f"CPU Frequency (Avg): {avg_cpu_freq}", font="Courier 12", bg="gray18", fg="white")
label.pack()

label = Label(width=0, text=f"CPU Frequency (Max): {max_cpu_freq}", font="Courier 12", bg="gray18", fg="white")
label.pack()

label = Label(width=0, text=f"OS INFO", font="Courier 22", bg="gray18", fg="white")
label.pack()

label = Label(width=0, text=f"OS: {system}", font="Courier 12", bg="gray18", fg="white")
label.pack()

label = Label(width=0, text=f"OS Version: {windows_ver}", font="Courier 12", bg="gray18", fg="white")
label.pack()

label = Label(width=0, text=f"OS Release: {os_version}", font="Courier 12", bg="gray18", fg="white")
label.pack()

label = Label(width=0, text=f"Architecture: {architecture}", font="Courier 12", bg="gray18", fg="white")
label.pack()

label = Label(width=0, text=f"PC Name: {pc_name}", font="Courier 12", bg="gray18", fg="white")
label.pack()

# Run TechInfo
window.mainloop()
