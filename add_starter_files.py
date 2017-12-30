#Copy paste the src folder, which has the format
import shutil
import os

#scaffold root path
root_path_file = open("D:\\d\\python\\rn-scaffold\\index.txt","rb");
root_path = root_path_file.read()[0:-2];
root_path_file.close();
os.remove(root_path[0:-3] + "App.js");
shutil.copy("D:\\d\\python\\rn-scaffold\\App.js",root_path[0:-3])
shutil.copytree("D:\\d\\python\\rn-scaffold\\src",root_path);
