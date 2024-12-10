# Version 1
# go to project directory that store lots of kicad project
# ask user to select kicad project
#   - display all kicad projects and let user to choose one
# ask user to input serial number
#   - input serial number one by one
#   - input txt / csv / json file to input all serial numbers
# generate all necessary files
# generate csv / json file that contain info of all components that are included in different projects, such as name, serial number, path of its footprint...

# Version 2
# develop plugin of KiCad to import those files, can use it through KiCad

import os

def dir_contain_extension_file(dir, extension):
  for entry in os.scandir(dir):
    if entry.is_file() and entry.name.endswith(extension):
      return True
  return False

os.system("clear")
dir_path = os.path.dirname(__file__)
print(dir_path)
os.chdir(dir_path)
prjs = []

for entry in os.scandir("."):
  if entry.is_dir():
    if dir_contain_extension_file(entry.path, ".kicad_pcb"):
      prjs.append(entry)

# check the number of project
print(f"Found {len(prjs)} projects!")
for i in range(len(prjs)):
  print(f"{i+1}. {prjs[i].name}")
print("Which project that you want to import the data of components from JLCSC to (input index number): ", end="")
index = int(input()) - 1
# check the range of index number
project = prjs[index]

print("There are 2 methods that you can use to input the serial number of components.")
print("1. Input the serial number in terminal")
print("2. Input a file (.txt/.csv/.json) that contain the serial number of all components")
print("Which method that you want to use (input index number): ", end="")
index = int(input())
# check the range of index number

components = ""
match index:
  case 1:
    print("Input the serial number in the format of (C123 C456 C789 ...): ", end="")
    components = input()
    # check format
  case 2:
    ... 
    # read the input file

os.chdir(project.path)
os.system(f"JLC2KiCadLib {components} -dir KiCad_lib -model_dir model_dir -footprint_lib footprint_lib -symbol_lib_dir symbol_lib_dir -symbol_lib symbol_lib")

# print("Input serial number: ", end="")

# serial_num = input()

# os.system("cd /Users/justin/Library/CloudStorage/OneDrive-Personal/Documents/Program")
# os.system(f"JLC2KiCadLib {serial_num} -dir KiCad_lib -model_dir model_dir -footprint_lib footprint_lib -symbol_lib_dir symbol_lib_dir -symbol_lib symbol_lib")

# C3029422 C24112 C1337258