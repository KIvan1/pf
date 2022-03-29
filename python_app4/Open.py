import tkinter as tk

def F():
	resultString.set(resultString1.get())
	print(resultString.get())
window = tk.Tk()
resultString1 = tk.StringVar()
entry = tk.Entry(textvariable = resultString1)
entry.pack()
resultString = tk.StringVar()
button = tk.Button(window, text = "Ok", command = F)
button.pack()
window.mainloop()
