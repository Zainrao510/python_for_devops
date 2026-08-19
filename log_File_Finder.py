import os

folder="logs" # Specify the folder path where you want to search for log files

try:
    if not os.path.exists(folder):
        print("Folder does not exist,")
        exit()
    for filename in os.listdir(folder):
        if filename.endswith(".log"):
            file_path = os.path.join(folder, filename)
            print(f"Found log file: {file_path}")

            with open(file_path, 'r') as file:
                for line in file:
                    if "ERROR" in line:
                        print(f"Error found in {filename}: {line.strip()}")
                    

except FileNotFoundError:
    print(f"Folder '{folder}' not found.")  
except Exception as e:
    print(f"An error occurred: {e}")                        