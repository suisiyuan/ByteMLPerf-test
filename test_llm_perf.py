import os
import sys
import subprocess

def main():
    os.chdir(sys.path[0])
    os.chdir("byte_infer_perf")
    print("current dir: {}".format(os.getcwd()))
    
    workload_list = []
    workload_dir = "llm_perf/workloads"
    for file in os.listdir(workload_dir):
        if (not file.endswith(".json")):
            continue
        workload_list.append(file[:-5])
    workload_list.sort()
    print("workloads list: ")
    print(workload_list)

    for op in workload_list:
        cmd = "python3 llm_perf/launch.py --task {} --hardware_type GPU".format(op)
        print(cmd)
        subprocess.run(cmd, shell=True)
        print("done...\n")

if __name__ == '__main__':
    main()