import re,os,codecs




def switch_content(filename):
    with open(fr'Y:\CASE2023\2023-193\2023-193\案件（20230706094745）\2023-193-2报告_html\Report\{filename}',
              mode='r', encoding='utf-16') as C:
        # contents = C.read()
        # print(codecs.escape_decode(contents)[0].decode("unicode_escape"))   #比较麻烦的方式，再次对比特流进行处理，mode='rb'
        contents = C.read()

    update_contents = contents
    num = 0
    pattern = r'(<param name="MediaFile"[\s\S]*?amr)"'  # 正则
    results = re.findall(pattern, contents)
    for i in results:
        num += 1
        new_documents = i.split('\\')[-1]
        new_documents2 = new_documents.split('.')[-2]

        # 重新截断路径，后MicroMsg后面的变化段
        # path_back_one = i.split('\\')
        path_back_one = '\\'.join(i.split('\\')[-5:])
        path_back_two = path_back_one.split('"')[0]  # 变化段带后缀
        path_back_three = path_back_two.split('.')[0]  # 变化段不带后缀

        # 重新组装调换标签
        finally_document = rf'<a href="Data\AppAttach\WeiXin\tencent\sdcard\Android\data\com.tencent.mm\MicroMsg\{path_back_three}.wav">点击播放音频</a>'
        i = i + r'" />'

        # print(i)
        print(finally_document)
        print(f'{num}次')
        # 全文检索调换
        update_contents = update_contents.replace(i, finally_document)
        # print(update_contents)

    with open(
              fr'Y:\CASE2023\2023-193\2023-193\案件（20230706094745）\2023-193-2报告_html\Report\{filename}',
              mode='w', encoding='utf-16') as W:
        t = str(update_contents)
        W.write(t)
        # print(update_contents)
        print(f'替换了{num}次')
        W.close()



