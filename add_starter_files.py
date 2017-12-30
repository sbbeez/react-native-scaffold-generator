#Copy paste the src folder, which has the format
import shutil
import os

#opening scaffold root file
scaffold_root_path_file = open("C:\\python27\\scaffold_root_path.txt","r");
scaffold_root_path = scaffold_root_path_file.read()[0:-1];
scaffold_root_path_file.close();

#scaffold root path
root_path_file = open(scaffold_root_path+"\\index.txt","rb");
root_path = root_path_file.read()[0:-2];
root_path_file.close();
os.remove(root_path[0:-3] + "App.js");
shutil.copy(scaffold_root_path+"\\App.js",root_path[0:-3])
shutil.copytree(scaffold_root_path+"\\src",root_path);
