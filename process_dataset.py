#coding=utf-8
import os
import numpy as np
import shutil
val_root_path = os.path.join(os.path.abspath("."),"data","files", "val")
print(val_root_path)
partial = 0.2
def get_val(path):
    #train_dir = path + "/train"
    train_dir = os.path.join(path,"train")
    file_names = os.listdir(train_dir)
    print("The total_number of labels are: %d"%(len(file_names)))
    for name in file_names:
        name = name.encode("utf-8").decode("utf-8")
        print(name)
        train_sub_dir = os.path.join(train_dir,name)
        pic_names = os.listdir(train_sub_dir)
        val_pic_names = np.random.choice(pic_names, int(len(pic_names)*partial))
        # create validate file
        val_label_name = os.path.join(val_root_path, name)
        os.mkdir(val_label_name)
        # copy files into validate folder
        for val_pic_name in val_pic_names:
            val_pic_name = val_pic_name.encode("utf-8").decode("utf-8")
            shutil.copy2(os.path.join(train_sub_dir,val_pic_name), os.path.join(val_label_name,val_pic_name))
        for val_pic_name in val_pic_names:
            val_pic_name = val_pic_name.encode("utf-8").decode("utf-8")
            try:
                os.remove(os.path.join(train_sub_dir,val_pic_name))
            except :
                print("Can not remove the file %s"%(os.path.join(train_sub_dir,val_pic_name)))
        print("finish letter %s"%(name))


if __name__=="__main__":
    get_val(os.path.join(os.path.abspath("."),"data","files"))