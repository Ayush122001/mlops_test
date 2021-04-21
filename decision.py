import os
ac = os.popen("cat a.txt")
a = ac.read()
a = a.rstrip()
accuracy = a
while float(accuracy) < 60:
  if float(a) < 60:
    os.system("rm -rf *.h5")
    os.system("python3 train1.py")
    ac = os.popen("cat a.txt")
    a = ac.read()
    a = a.rstrip()
    accuracy = a
    if float(accuracy) > 60:
      break
  
  if float(a) < 60:
    os.system("rm -rf *.h5")
    os.system("python3 train2.py")
    ac = os.popen("cat a.txt")
    a = ac.read()
    a = a.rstrip()
    accuracy = a
    if float(accuracy) > 60:
      break
  
  
  if float(a) < 60:
    os.system("rm -rf *.h5")
    os.system("python3 train3.py")
    ac = os.popen("cat a.txt")
    a = ac.read()
    a = a.rstrip()
    accuracy = a
    if float(accuracy) > 60:
      break
  
  if float(a) < 60:
    os.system("rm -rf *.h5")
    os.system("python3 train4.py")
    ac = os.popen("cat a.txt")
    a = ac.read()
    a = a.rstrip()
    accuracy = a    
    if float(accuracy) > 60:
      break
  
  if float(a) < 60:
    os.system("rm -rf *.h5")
    os.system("python3 train5.py")
    ac = os.popen("cat a.txt")
    a = ac.read()
    a = a.rstrip()
    accuracy = a    
    if float(accuracy) > 60:
      break
print("Final Accuracy = ", accuracy)
