import zipfile
import json
import tkinter as tk
import time

n=0
def animate():
    global root
    global n
    if n<10:
        with zipfile.ZipFile('kabeposter.zip', 'r') as zfile:
            for name in zfile.namelist():
                with zfile.open(name,'r')as jfile:
                    data = json.load(jfile)
                    people_data = data["people"]
                    data1 = people_data[0]
                    data2 = people_data[0]
                    print(name)
                    canvas.create_line(data1["pose_keypoints_2d"][0], data1["pose_keypoints_2d"][1], data1["pose_keypoints_2d"][3], data1["pose_keypoints_2d"][4])
                    canvas.create_line(data1["pose_keypoints_2d"][3], data1["pose_keypoints_2d"][4], data1["pose_keypoints_2d"][6], data1["pose_keypoints_2d"][7])
                    canvas.create_line(data1["pose_keypoints_2d"][6], data1["pose_keypoints_2d"][7], data1["pose_keypoints_2d"][9], data1["pose_keypoints_2d"][10])
                    canvas.create_line(data1["pose_keypoints_2d"][9], data1["pose_keypoints_2d"][10], data1["pose_keypoints_2d"][12], data1["pose_keypoints_2d"][13])
                    canvas.create_line(data1["pose_keypoints_2d"][3], data1["pose_keypoints_2d"][4], data1["pose_keypoints_2d"][15], data1["pose_keypoints_2d"][16])
                    canvas.create_line(data1["pose_keypoints_2d"][15], data1["pose_keypoints_2d"][16], data1["pose_keypoints_2d"][18], data1["pose_keypoints_2d"][19])
                    canvas.create_line(data1["pose_keypoints_2d"][18], data1["pose_keypoints_2d"][19], data1["pose_keypoints_2d"][21], data1["pose_keypoints_2d"][22])
                    canvas.create_line(data1["pose_keypoints_2d"][3], data1["pose_keypoints_2d"][4], data1["pose_keypoints_2d"][24], data1["pose_keypoints_2d"][25])
                    canvas.create_line(data1["pose_keypoints_2d"][24], data1["pose_keypoints_2d"][25], data1["pose_keypoints_2d"][27], data1["pose_keypoints_2d"][28])
                    canvas.create_line(data1["pose_keypoints_2d"][27], data1["pose_keypoints_2d"][28], data1["pose_keypoints_2d"][30], data1["pose_keypoints_2d"][31])
                    canvas.create_line(data1["pose_keypoints_2d"][30], data1["pose_keypoints_2d"][31], data1["pose_keypoints_2d"][33], data1["pose_keypoints_2d"][34])
                    canvas.create_line(data1["pose_keypoints_2d"][33], data1["pose_keypoints_2d"][34], data1["pose_keypoints_2d"][66], data1["pose_keypoints_2d"][67])
                    canvas.create_line(data1["pose_keypoints_2d"][33], data1["pose_keypoints_2d"][34], data1["pose_keypoints_2d"][72], data1["pose_keypoints_2d"][73])
                    canvas.create_line(data1["pose_keypoints_2d"][66], data1["pose_keypoints_2d"][67], data1["pose_keypoints_2d"][69], data1["pose_keypoints_2d"][70])
                    canvas.create_line(data1["pose_keypoints_2d"][24], data1["pose_keypoints_2d"][25], data1["pose_keypoints_2d"][36], data1["pose_keypoints_2d"][37])
                    canvas.create_line(data1["pose_keypoints_2d"][36], data1["pose_keypoints_2d"][37], data1["pose_keypoints_2d"][39], data1["pose_keypoints_2d"][40])
                    canvas.create_line(data1["pose_keypoints_2d"][39], data1["pose_keypoints_2d"][40], data1["pose_keypoints_2d"][42], data1["pose_keypoints_2d"][43])
                    canvas.create_line(data1["pose_keypoints_2d"][42], data1["pose_keypoints_2d"][43], data1["pose_keypoints_2d"][63], data1["pose_keypoints_2d"][64])
                    canvas.create_line(data1["pose_keypoints_2d"][42], data1["pose_keypoints_2d"][43], data1["pose_keypoints_2d"][57], data1["pose_keypoints_2d"][58])
                    canvas.create_line(data1["pose_keypoints_2d"][57], data1["pose_keypoints_2d"][58], data1["pose_keypoints_2d"][60], data1["pose_keypoints_2d"][61])
                    canvas.create_line(data1["pose_keypoints_2d"][0], data1["pose_keypoints_2d"][1], data1["pose_keypoints_2d"][45], data1["pose_keypoints_2d"][46])
                    canvas.create_line(data1["pose_keypoints_2d"][45], data1["pose_keypoints_2d"][46], data1["pose_keypoints_2d"][51], data1["pose_keypoints_2d"][52])
                    canvas.create_line(data1["pose_keypoints_2d"][0], data1["pose_keypoints_2d"][1], data1["pose_keypoints_2d"][48], data1["pose_keypoints_2d"][49])
                    canvas.create_line(data1["pose_keypoints_2d"][48], data1["pose_keypoints_2d"][49], data1["pose_keypoints_2d"][54], data1["pose_keypoints_2d"][55])
                    
                    canvas.create_line(data2["pose_keypoints_2d"][0], data2["pose_keypoints_2d"][1], data2["pose_keypoints_2d"][3], data2["pose_keypoints_2d"][4])
                    canvas.create_line(data2["pose_keypoints_2d"][3], data2["pose_keypoints_2d"][4], data2["pose_keypoints_2d"][6], data2["pose_keypoints_2d"][7])
                    canvas.create_line(data2["pose_keypoints_2d"][6], data2["pose_keypoints_2d"][7], data2["pose_keypoints_2d"][9], data2["pose_keypoints_2d"][10])
                    canvas.create_line(data2["pose_keypoints_2d"][9], data2["pose_keypoints_2d"][10], data2["pose_keypoints_2d"][12], data2["pose_keypoints_2d"][13])
                    canvas.create_line(data2["pose_keypoints_2d"][3], data2["pose_keypoints_2d"][4], data2["pose_keypoints_2d"][15], data2["pose_keypoints_2d"][16])
                    canvas.create_line(data2["pose_keypoints_2d"][15], data2["pose_keypoints_2d"][16], data2["pose_keypoints_2d"][18], data2["pose_keypoints_2d"][19])
                    canvas.create_line(data2["pose_keypoints_2d"][18], data2["pose_keypoints_2d"][19], data2["pose_keypoints_2d"][21], data2["pose_keypoints_2d"][22])
                    canvas.create_line(data2["pose_keypoints_2d"][3], data2["pose_keypoints_2d"][4], data2["pose_keypoints_2d"][24], data2["pose_keypoints_2d"][25])
                    canvas.create_line(data2["pose_keypoints_2d"][24], data2["pose_keypoints_2d"][25], data2["pose_keypoints_2d"][27], data2["pose_keypoints_2d"][28])
                    canvas.create_line(data2["pose_keypoints_2d"][27], data2["pose_keypoints_2d"][28], data2["pose_keypoints_2d"][30], data2["pose_keypoints_2d"][31])
                    canvas.create_line(data2["pose_keypoints_2d"][30], data2["pose_keypoints_2d"][31], data2["pose_keypoints_2d"][33], data2["pose_keypoints_2d"][34])
                    canvas.create_line(data2["pose_keypoints_2d"][33], data2["pose_keypoints_2d"][34], data2["pose_keypoints_2d"][66], data2["pose_keypoints_2d"][67])
                    canvas.create_line(data2["pose_keypoints_2d"][33], data2["pose_keypoints_2d"][34], data2["pose_keypoints_2d"][72], data2["pose_keypoints_2d"][73])
                    canvas.create_line(data2["pose_keypoints_2d"][66], data2["pose_keypoints_2d"][67], data2["pose_keypoints_2d"][69], data2["pose_keypoints_2d"][70])
                    canvas.create_line(data2["pose_keypoints_2d"][24], data2["pose_keypoints_2d"][25], data2["pose_keypoints_2d"][36], data2["pose_keypoints_2d"][37])
                    canvas.create_line(data2["pose_keypoints_2d"][36], data2["pose_keypoints_2d"][37], data2["pose_keypoints_2d"][39], data2["pose_keypoints_2d"][40])
                    canvas.create_line(data2["pose_keypoints_2d"][39], data2["pose_keypoints_2d"][40], data2["pose_keypoints_2d"][42], data2["pose_keypoints_2d"][43])
                    canvas.create_line(data2["pose_keypoints_2d"][42], data2["pose_keypoints_2d"][43], data2["pose_keypoints_2d"][63], data2["pose_keypoints_2d"][64])
                    canvas.create_line(data2["pose_keypoints_2d"][42], data2["pose_keypoints_2d"][43], data2["pose_keypoints_2d"][57], data2["pose_keypoints_2d"][58])
                    canvas.create_line(data2["pose_keypoints_2d"][57], data2["pose_keypoints_2d"][58], data2["pose_keypoints_2d"][60], data2["pose_keypoints_2d"][61])
                    canvas.create_line(data2["pose_keypoints_2d"][0], data2["pose_keypoints_2d"][1], data2["pose_keypoints_2d"][45], data2["pose_keypoints_2d"][46])
                    canvas.create_line(data2["pose_keypoints_2d"][45], data2["pose_keypoints_2d"][46], data2["pose_keypoints_2d"][51], data2["pose_keypoints_2d"][52])
                    canvas.create_line(data2["pose_keypoints_2d"][0], data2["pose_keypoints_2d"][1], data2["pose_keypoints_2d"][48], data2["pose_keypoints_2d"][49])
                    canvas.create_line(data2["pose_keypoints_2d"][48], data2["pose_keypoints_2d"][49], data2["pose_keypoints_2d"][54], data2["pose_keypoints_2d"][55])
                    #print("aiueo")
                    n += 1
                    root.after(1000, animate)
    #if n < n1:
        #root.after(1000, animate)
       

    

root = tk.Tk()
root.geometry("1500x1500")

canvas = tk.Canvas(root, bg = "white")

canvas.pack(fill = tk.BOTH, expand = True)

root.after(1000, animate)#animate()
root.mainloop() 
#i = 0

            
            
        
            # if i >= 10:
            #     a = "0000000000" + str(i)
            # else:
            #     a = "00000000000" + str(i)
            # print(a)          
            # if a in name:
                    #time.sleep(0.1)
                    
                    #animate(data)

                #people2.append(people_data[1])
                
                
                #def human():
                    #global n
                    #data1 = people1[n]
                    #data2 = people_data[n]
                    
                
                    
                    # print(1)
                #def move():
                    #for i range(0,23)
                    #canvas.move("h", data1["pose_keypoints_2d"][i+1] - data1["pose_keypoints_2d"][i], data1["pose_keypoints_2d"][3*i+1] - data1["pose_keypoints_2d"][3*i])
                    #canvas.after(100, move)

                    # i += 1
    
                #move()
                    