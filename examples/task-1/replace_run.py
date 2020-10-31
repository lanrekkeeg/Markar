import subprocess
file = open("unittest_.py", 'r').read().strip()
file = file.replace("<<DIR>>", "compute_sum.cpp")
print(subprocess.run(["python", "unittest_.py"], capture_output=True))