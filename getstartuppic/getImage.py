#coding:utf-8
import getpass
import os, sys, re,shutil,time, ctypes
import cv2
#import Image
from PIL import Image
import datetime
#import win32gui,win32con,win32api

userName=getpass.getuser()

# path = "D:\\Image\\"; //存储图片的文件夹
# while True:
	# file = os.listdir(path);   #打开存储图片文件夹中的图片目录
	# filepath = path + random.choice(file); #随机选取某张图片，建立绝对地址
	# ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 0) # 设置桌面壁纸
	# time.sleep(30*60); #睡眠半个小时
 
# def setWallpaperFromBMP(imagepath):
    # k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    # win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "2") #2拉伸适应桌面,0桌面居中
    # win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
    # win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,imagepath, 1+2)

# def setWallPaper(imagePath):
    # """
    # Given a path to an image, convert it to bmp and set it as wallpaper
    # """
    # bmpImage = Image.open(imagePath)
    # newPath = StoreFolder + '\\mywallpaper.bmp'
    # bmpImage.save(newPath, "BMP")
    # setWallpaperFromBMP(newPath)
    
    
# bmp 转换为jpg
def jpgToBmp(fileName):
        im = Image.open(fileName)
        im.save(newFileName)

path=r"C:/Users/"
path=path+str(userName)+"/appdata/Local/Packages/"


dirList=os.listdir(path)
# 返回的是一个list，该list的一项代表一个文件名

reMatch=re.compile(r'.*Microsoft.Windows.ContentDeliveryManager_.*')


dirList=os.listdir(path)
reMatch=re.compile(r'.*Microsoft.Windows.ContentDeliveryManager_.*')
for item in dirList:
    if(reMatch.match(str(item))):
        path+=str(item)

path+="/LocalState/Assets/"
dirList=os.listdir(path)

destiPath="E:/开机图片".decode("utf-8").encode("gbk")
#destiPath="E:/startPic"
#destiPath=destiPath.decode("utf-8")
# 如果桌面不存在“开机图片”这个文件夹，则创建
if(not os.path.exists(destiPath)):
    os.mkdir(destiPath)
for fileItem in dirList:
    filePath=os.path.join(path,fileItem)
    fileName,fileExtend=os.path.split(fileItem)
    print(filePath)
    dstpic=destiPath+"/"+str(fileExtend)+".jpg"
    if(os.path.isfile(dstpic)):
        print("exist pic")
    else:
        shutil.copy(filePath,dstpic)
        img=cv2.imread(dstpic)
        
        sp1 = img.shape
        if(sp1[0] == 1080):
            print("set wallpaper")
            # newPath = dstpic.replace('.jpg', '.bmp')
            # im = Image.open(dstpic)
            # im.save(newPath)

            print dstpic
            ctypes.windll.user32.SystemParametersInfoW(20, 0, dstpic.decode("gbk"), 0) # 设置桌面壁纸
            #setWallPaper(dstpic)
            
