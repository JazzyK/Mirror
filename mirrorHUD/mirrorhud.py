from Tkinter import*


window = Tk()
window.title("mirrorHUD")
window.configure(background = "black")

# make it cover the entire screen
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.overrideredirect(1)
window.geometry("%dx%d+0+0" % (w, h))

window.mainloop()