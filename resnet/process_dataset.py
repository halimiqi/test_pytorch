import numpy
import os

split_char = "\t"
def read_all_name_labels(txt_files):
    my_dict = {}
    with open(txt_files, "r") as f:
        for line in f:
            list = line.strip().split(split_char)
            my_dict[list[0]] = list[1]

    return my_dict

if __name__ == '__main__':
    my_dict = read_all_name_labels("tiny-imagenet-200/val/val_annotations.txt")
    for key, value in my_dict.items():
        # print(key)
        # print(value)
        # cmd_str = "mkdir -p " + "tiny-imagenet-200/val/"+value
        # os.system(cmd_str)
        cmd_str = "mv tiny-imagenet-200/val/images/" + key + " " + "tiny-imagenet-200/val/" + value
        os.system(cmd_str)
