import subprocess
file = open("unittest_.py", 'r').read().strip()
out = subprocess.call(['python', "unittest_.py"])
if out:
    print("Error in  Compiling...")
print("Output:",out)
#file = file.replace("<<DIR>>", "compute_sum.cpp")
#print(subprocess.run(["python", "last_test.py"], capture_output=True))