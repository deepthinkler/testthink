#coding:utf-8
from moviepy.editor import *
import os

# 定义一个数组


def getFileList(path):
    L=[]
    listmv=os.listdir(path)
    print(listmv)
    for each in listmv:
        if os.path.isfile(path+'\\'+each) :
            if each.endswith('.mp4') or each.endswith('.MP4'):
                # print(int(each.strip('.mp4')))
                #注意我的文件夹里的视频都是数字+.mp4的!如果不是这种命名格式就修改下面代码！！！！！！！！！！！！！！！！！！！！！！！！！

                L.append(each.split('.')[0])
    L.sort()
    # videofileclip载入视频
    mvFiles=[VideoFileClip(path+'\\'+str(e)+'.mp4') for e in L]
    return mvFiles

def main(inpath,outMvNmae):
    mvTemp=getFileList(inpath)
    final_clip = concatenate_videoclips(mvTemp)
    final_clip.to_videofile(outMvNmae+'.mp4', fps=24, remove_temp=False)
    
path='E:\\视频处理'
name='combine'
main(path,name)