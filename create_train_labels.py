from glob import glob
import functools

imgs_path = sorted(glob("C:/Users/Daniel_Lin/Desktop/caffe_image/Googlenet_Raw_Data/img_*.jpg"))
imgs_name = map(lambda path: path[path.rfind("\\")+1 : ], imgs_path)
categories = map(lambda path: path[path.index("_", 60)+1 : path.rfind("_")], imgs_path)
numeric_categories = map(lambda cate: 1 if cate == "hat" else 0, categories)

with open("train.txt", "w") as f:
    for name, cate in zip(imgs_name, numeric_categories):
        f.write("{} {}\n".format(name, cate))

f.close()

print(len(list(imgs_name)))
print(len(list(numeric_categories)))

# with open("train.txt", "w") as f:


print("hello")