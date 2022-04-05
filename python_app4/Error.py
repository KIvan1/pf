import tkinter as tk

def Error_message_box():
	def exit():
		err_win.destroy()

	def exit_comb(entry):
		exit()
	err_win = tk.Tk()
	err_win.title("Error")
	error_label = tk.Label(text = "Wrong argument: incorrect link", fg = "red", width = 50, height = 3)
	exit_button = tk.Button(text = "OK", command = exit, width = 8, height = 2)
	err_win.bind('<Return>', exit_comb)
	error_label.pack()
	exit_button.pack()
	err_win.mainloop()

def Error_format():
	def exit():
		err_win.destroy()
	def exit_comb(event):
		exit()
	err_win = tk.Tk()
	err_win.title("Error")
	error_label = tk.Label(err_win, text = "Incorrect data", fg = "red", width = 50, height = 3)
	exit_button = tk.Button(err_win, text = "OK", command = exit, width = 8, height = 2)
	err_win.bind('<Return>', exit_comb)
	error_label.pack()
	exit_button.pack()
	err_win.mainloop()