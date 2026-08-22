import subprocess

"""
result = subprocess.run(["git","status"], capture_output=True, text=True) #Ye command ek subprocess create karta hai aur git status command ka output capture karta hai.

if result.returncode == 0:
    print("Command successful")
    print(result.stdout) # .stdout attribute me command ke output messages capture hote hain. Agar command successfully execute hoti hai to ye output message return karega. Agar command error throw karti hai to ye empty string return karega.
else:
    print("Command failed")
    print(result.stderr) # .stderr attribute me command ke error messages capture hote hain. Agar command successfully execute hoti hai to ye empty string return karega. Agar command error throw karti hai to ye error message return karega.
"""

"""
try:
    result=subprocess.run(["git", "status"], capture_output=True, text=True, check=True)
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print("Command failed with return code:", e.returncode)
    print("Error message:", e.stderr)    
"""
try:
    result = subprocess.run(["docker", "--version"], capture_output=True, text=True, check=True)
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(e.returncode)
    print("Docker is not available")    
    print(e.stderr)

