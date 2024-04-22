import os
import sys
import subprocess

def main():
    os.chdir(sys.path[0])
    os.chdir("byte_micro_perf")
    print("currrent dir: {}".format(os.getcwd()))

    workload_list = []
    workload_dir = "workloads"
    for file in os.listdir(workload_dir):
        workload_list.append(file[:-5])
    workload_list.sort()
    print(workload_list)
    
    for op in workload_list:
        cmd = "python3 ./launch.py --hardware_type GPU --vendor_path ../vendor_zoo/NVIDIA/A100-PCIe.json --task {}".format(op)
        print(cmd)
        subprocess.run(cmd, shell=True)
        print("done...\n")

if __name__ == '__main__':
    main()