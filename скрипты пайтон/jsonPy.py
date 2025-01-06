import os
import json

d = 'Манул_Креатор_layers'

def buildStruc(directory):
    dir_list = os.listdir(directory)
    m = []
    for dir in dir_list:
        if os.path.isfile(os.path.join(directory, dir)):
            m.append(os.path.join(directory, dir))
        else:
            m.append(buildS(os.path.join(directory, dir)))
    return {directory : m}


        
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(buildS(d), f, indent=4, ensure_ascii=False)
