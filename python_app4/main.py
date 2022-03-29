import Uplode
import Open
import Link
import Editor
import tkinter as tk

s = Link.Ask_link()
#s = "http://kappa.cs.petrsu.ru/~dimitrov/info_1/test.json"
print(s)
jsonData = Uplode.fuplode(s)
print(jsonData)
jsonData = Editor.json_editor(jsonData)
print("\n\n")
print(jsonData)