import os #os module provides a way of using operating system dependent functionality like reading or writing to the file system.

print(os.getcwd()) #getcwd()method returns the current working directory of a process.
print(os.listdir()) #listdir() method returns a list containing the names of the entries in the directory given by path.
print(os.system('mkdir new_folder')) #system() method allows you to run shell commands from within Python.
print(os.system('rmdir new_folder')) #rmdir() method removes the specified directory.

print(os.system('dir')) #dir command lists the files and directories in the current directory on Windows.

print(os.system('sysinfo')) #sysinfo command displays detailed information about the system configuration on Windows.

command ="mkdir new_folder" #mkdir command creates a new directory with the specified name.
command ="rmdir new_folder" #rmdir command removes the specified directory.
command ="dir" #dir command lists the files and directories in the current directory on Windows.
command ="sysinfo" #sysinfo command displays detailed information about the system configuration on Windows.

def execute_command(command):
    return os.system(command) #system() method allows you to run shell commands from within Python.

#execute_command("dir")
