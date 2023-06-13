import os
with open('backup.xml', encoding='utf-8') as name_o:
    contents_by_line=name_o.readlines()
    name_o.close()

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
    for line in contents_by_line:
        if line.find('adaptation')!=-1 :
            AppName=line[line.find('appName=')+9:line.find('"',line.find('appName=')+9)]
            PkgName=line[line.find('packageName=')+13:line.find('"',line.find('packageName=')+13)]
            StartActivity=line[line.find('startActivity=')+15:line.find('"',line.find('startActivity=')+15)]
            if name_dict.get(PkgName)!=None: #已存在相关记录
                a=0
                for s in name_dict[PkgName]:
                    if s==StartActivity:
                        a=1
                if a==0: #不存在该启动类
                    name_dict.update({PkgName:name_dict[PkgName]+[StartActivity]})
                if name_dict[PkgName][0]=='':#如果应用名为空，则补上应用名
                    l=name_dict[PkgName]
                    l[0]=AppName
                    name_dict.update({PkgName:l})
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