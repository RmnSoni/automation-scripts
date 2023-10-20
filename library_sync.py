import os
import subprocess
print ("Hello World")

path = '/home/gasher/Downloads/'

listed = os.listdir(path)

accepted_formats = [ '.epub', '.mobi', '.awz' ]

for item in listed:
    if any(item.endswith(ext) for ext in accepted_formats):

        # subprocess.Popen( 'calibredb add "'+path+item+'"', shell=True)
        try:
            result = subprocess.check_output(["calibredb", "add", "--automerge=new_record", path + item], universal_newlines=True, stderr=subprocess.STDOUT)
            print(f"Added '{item}' to Calibre library. Result:\n{result}")
            os.remove(path + item)
        except subprocess.CalledProcessError as e:
            print(f"Error adding '{item}' to Calibre library. Error message:\n{e.output}")
