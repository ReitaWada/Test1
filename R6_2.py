import zipfile
import json
import tkinter as tk

root = tk.Tk()
root.geometry("500x400")

canvas = tk.Canvas(root, bg = "white")

with zipfile.ZipFile('kabeposter.zip', 'r') as zfile:
    for name in zfile.namelist():
        if "000000000000" in name:
            with zfile.open(name,'r')as jfile:
                data = json.load(jfile)
                people_data = data["people"]
                data1 = people_data[0]
                data2 = people_data[1]