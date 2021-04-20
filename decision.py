import os
ac = os.popen("cat a.txt")
a = ac.read()
a = a.rstrip()
if a < 80:
  os.system("python3 train1.py")
