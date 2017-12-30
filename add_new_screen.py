#Screen scaffold generator for react native using python


#opening scaffold root file
scaffold_root_path_file = open("C:\\python27\\scaffold_root_path.txt","r");
scaffold_root_path = scaffold_root_path_file.read()[0:-1];
scaffold_root_path_file.close();

#route setup
set_up_file = open(scaffold_root_path+"\\index.txt","r");
rn_project_root_path = set_up_file.read();
set_up_file.close();

#Screen file creation
screen_name = raw_input("enter screen name  = "); #Screen name

reducer_key = raw_input("enter reducer key = "); #Reducer key for the screen

#creating the screen file, actions file and reducer file
scaffold_file = open(scaffold_root_path+"\\screenGeneratorJsfiles\\screenScaffold.txt","r");
scaffold_content = scaffold_file.readlines();
#closing screen scaffold file
scaffold_file.close();

#temp arrays for processing
temp_scaffold_content = []; #after changing the sampleScaffold to particular screen content, each line of screen is appended.
temp_words_array = []; #after changing the sampleScaffold(after each word is processed), each word is appended
temp_words = []; #before changing the sampleScaffold, each word is stored as an array
screen_file_content = "" #Final screen content to be pasted

for lines in scaffold_content:
    temp_words = lines.split();
    for word in temp_words:
        if word == "SCREEN_NAME":
            word = screen_name;
        if word == "state.KEY;":
            word = "state."+reducer_key+";";
        if word == "{})(SCREEN_NAME);":
            word = "{})("+screen_name+");"
        temp_words_array.append(word);
    temp_scaffold_content.append(temp_words_array);
    temp_words_array = [];
    temp_words = [];

for lines in temp_scaffold_content:
    for words in lines:
        screen_file_content+=words;
        screen_file_content+=" "
    screen_file_content+="\n"

createScreenFile  =  open(rn_project_root_path+"screens\\"+screen_name+".js","w+");
createScreenFile.write(screen_file_content);
createScreenFile.close();
#export Generated screen
screenExportFile = open(rn_project_root_path+"screens\\index.js","a");
screenExportFile.write('\nexport { default as '+screen_name+' } from "./'+screen_name+'";')
screenExportFile.close();

#---------------------------------Actions---------------------------------------#
#Creating action files for specified screens
createActionFile =  open(rn_project_root_path+"actions\\"+screen_name+"Actions.js","w+");
#closing action file
createActionFile.close();

#~~~Adding to index.js file of actions folder to export all actions~~
actionsExportFile = open(rn_project_root_path+"actions\\index.js","a");
actionsExportFile.write('\nexport * from "./'+screen_name+'Actions";');
actionsExportFile.close();


#---------------------------------Reducers---------------------------------------#
#Creating Reducer file and wiring to redux
createReducerFile =  open(rn_project_root_path+"reducers\\"+screen_name+"Reducer.js","w+");
reducer_file_scaffold = open(scaffold_root_path+"\\reducerGeneratorJsfiles\\reducerSample.txt","r");
createReducerFile.write(reducer_file_scaffold.read());
reducer_file_scaffold.close();
createReducerFile.close();
