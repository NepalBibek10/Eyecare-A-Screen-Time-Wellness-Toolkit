
import time
import tkinter as tk

def show_message():
    alert=tk.Label(root,text="ALERT!!!",font=("Arial 100 bold"),fg='#ff0000',bg="#a6a6a6") # display the Alert text in bold  and 100 size
    alert.pack(expand=True)
    message=tk.Label(root,text="Focus on Object which \n are 20ft away for 20 sec",font=("Arial 80 bold"),fg='#000000',bg="#a6a6a6") # display message
    message.pack(expand=True)
def show_timer():
    timer_label = tk.Label(root, text="20", font=("Arial 50 bold"),fg='#000000',bg="#a6a6a6") # timer for 20 sec
    timer_label.pack(expand=True)
    remaining_time = 20
    while remaining_time >= 0:
        time_str = time.strftime('%S', time.gmtime(remaining_time))
        timer_label.configure(text=time_str)
        root.update()
        time.sleep(1)
        remaining_time -= 1
    root.after(10, root.destroy)
    root.mainloop()
while True:
    time.sleep(1200)   # sleep the for 20 mins
    root=tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="#a6a6a6")
    show_message()
    show_timer()



