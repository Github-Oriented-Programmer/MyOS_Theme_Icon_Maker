import os

icon_name_by_line=os.listdir('.\icon')


name_dict={}

#读取已有文件并创建字典
with open('NameList.csv',"a",encoding='utf-8') as name_list_old:
    name_list_old.close()

with open('NameList.csv',encoding='utf-8') as name_list_old:
    old_by_line=name_list_old.readlines()
    for line in old_by_line:
        a1=line.find(',')
        a2=line.find(',',a1+1)
        pkgname=line[a1+1:a2]
        appname=line[:a1]
        activity=line[a2+1:-1]
        name_dict.update({pkgname:[appname]+activity.split(',')})
    name_list_old.close()

contents=''

with open('NameList.csv', "w",encoding='utf-8') as name_list:
    for line in icon_name_by_line:
        line=line[:-4]#去掉.png
        line=line.replace('_','.')
        AppName=''#zte主题包格式无法获取到应用名称
        PkgName=line[:line.find('-')]
        StartActivity=line[line.find('-')+1:]
        if name_dict.get(PkgName)!=None: #已存在相关记录
            a=0
            for s in name_dict[PkgName]:
                if s==StartActivity:
                    a=1
            if a==0: #不存在该启动类
                name_dict.update({PkgName:name_dict[PkgName]+[StartActivity]})
            """ if name_dict[PkgName][0]=='':#如果应用名为空，则补上应用名
                l=name_dict[PkgName]
                l[0]=AppName
                name_dict.update({PkgName:l}) """
        else : #无记录
            name_dict.update({PkgName:[AppName]+[StartActivity]})
    for key in name_dict.keys():
        a=''
        for str in name_dict[key][1:]:
            a=a+','+str
        l=name_dict[key][0]+','+key+','+a[1:]+'\n'
        contents=contents+l
    name_list.write(contents)
    name_list.close()