import os
from dotenv import load_dotenv


#print(os.getcwd()) #getcwd() method returns the current working directory of a process.
#print(os.listdir()) #listdir() method returns a list containing the names of the entries in the directory given by path.
#items=os.listdir(r"D:\semester 6\devops\python") #for spacific directory
#for item in items:
#    print(item) #print() method prints the specified message to the console or other standard output device.

#os.chdir(r"D:\semester 6\devops\python") #chdir() method changes the current working directory to the specified path. r is used to indicate that the string is a raw string, which means that backslashes are treated as literal characters and not as escape characters.
#print(os.getcwd()) #getcwd() method returns the current working directory of a process.

#os.mkdir("new_folder") #mkdir() method creates a new directory with the specified name.
#os.rmdir("new_folder") #rmdir() method removes the specified directory.
"""
os.makedirs("new_folder/sub_folder") #makedirs() method creates a new directory and any necessary parent directories with the specified name.
os.removedirs("new_folder/sub_folder") #removedirs() method removes the specified directory and any empty parent directories.
os.makedirs("new_folder/sub_folder", exist_ok=True) #exist_ok parameter is used to avoid raising an error if the directory already exists. If set to True, the function will not raise an error if the directory already exists. If set to False, the function will raise a FileExistsError if the directory already exists.
"""

#############   Check Karna File/Folder Exist Karta Hai Ya Nahi ##################3

"""
if os.path.exists("new_folder"): #exists() method returns True if the specified path exists, otherwise it returns False.
    print("Directory exists")
else:
    print("Directory does not exist")

if os.path.exists("server.log"): #exists() method returns True if the specified path exists, otherwise it returns False.
    print("File exists")
else:
    print("File does not exist")
"""

######################    File Hai Ya Directory? #####################

"""
if os.path.isfile("server.log"): #isfile() method returns True if the specified path is an existing regular file, otherwise it returns False.
    print("This is a file")
else:
    print("File does not exist")    

if os.path.isdir("new_folder"): #isdir() method returns True if the specified path is an existing directory, otherwise it returns False.
    print("This is a directory")  
else:
    print("Directory does not exist")     
"""
        
########################   File Rename Karna   ####################

#os.rename("server.log", "new_server.log") #rename() method renames the specified file or directory to the specified new name.

######################3   File Delete Karna   ####################
"""
try:
    os.remove("newfile.py")#remove() method removes the specified file.
    print("file removed: ")
except FileNotFoundError:
    print("file not found: ")  

"""

#####################  Folder delete karne ke liye: ##############
#os.rmdir() sirf empty directory remove karta hai.
"""
try:
    os.rmdir("abc")#rmdir() method removes the specified directory.
    print("directory removed: ")
except FileNotFoundError:
    print("directory not found: ")
"""

#################   Environment Variables    #################
"""
load_dotenv()

database_url = os.getenv("DATABASE_URL")
api_key = os.getenv("API_KEY")
environment = os.getenv("APP_ENV")
path = os.getenv("PATH") #.getenv() method returns the value of the environment variable with the specified name. If the environment variable does not exist, it returns None.

print(environment)
print("Database URL:", database_url)
print("API Key:", api_key)
print("PATH:", path)
#print(os.environ)
#print(os.environ.get("PATH"))
"""

####################  OS Information  ####################
"""
print("Operating System:", os.name) #name attribute returns the name of the operating system dependent module imported. The following names have currently been registered: 'posix', 'nt', 'os2', 'ce', 'java', 'riscos'.
print("cpu count:", os.cpu_count()) #cpu_count() method returns the number of CPUs in the system.
"""
"""
path = os.path.join("backup", "server", "logs") #os.path.join() method joins one or more path components intelligently. It returns a string representing the concatenation of the path components with the appropriate separator for the operating system.

print(path)
"""

##################  File Extension ####################
#DevOps mein tum is tarah sirf .log files identify kar sakte ho.

filename = "server.log"
name , file_extension = os.path.splitext(filename) #os.path.splitext() method splits the pathname into a pair (root, ext) such that root + ext == pathname, and ext is empty or begins with a period and contains at most one period. It returns a tuple containing the root and the extension of the file.
print("File Name:", name)
print("File Extension:", file_extension)    



