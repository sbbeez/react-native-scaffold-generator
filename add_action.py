#Add actions to the action file

#Imports for adding action
import re

#opening scaffold root file
scaffold_root_path_file = open("C:\\python27\\scaffold_root_path.txt","r");
scaffold_root_path = scaffold_root_path_file.read()[0:-1];
scaffold_root_path_file.close();

#route setup
set_up_file = open(scaffold_root_path+"\\index.txt","r");
rn_project_root_path = set_up_file.read();
set_up_file.close();

class ActionScaffold:
    def __init__(self,action):
        self.action = action;

    def getTypeFormat(self):
        array = re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', self.action)
        formatted_type = ""
        for words in array:
            formatted_type+=words.lower();
            if words == array[-1]:
                formatted_type+="_type"
                break;
            formatted_type+="_"
        return formatted_type;


#inputs for adding actions
screen_name = raw_input("Enter screen name = "); #Get screen Name to which action is to be added

action_name = raw_input("Enter Action name = "); #Get Action name

comment_for_action = raw_input("Enter some comment for the action = ");

#---------------------------Types--------------------------------
#creating instance of class for data processing
action_scaffold_generator = ActionScaffold(action_name);
#Getting formatted type string for creating type in types.js
formatted_type = action_scaffold_generator.getTypeFormat();

#exporting type for the action

#open types file for adding type
action_types_file = open(rn_project_root_path+"actions\\types.js","a");
#appending the type to types.js
action_types_file.write("\nexport const "+formatted_type.upper()+" = "+'"'+formatted_type+'";');
action_types_file.close(); #closing the types.js file

#---------------------------Actions---------------------------------
action_file = open(rn_project_root_path+"actions\\"+screen_name+"Actions.js","a");
action_sample_file = open(scaffold_root_path+"\\actionsGeneratorJsfiles\\ActionsSample.txt","r");
action_sample = action_sample_file.readlines();

words_array = [];
temp_words_array = [];
temp_action_content_array =[];
action_content = ""

for lines in action_sample:
    words_array = lines.split();
    for word in words_array:
        print(word)
        if word == "ACTION_NAME":
            word = action_name[0].lower() + action_name[1:]+"Action";
        if word == "ACTION_TYPE,":
            word = formatted_type.upper()+",";
        temp_words_array.append(word);
    temp_action_content_array.append(temp_words_array);
    temp_words_array = [];
    words_array = [];

for lines in temp_action_content_array:
    for words in lines:
        action_content+=words;
        action_content+=" "
    action_content+="\n"

print(action_content)
action_file.write("\n\n"+action_content)
