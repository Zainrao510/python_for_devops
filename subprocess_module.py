import subprocess


#subprocess.run(["python", "--version"]) #Ye command ek subprocess create karta hai aur python ke version ko print karta hai. Ye command system ke PATH environment variable me search karta hai. Agar python installed hai to ye command successfully execute hoga aur python ka version print karega. Agar python installed nahi hai, to ye command error throw karega.
#subprocess.run(["dir"], shell=True) #Ye command ek subprocess create karta hai aur current directory ke files aur directories ko list karta hai in long format. Ye command system ke PATH environment variable me search karta hai. Agar dir command available hai to ye command successfully execute hoga aur files aur directories ka detailed list print karega. Agar dir command available nahi hai, to ye command error throw karega.
"""
result = subprocess.run(["python", "--version"], capture_output=True, text=True) #Ye command ek subprocess create karta hai aur python ke version ko capture karta hai. Ye command system ke PATH environment variable me search karta hai. Agar python installed hai to ye command successfully execute hoga aur python ka version capture karega. Agar python installed nahi hai, to ye command error throw karega.  capture_output=True ka matlab hai ke command ka output capture kiya jayega aur text=True ka matlab hai ke output ko string format me return kiya jayega. Agar aapko output ko print karna hai to aap print(result.stdout) use kar sakte hain, jahan result subprocess.run() ka return value hai.   
#print(result.stdout) #Ye command python ke version ko print karta hai jo ke result variable me capture hua hai. Agar python installed hai to ye command successfully execute hoga aur python ka version print karega. Agar python installed nahi hai, to ye command error throw karega.     

print("OUTPUT:")
print(result.stdout) # .stdout attribute me command ke output messages capture hote hain. Agar command successfully execute hoti hai to ye output message return karega. Agar command error throw karti hai to ye empty string return karega.

print("ERROR:")
print(result.stderr) # .stderr attribute me command ke error messages capture hote hain. Agar command successfully execute hoti hai to ye empty string return karega. Agar command error throw karti hai to ye error message return karega.

print("RETURN CODE:")
print(result.returncode) # .returncode attribute me command ke return code capture hota hai. Agar command successfully execute hoti hai to ye 0 return karega. Agar command error throw karti hai to ye non-zero value return karega.

if result.returncode == 0:
    print("Command successful")
else:
    print("Command failed")
"""

"""
result =subprocess.run(["git", ""], capture_output=True, text=True , check=True ) #check=True ka matlab hai ke agar command error throw karti hai to ye exception raise karega. Agar command successfully execute hoti hai to ye output message return karega. Agar command error throw karti hai to ye exception raise karega aur aapko error message print karna hoga. Agar aapko output ko print karna hai to aap print(result.stdout) use kar sakte hain, jahan result subprocess.run() ka return value hai.

print(result.stdout)
"""
"""
result = subprocess.run("dir" , shell=True) #shell=True ka matlab hai ke ye command shell ke through execute hogi. Agar aapko output ko print karna hai to aap print(result.stdout) use kar sakte hain, jahan result subprocess.run() ka return value hai.
print(result.stdout) # .stdout attribute me command ke output messages capture hote hain. Agar command successfully execute hoti hai to ye output message return karega. Agar command error throw karti hai to ye empty string return karega.

"""
