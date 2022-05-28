from torch.utils.data import Dataset
from PIL import Image #图片操作
import os

from pytorch.getdata import Mydata

image_path="G:\\college\\Python\\pytorch\\dataset\\pic\\final.png"
image=Image.open(image_path)
image.size
image.show()

dir_path = "dataset/pic"
image_path_list=os.listdir(dir_path)#将地址下文件制成列表
image_path_list[0]

root_dir = "dataset"
label_dir = "pic"
path=os.path.join(root_dir,label_dir)#路径拼接

root_dir = "dataset"
pic_label_dir="pic" #文件名
pic_dataset = Mydata(root_dir,pic_label_dir)

setu_label_dir="setu"
setu_dataset = Mydata (root_dir,setu_label_dir)
total_dataset=pic_dataset+setu_dataset      #拼接
img,lab=total_dataset[3]
img.show()