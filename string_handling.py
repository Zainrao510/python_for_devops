text = "DevOps with Python"

print(len(text))          # Length
print(text.upper())       # Uppercase
print(text.lower())       # Lowercase
print(text.strip())       # Remove spaces
print(text.replace("Python", "Linux"))
print(text.split())       # Convert into list

##error handling in logs 

log = "ERROR: Database connection failed"

if "ERROR" in log:
    print("Error found!")

##DevOps example: Log filtering

log = """
INFO: Server started
INFO: User logged in
ERROR: Database connection failed
WARNING: Disk space is low
"""

for line in log.splitlines():
    if "ERROR" in line:
        print(line)    