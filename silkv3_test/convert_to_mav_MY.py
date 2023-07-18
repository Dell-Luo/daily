import os

#路径文件名过长，cmd装不下，导入到一二级目录下遍历即可。
# file_path  =  "Y:\\CASE2023\\2023-193\\2023-193\\案件（20230706094745）\\2023-193-2报告_html\\Report\\Data\\AppAttach\\WeiXin\\tencent\\sdcard\\Android\\data\\com.tencent.mm\\MicroMsg"
file_path = r"C:\Users\JY-YQ-51\Desktop\AMR音频\arm_pcm_mp3\test3"
object_walk = os.walk(file_path)
os.system('chcp 65001')

# print(object_walk)
for root,dirs,file_name in object_walk:
    # print(root, file_name)
    if "voice2" in root and file_name != [] :
        # print(root,file_name)
        for voice_document in file_name :
            path_and_name = root+'\\'+voice_document    #绝对路径，格式正确
            name_suffix = path_and_name.split('.')[-1]
            name_prefix ='.'.join(path_and_name.split('.')[:-1])
            half_document_pcm = name_prefix + '.pcm'    #第一次转pcm
            half_document_wav = name_prefix + '.wav'   #第二次转wav
            # print(half_document_wav)
            # print(name_suffix)

            #对后缀做判断，amr格式才处理
            if name_suffix == 'amr':
                try:
                    os.system(f'.\\silk_v3_decoder.exe {path_and_name} {half_document_pcm}')
                    os.system(f'.\\ffmpeg.exe -y -f s16be -ac 2 -ar 13000 -acodec pcm_s16le -i {half_document_pcm} {half_document_wav}')
                #     # os.system(f'del {half_document_pcm},{document_old}')   #删除原始数据
                    print(f"{half_document_wav}, has done!")
                except Exception as e:
                    print(e)



