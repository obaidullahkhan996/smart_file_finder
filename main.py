import os

search_name = input("Enter file name to search: ")
folder_path = input("Enter folder path to search: ")
if not os.path.isdir(folder_path):
    print("Invalid folder path!")
    exit()


found = 0
for root, folders, files in os.walk(folder_path):


     folders[:] = [folder for folder in folders if folder != ".git"]

   
     for file in files:
          if search_name.lower() in file.lower():
               print("Location:", os.path.join(root, file))
               found += 1
               

if found == 0:
     print("no files found")
else:
     print("Total files found:", found)
     print("search term:", search_name)
     print("total matches:", found)
     print("search completed succesfully")                  
        
         