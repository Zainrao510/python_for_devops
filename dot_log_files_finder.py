from pathlib import Path

location =Path(r"D:\semester 6\devops\python")
"""
if not location.exists():
    print("location not exists:")

for file in location.glob("*.log"): #.glob() Python mein files/folders ko pattern ke basis par search karne ke liye use hota hai.
    print(file)
    content=file.read_text()
    print(f"{content} of the {file} ")
    with file.open("r") as f:
        for line in f:
           if "ERROR" in line:           
            print(f"ERROR find in the following line ::: {line} of the file: {file}")
"""
"""
for file in location.rglob("*.log"): #Recursive Search: Agar subdirectories ke andar bhi .log files find karni hain:
    print(file)
"""

try:
    for file in location.rglob("*.log"):
        content=file.read_text()
        for line in content.splitlines():
            if "ERROR" in line:
                print(f"ERROR: {line} : 'find in the file : '{file}")
except FileNotFoundError:
    print("Logs directory not found.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print(f"Something went wrong: {e}")                        
    