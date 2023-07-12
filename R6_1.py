import zipfile
import json

with zipfile.ZipFile('kabeposter.zip', 'r') as zfile:
    for name in zfile.namelist():
        if "000000000000" in name:
            with zfile.open(name,'r')as jfile:
                data = json.load(jfile)
                people_data = data["people"]
                data1 = people_data[0]
                data2 = people_data[1]
                print(data1["pose_keypoints_2d"][0])
                print(data1["pose_keypoints_2d"][1])
                print(data1["pose_keypoints_2d"][2])
                
                print(data2["pose_keypoints_2d"][0])
                print(data2["pose_keypoints_2d"][1])
                print(data2["pose_keypoints_2d"][2])