import shutil
import datetime
import os

def backup_files(source, distination):
    today = datetime.date.today()
    backup_filename = os.path.join(distination, f"backup_{today}.tar.gz")
    shutil.make_archive(backup_filename.replace('.tar.gz', ''), 'gztar', source)


source =r"D:\semester 6\devops\python"
distination =r"D:\semester 6\devops\python\backups"

backup_files(source, distination)