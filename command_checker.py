import subprocess
import shutil

def command_checker(command, version="--version"):
    if shutil.which(command) is None:  #shutil.which() = "Ye command mere system mein available hai? Agar hai to kahan hai?"shutil.which() ka kaam hai check karna ke koi command/program system ke PATH mein available hai ya nahi.
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