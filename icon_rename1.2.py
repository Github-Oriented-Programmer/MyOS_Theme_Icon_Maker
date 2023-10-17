import os
from shutil import copyfile

icon_name = os.listdir('./icons')

name_dict = {}

with open('NameList.csv', encoding='utf-8') as name_list:
    by_line = name_list.readlines()
    for line in by_line:
        a1 = line.find(',')
        a2 = line.find(',', a1 + 1)
        pkgname = line[a1 + 1:a2]
        appname = line[:a1]
        activity = line[a2 + 1:-1]
        name_dict.update({pkgname: activity.split(',')})

os.mkdir('icons_out')

# Simple string-based progress bar
def progress_bar(current, total, length=50):
    progress = int(length * current / total)
    bar = '[' + '=' * progress + ' ' * (length - progress) + ']'
    return f'{current}/{total} {bar}'

total_icons = len(icon_name)
for i, name_old in enumerate(icon_name, 1):
    name_new = name_old[:-4]
    if name_dict.get(name_new) is not None:
        for activity_str in name_dict[name_new]:
            name_new1 = f"{name_new.replace('.', '_')}-{activity_str.replace('.', '_')}.png"
            copyfile(os.path.join('./icons', name_old), os.path.join('./icons_out', name_new1))
    
    # Display progress
    print(progress_bar(i, total_icons), end='\r')

print('\nCopying completed.')
