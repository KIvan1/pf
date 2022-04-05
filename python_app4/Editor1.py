import tkinter as tk
from tkinter.filedialog import asksaveasfilename
import json
from pprint import pformat
from Error import Error_format

def json_editor(jsonData):
	file_way = None
	def save_as():
		try:
			filepath = asksaveasfilename()
			global file_way
			file_way = filepath
			if not filepath:
				return
			with open(filepath, "w") as json_out_file:
				string = main_text.get('1.0', tk.END)
				string = string.replace('\n','')
				jsonData = eval(string)
				json.dump(jsonData, json_out_file)
		except SyntaxError:
			Error_format()

	def save():
		try:
			global file_way
			with open(file_way, "w") as json_out_file:
				string = main_text.get('1.0', tk.END)
				string = string.replace('\n','')
				jsonData = eval(string)
				json.dump(jsonData, json_out_file)
		except SyntaxError:
			Error_format()
			file_way = None
		except (NameError, TypeError, FileNotFoundError):
			save_as()

	def save_comb(event):
		save()

	def press_enter(event):
		data = main_text.get('1.0',tk.INSERT)
		if data[len(data) - 1] != ',':
			main_text.insert(tk.INSERT, ',')

	def press_space(event):
		data = main_text.get('1.0',tk.INSERT)
		if data[len(data) - 1] == '\'' or data[len(data) - 1] == '\"':
			main_text.insert(tk.INSERT, ':')

	ed_window = tk.Tk()
	save_frame = tk.Frame(ed_window)
	save_as_button = tk.Button(save_frame, text = "Save as", command = save_as)
	save_as_button.pack(side = tk.LEFT)
	save_button = tk.Button(save_frame, text = "Save", command = save)
	save_button.pack(side = tk.LEFT)
	save_frame.pack(fill = tk.X)
	ed_frame = tk.Frame(ed_window)
	scroll = tk.Scrollbar(ed_frame, orient = tk.VERTICAL)
	main_text = tk.Text(ed_frame, yscrollcommand = scroll.set)
	main_text.insert(1.0, pformat(jsonData, width = main_text['width']))
	main_text.bind('<Return>', press_enter)
	main_text.bind('<Control-s>', save_comb)
	main_text.bind('<space>', press_space)
	scroll.configure(command = main_text.yview)
	scroll.pack(side = tk.RIGHT, fill = tk.Y)
	main_text.pack(fill = tk.BOTH)
	ed_frame.pack(fill = tk.BOTH)
	ed_window.mainloop()
	return jsonData