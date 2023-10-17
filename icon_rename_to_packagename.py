import os
import xml.etree.ElementTree as ET

def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    renaming_dict = {}

    for icon, adaptation in zip(root.findall('icon'), root.findall('adaptation')):
        icon_name = icon.get('name')
        drawable = icon.get('drawable')
        package_name = adaptation.get('packageName')
        if icon_name and drawable and package_name:
            renaming_dict[drawable] = package_name

    return renaming_dict

def rename_png_files(folder_path, renaming_dict):
    files_renamed = 0

    for drawable, package_name in renaming_dict.items():
        old_path = os.path.join(folder_path, f'{drawable}.png')
        new_path = os.path.join(folder_path, f'{package_name}.png')

        if os.path.exists(old_path) and not os.path.exists(new_path):
            os.rename(old_path, new_path)
            print(f'Renamed: {old_path} to {new_path}')
            files_renamed += 1
        elif os.path.exists(new_path):
            print(f'File already renamed: {new_path}')
        else:
            print(f'File not found: {old_path}')

    return files_renamed

if __name__ == "__main__":
    xml_file = 'backup.xml'  # XML文件路径为当前目录下的backup.xml
    folder_path = 'icons'  # icons文件夹路径为当前目录下的icons文件夹

    if not os.path.exists(folder_path):
        print(f'Folder not found: {folder_path}')
        exit()

    renaming_dict = parse_xml(xml_file)
    total_files_renamed = rename_png_files(folder_path, renaming_dict)

    print(f'Total files renamed: {total_files_renamed}')
    print('Renaming completed.')
