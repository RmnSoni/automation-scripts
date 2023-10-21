import os
import subprocess

path = '/home/gasher/Downloads/'

listed = os.listdir(path)

accepted_formats = [ '.epub', '.mobi', '.awz' ]
subprocess.run(["notify-send", "Movings ebooks to library"])
for item in listed:
    if any(item.endswith(ext) for ext in accepted_formats):

        try:
            result = subprocess.check_output(
                ["calibredb", "add", "--automerge=new_record", path + item],
                universal_newlines=True,
                stderr=subprocess.STDOUT)
            print(f"Added '{item}' to Calibre library. Result:\n{result}")
            os.remove(path + item)
        
        except subprocess.CalledProcessError as e:
            print(f"Error adding '{item}' to Calibre library. Error message:\n{e.output}")
            


'''
bash alias
alias libsync="python ~/Desktop/coding/automation-scripts/library_sync.py"
'''
