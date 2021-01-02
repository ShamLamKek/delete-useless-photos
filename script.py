import os
import re


print("Введите путь к телеметрии")
x = input()
photos = []
with open(x, "r") as f:
    photos = f.readlines()
    for i in range(len(photos)):
        photos[i] = re.sub(r"#" + '.*', "", photos[i])
        photos[i] = re.sub(r'\t' + '.*', "", photos[i])
        photos[i] = re.sub(r"\n", "", photos[i])
    photos = [x for x in photos if x]
    photos = [x + ".JPG" for x in photos]

print("Введите путь к фотографиям")
y = input()
files = os.listdir(y)
files = filter(lambda x: x.endswith('.JPG'), files)

to_remove = []
for i in files:
    if i not in photos:
        to_remove.append(i)

for j in to_remove:
    j = os.path.join(y, j)
    os.remove(j)

if __name__ == "__main__":
    print("--------- ЗАПУСК СКРИПТА ------")
