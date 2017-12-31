#opening scaffold root file
scaffold_root_path_file = open("C:\\python27\\scaffold_root_path.txt","r");
scaffold_root_path = scaffold_root_path_file.read()[0:-1];
scaffold_root_path_file.close();


#Input for root file or project Name
project_path = raw_input("Enter project path = ");

#route setup
set_up_file = open(scaffold_root_path+"\\index.txt","w");
set_up_file.write(project_path);
set_up_file.close();