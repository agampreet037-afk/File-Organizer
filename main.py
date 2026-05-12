import os
import shutil

  
# DEFINING A SOURCE FOLDER WHERE USER PUTS INPUT
source_folder = input("Enter Path: ")


# DEFINING EXTENSIONS OF FILES
file_types = {
"Images" : [".jpg",".jpeg",".png"],
"Videos" : [".mp4",".mkv"],
"Documents" : [".pdf",".docx",".txt",".odt",".xlsx"],
"Music": [".mp3",".wav",".m4a",".m4b"],
"Applications": [".exe",".msi"]
}
# CREATING FOLDERS FOR VARIOUS TYPES OF FILES
def createfolders():
   folders = ["Images","Documents","Videos","Music","Others"]
   for folder in folders:
      folder_path = os.path.join(source_folder,folder)
        
      if not os.path.exists(folder_path):            
         os.mkdir(folder_path)
         print(f"Created the folder: {folder_path}")
      else:
       print(f"{folder_path} is already present")
       
       
          

createfolders() 
 
# GETTING FILE INFORMATION         
def getfiles():
   files = os.listdir(source_folder)
   print(f"The files present in the source folder are:\n {files}")           
   for file in files:
      name,extension = os.path.splitext(file)
      extension = extension.lower()
      
      src = os.path.join(source_folder,file)
      if os.path.isfile(src):
        found = False               
        for key,value in file_types.items():
          if extension in value:
            dest = os.path.join(source_folder,key,file)
            shutil.move(src,dest)
            found = True           
            print(f"{file} moved to {key}")
            break
        if not found:              
          others_dest = os.path.join(source_folder,"Others",file)
          shutil.move(src,others_dest)
          print(f"{file} moved to Others")
     
          
          
              
getfiles()                   
     

        
      
        
        
        
        

                      

                 
    

