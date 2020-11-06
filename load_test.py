import multiprocessing
import subprocess
def worker():
    #worker function
    out = subprocess.call(["python","markar.py","submit"])
    print("Output: {}".format(out))

if __name__ == '__main__':
    jobs = []
    for i in range(80):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()