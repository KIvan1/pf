import Uplode
import Open
import Link
import Editor
import tkinter as tk

s = ""
s = Link.Ask_link(s)
print(s)
s = "http://kappa.cs.petrsu.ru/~dimitrov/info_1/test.json"
jsonData = Uplode.fuplode(s)
print(jsonData)
jsonData = Editor.json_editor(jsonData)
print("\n\n")
print(jsonData)