file_name = "data.txt"
sum = 0

with open(file_name, 'r') as file:
    for line in file: #1行ずつ読み込む
        try:
            if float(line).is_integer():
                sum += int(line)
            else:
                pass
        except:
            pass
print(sum)