try:
    with open("server.log", "r") as file:
        errors=[]
        for line in file:
            if "error" in line.lower(): #lower() method converts the string to lowercase, making the search case-insensitive.
                errors.append(line.strip())

    with open("error_log.txt", "w") as file:
        for error in errors:
            file.write(error + "\n")          
            



except FileNotFoundError:
    print("File not found")

except Exception as e:
    print(f"Something went wrong: {e}")    


