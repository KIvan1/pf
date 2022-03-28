import tkinter as tk

def json_editor(jsonData):
	ed_window = tk.Tk()
	name = []
	data = []
	j = 0
	for i in jsonData:
		name.append(tk.Label(text = i))
		name[j].pack()
		j += 1
	ed_window.mainloop()
	return data
