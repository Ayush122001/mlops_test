import os
ac = os.popen("cat a.txt")
a = ac.read()
a = a.rstrip()
if float(a) < 85:
  os.system("rm -rf *.h5")
  os.system("python3 train1.py")
  
if float(a) < 85:
  os.system("rm -rf *.h5")
  os.system("python3 train2.py")
  
  
if float(a) < 85:
  os.system("rm -rf *.h5")
  os.system("python3 train3.py")
