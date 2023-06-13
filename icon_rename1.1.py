import os
from shutil import copyfile

icon_name=os.listdir('.\icons')

name_dict={}

with open('NameList.csv',encoding='utf-8') as name_list:
    by_line=name_list.readlines()
    print(name_list.read())
    for line in by_line:
        a1=line.find(',')
        a2=line.find(',',a1+1)
        pkgname=line[a1+1:a2]
        appname=line[:a1]
        activity=line[a2+1:-1]
        name_dict.update({pkgname:activity.split(',')})
    name_list.close()

os.mkdir('icons_out')

for name_old in icon_name:
    name_new=name_old[:-4]
    if name_dict.get(name_new)!=None:
        for str in name_dict[name_new]:
            name_new1=name_new.replace('.','_')+'-'+str.replace('.','_')+'.png'
            copyfile('./icons/'+name_old,'./icons_out/'+name_new1)
        