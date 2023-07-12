import zipfile
import json
import tkinter as tk

root = tk.Tk()
root.geometry("1350x950")

canvas = tk.Canvas(root, bg = "white")

canvas.pack(fill = tk.BOTH, expand = True)

with zipfile.ZipFile('kabeposter.zip', 'r') as zfile:
    for name in zfile.namelist():
        if "000000000000" in name:
            with zfile.open(name,'r')as jfile:
                data = json.load(jfile)
                people_data = data["people"]
                data1 = people_data[0]
                data2 = people_data[1]
                
                canvas.create_line(data1["pose_keypoints_2d"][6], data1["pose_keypoints_2d"][7], data1["pose_keypoints_2d"][15], data1["pose_keypoints_2d"][16])
                
                canvas.create_line(data2["pose_keypoints_2d"][6], data2["pose_keypoints_2d"][7], data2["pose_keypoints_2d"][15], data2["pose_keypoints_2d"][16])
                
                root.mainloop()