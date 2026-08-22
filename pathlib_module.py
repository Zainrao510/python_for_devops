from pathlib import Path #pathlib Python mein files aur directories ke paths ko manage karne ka modern aur clean way hai.
import shutil
"""
path=Path("backup") /"server" / "logs"

print(path)
"""
"""
current= Path.cwd() #cwd current working directory
print(current)


print(Path.home())


path= Path("server.log")
print(path)

"""

###############  Check File Exists  #################
"""
file=Path("server.log")
if file.exists():
    print("file exists:")
else:
    print("file not exists:")

"""
###############   File Hai Ya Folder? ##############    
"""
path=Path("server.log")

if path.is_file():
    print("this is a file:")
if path.is_dir():
    print("it is a directory:")
"""

###############  7. Folder Create Karna ################
"""
folder=Path("CREATED")
folder.mkdir()
"""
#Nested directories:
"""
folder=Path("backup/server/logs")
folder.mkdir(parents=True, exist_ok=True) #exist_ok = true mean if path already can be exists
"""

##############  8. File Create Karna  #############
"""
file = Path("test.txt")
file.touch()
"""

############### 9. File Read Karna ⭐##################
"""
file=Path("output.txt")

content = file.read_text()
print(content)
"""
#############  10. File Write Karna ###################
"""
file = Path("output.txt")

file.write_text("write the new txt ") #Path.write_text() normally existing content replace karta hai.

"""

###############  11. File Append  ####################
"""
file = Path("output.txt")

with file.open("a") as file:
    file.write("\n add the new line")
"""

############### 12. File Delete  ####################
"""
file =Path("test.txt")

file.unlink() #unlink() file delete karta hai.
"""
#folder = Path("backup")
#folder.rmdir() #rmdir() sirf empty directory remove karega.

#Agar folder ke andar files hain to shutil.rmtree() use karna better hai
#shutil.rmtree("backup")

#################   13. Path Join ⭐ ################
"""
path=Path("backup") / "server" / "logs"
print(path)

"""
###############  14. File Name  #################
"""
file= Path("backup/server/error.log")

print(file.name)
"""

################  15. File Stem ###############
"""
file=Path("server.log")
print(file.stem) #stem = filename without extension.
"""

##############33  16. File Extension   ##############
"""
file=Path("server.log")
print(file.suffix)  # ouput .log
"""

################# 17. Parent Directory ################
"""
file = Path("backup/server/error.log")

print(file.parent) # output backup\server
"""
###########  dot_log_files_finder.py example
