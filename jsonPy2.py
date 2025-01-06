import os
import json

#Короч это скрипт который генерит json с путями пнгэх

d = 'Манул_Креатор_layers'

def buildStruct(directory, name):
    dir_list = os.listdir(directory)
    m = []
    for dir in dir_list:
        if os.path.isfile(os.path.join(directory, dir)):
            m.append(os.path.join(directory, dir))
        else:
            m.append(buildStruct(os.path.join(directory, dir), dir))
    return {name : m}


        
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(buildStruct(d, d), f, indent=4, ensure_ascii=False)

print('ok')
