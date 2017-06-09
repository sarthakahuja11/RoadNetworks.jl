import os
def rename(directory):
i = 0
for file_name in os.listdir(directory):
      new_file_name = str(i) + '.jpg'
      old_file_name = file_name
os.rename(old_file_name, new_file_name)
i += 1
PATH = os.path.abspath('/Users/maxdeutsch/Desktop/nvidia/udacity_data')
rename(PATH)
