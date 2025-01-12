import os
import json

#Короч это скрипт который рекурсивно генерит json с путями пнгэх

rootDir = 'ROOT'

def getNode(directory):
    node = {}
    node['name'] = os.path.basename(directory)[1:]
    dlist = os.listdir(directory)
    for d in dlist:
        if os.path.isfile(os.path.join(directory, d)):
            node[os.path.splitext(d)[0]] = os.path.join(directory, d)
            print(node)
    return node

def buildStruct(directory):
    dir_list = os.listdir(directory)
    NON = 1 #Number Of Nodes
    m = {} 
    for dir in dir_list:
        if os.path.isfile(os.path.join(directory, dir)):
            m[dir] = os.path.join(directory, dir)
        else:
            if dir[0] == '_':
                m[NON] = getNode(os.path.join(os.path.join(directory, dir)))
                NON += 1
            else:   
                m[dir] = buildStruct(os.path.join(directory, dir))
    return m


        
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(buildStruct(rootDir), f, indent=4, ensure_ascii=False)

print('ok')
