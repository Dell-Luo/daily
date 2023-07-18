import os,web_switch

def switch_all(folder_path):
    # 获取一级子目录下的文件名，列表推导式
    file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    print(file_names)

    # 遍历文件名
    for file_name in file_names:
        if file_name.startswith('Contents'):
            print(file_name, "initiate")
            web_switch.switch_content(file_name)
            print(file_name, "done!")
