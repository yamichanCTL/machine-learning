from torch.utils.data import Dataset
from PIL import Image  #图片操作
import os       #关于系统

class Mydata(Dataset):
    def __init__(self, root_dir, label_dir):  #label是图片上一级名称
        self.root_dir=root_dir  #指定全局变量，供后面使用  根目录
        self.label_dir=label_dir
        self.path=os.path.join(self.root_dir,self.label_dir)#根目录+label名
        self.image_path=os.listdir(self.path)   #所有图片制成列表

    def __getitem__(self, index):
        image_name=self.image_path[index]   #取图片文件名
        image_item_path=os.path.join(self.root_dir,self.label_dir,image_name)   #每张图路径
        image=Image.open(image_item_path)
        label=self.label_dir
        return image,label
    def __len__(self):
        return len(self.image_path)     #列表元素个数


