import os
import shutil
import datetime

"""
source = r"D:\semester 6\devops\python"
destination = r"D:\semester 6\devops\python\backup"

try:
    if os.path.exists(destination):
        shutil.rmtree(destination)  # Remove the existing destination folder and its contents

    shutil.copytree(source, destination)  # Copy the source folder to the destination
    print(f"Successfully copied {source} to {destination}")


except FileNotFoundError:
    print(f"Source folder '{source}' does not exist.")

except Exception as e:
    print(f"Error occurred while removing the destination folder: {e}")        

"""

def backup_files(source, distination):
    today = datetime.date.today()
    backup_filename = os.path.join(distination, f"backup_{today}.tar.gz")
    shutil.make_archive(backup_filename.replace('.tar.gz', ''), 'gztar', source)


source =r"D:\semester 6\devops\python"
distination =r"D:\semester 6\devops\python\backups"

backup_files(source, distination)

