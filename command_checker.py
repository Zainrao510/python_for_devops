import subprocess
import shutil

def command_checker(command, version="--version"):
    if shutil.which(command) is None:
        print(f"{command} is not installed: ")
        return
    try:
        result = subprocess.run([command,version], capture_output=True, text=True, check=True )
        print(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        print(f"{command} command is failed: ")
        print(e.stderr)

command_checker("python") 
command_checker("git")   
command_checker("docker")    