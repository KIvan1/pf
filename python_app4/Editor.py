import tkinter as tk

def json_editor(jsonData):
	def change_data():
		k = 0
		for i in jsonData:
			#jsonData[i] = newData[k].get()
			k += 1
	ed_window = tk.Tk()
	ed_window.title("Json editor")
	name = []
	data = []
	newData = []
	json_frame = []
	j = 0
	frame = tk.Frame(ed_window)
	save_button = tk.Button(frame, text = "Save", command = change_data)
	save_as_button = tk.Button(frame, text = "Save as")
	save_button.pack(side = tk.LEFT)
	save_as_button.pack(side = tk.LEFT)
	frame.pack() 
	for i in jsonData:
		json_frame.append(tk.Frame(ed_window))
		name.append(tk.Label(json_frame[j], text = i + ': '))
		name[j].pack(fill = tk.X, side = tk.LEFT)
		newData.append(tk.StringVar())
		data.append(tk.Entry(json_frame[j], fg = "blue", textvariable = newData[j]))
		data[j].insert(0, jsonData[i])
		data[j].pack(fill = tk.X)
		json_frame[j].pack(fill = tk.X)
		j += 1
	ed_window.mainloop()
	return data
