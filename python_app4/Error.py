import tkinter as tk

def Error_message_box():
	def exit():
		err_win.destroy()
	err_win = tk.Tk()
	error_label = tk.Label(text = "Wrong argument: incorrect link", fg = "red", width = 50, height = 3)
	exit_button = tk.Button(text = "OK", command = exit, width = 8, height = 2)
	error_label.pack()
	exit_button.pack()
	err_win.mainloop()