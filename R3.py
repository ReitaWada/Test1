import zipfile
sum = 0

with zipfile.ZipFile('sample.zip', 'r') as file:
    lst = file.namelist()
    
    for name in lst:
        if "kitamura" in name:
            if int(name.split('_')[1]) % 2 != 0:
                with file.open(name, 'r') as f:
                    contents = f.read()
                    number = int(contents.strip())
                    sum += number
print(sum)
                    
