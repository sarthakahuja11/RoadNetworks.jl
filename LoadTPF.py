#!/usr/bin/env python3

import subprocess
import time
import shutil

#--
target_folder = "/home/sarthak11/Desktop/TPF"
excluded = ["HP_TOOLS"]
#--
#use lsusb and lsblk for excluded directory
def get_mountedlist():
    return [(item.split()[0].replace("├─", "").replace("└─", ""),
             item[item.find("/"):]) for item in subprocess.check_output(
            ["/bin/bash", "-c", "lsblk"]).decode("utf-8").split("\n") if "/" in item]

def identify(disk):
    command = "find /dev/disk -ls | grep /"+disk
    output = subprocess.check_output(["/bin/bash", "-c", command]).decode("utf-8")
    if "usb" in output:
        return True
    else:
        return False

done = []
while True:
    mounted = get_mountedlist()
    new_paths = [dev for dev in get_mountedlist() if not dev in done and not dev[1] == "/"]
    valid = [dev for dev in new_paths if (identify(dev[0]), dev[1].split("/")[-1]  in excluded) == (True, False)]
    for item in valid:
        target = target_folder+"/"+item[1].split("/")[-1]
        try:
            shutil.rmtree(target)
        except FileNotFoundError:
            pass
        shutil.copytree(item[1], target)
    done = mounted

#Alternative C++ approach
"""
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main () 
{
  string line;
  ifstream file ("/media/sarthak11/Tanmay/Sarthak/Rnp.txt");
  ofstream file1 ("/home/sarthak11/Desktop/Local2.txt"); 
  if (file.is_open())
  {
    while ( getline (file,line) )
    {
	//cout << line << '\n';
	file1<<line<<'\n';
    }
    file.close();
    file1.close();
  }

  else cout << "Unable to open file"; 

  return 0;
}"""
