import shutil # This module provides a higher level interface for file operations, including copying and archiving files and directories. It is part of the Python standard library and is used for tasks such as copying files, moving files, and removing directories.
#shutil ka naam Shell Utilities se aaya hai.Iska main purpose filesystem par high-level operations perform karna hai.
"""
#shutil module ke kuch important functions ye hai:
#shutil.copy("new_server.log", "backups/new_server.log") #Ye function ek file ko copy karta hai from source (src) to destination (dst). Agar destination ek directory hai, to file ko us directory me copy kiya jata hai with the same name.  
#shutil.copy2("output.txt", "backups/output.txt") #Ye function bhi file ko copy karta hai, lekin ye original file ke metadata (jaise timestamps) ko bhi preserve karta hai. Agar aapko file ke saath uske attributes bhi chahiye, to ye function use karein.
#shutil.copytree("backups", "destination_folder") #Ye function ek directory aur uske saare contents ko recursively copy karta hai from source to destination. Agar destination folder already exist karta hai, to ye error throw karega.
#shutil.move("data.txt", "moved_files/data.txt") #Ye function ek file ya directory ko move karta hai from source to destination. Agar destination ek existing file hai, to ye us file ko overwrite kar dega.
#shutil.move("new_server.log", "server.log") #Ye function ek directory ko move karta hai from source to destination. Agar destination folder already exist karta hai, to ye error throw karega.
#shutil.rmtree("destination_folder") #Ye function ek directory aur uske saare contents ko recursively delete karta hai. Ye function use karte waqt caution rakhein, kyunki ye permanently delete kar deta hai.
"""

################# Disk Usage ⭐ DevOps mein system monitoring ke liye useful: ############
"""
total, used, free = shutil.disk_usage("/") #Ye function disk usage ko check karta hai. Ye function ek tuple return karta hai jisme total space, used space aur free space ke values hote hain in bytes.
print("total:", total // (2**30), "GiB") #Total disk space ko GiB me convert karke print karta hai.
print("used:", used // (2**30), "GiB") #Used disk space ko GiB me convert karke print karta hai.
print("free:", free // (2**30), "GiB") #Free disk space ko GiB me convert karke print karta hai.

"""
################ shutil.which() ⭐ Check karna ke koi command system mein available hai ya nahi:  #############
"""
python =shutil.which("python") #Ye function ek command ke executable path ko return karta hai. Agar command available nahi hai, to ye None return karega. Ye function system ke PATH environment variable me search karta hai.  
print(python) #Ye print karega python command ka executable path, jaise /usr/bin/python ya C:\Python39\python.exe, agar python installed hai to. Agar python installed nahi hai, to ye None print karega.   

"""



