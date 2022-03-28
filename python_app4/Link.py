import tkinter as tk

def Ask_link():
	window = tk.Tk()
	text = tk.Label(text = "Вводите ссылку на json файл")
	text.pack()
	entry = tk.Entry(width = 50, fg = "blue")
	entry.pack()
	button = tk.Button(text = "OK", width = 10, height = 2, fg = "blue")
	button.pack()
	s = entry.get()
	window.mainloop()
	return s