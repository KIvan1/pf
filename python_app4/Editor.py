import tkinter as tk

def json_editor(jsonData):
	def change_data():
		k = 0
		for i in jsonData:
			jsonData[i] = newData[k].get()
			k += 1

	def add():
		add_str = {key.get(): addData.get()}
		jsonData.update(add_str)

		json_frame.append(tk.Frame(ed_window))
		name.append(tk.Label(json_frame[len(json_frame) - 1], text = key.get() + ': '))
		name[len(name) - 1].pack(fill = tk.X, side = tk.LEFT)
		newData.append(tk.StringVar())
		data.append(tk.Entry(json_frame[len(json_frame) - 1], fg = "blue", textvariable = newData[len(newData) - 1]))
		data[len(data) - 1].insert(0, jsonData[key.get()])
		data[len(data) - 1].pack(fill = tk.X)
		json_frame[len(json_frame) - 1].pack(fill = tk.X)

		ed_window.update()

	ed_window = tk.Tk()
	ed_window.title("Json editor")

	save_frame = tk.Frame(ed_window)
	save_button = tk.Button(save_frame, text = "Save", command = change_data)
	save_button.pack(side = tk.LEFT)
	save_frame.pack()
	
	add_frame = tk.Frame(ed_window)
	add_button = tk.Button(add_frame, text = "Add data", command = add)
	key_label = tk.Label(add_frame, text = "Key: ")
	data_label = tk.Label(add_frame, text = "data: ")
	addData = tk.StringVar()
	key = tk.StringVar()
	add_key = tk.Entry(add_frame, textvariable = key)
	add_data = tk.Entry(add_frame, textvariable = addData)
	add_button.pack(side = tk.RIGHT)
	key_label.pack(side = tk.LEFT)
	add_key.pack(side = tk.LEFT)
	data_label.pack(side = tk.LEFT)
	add_data.pack(side = tk.LEFT)
	add_frame.pack(side = tk.BOTTOM)

	name = []
	data = []
	newData = []
	json_frame = []
	j = 0
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
	return jsonData
