import os

for folder_name,subfolders,files in os.walk("/Users/rahulprakash/summerPy"):
    print("Current folder: "+folder_name)
    for subfolder in subfolders:
        print("==>Current Subfolder: "+subfolder)
    for file in files:
        print("---->"+file)