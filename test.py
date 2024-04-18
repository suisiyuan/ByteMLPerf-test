import os
import sys
import subprocess


def main():
    os.chdir(sys.path[0])
    print("currrent dir: {}".format(os.getcwd()))

    os.chdir("byte_micro_perf")

    workload_list = []
    for file in os.listdir("workloads"):
        workload_list.append(file[:-5])
    workload_list.sort()
    
    for op in workload_list:
        cmd = "python3 ./launch.py --hardware_type GPU --vendor_path ../vendor_zoo/NVIDIA/A100-PCIe.json --task {}".format(op)
        print(cmd)
        subprocess.run(cmd, shell=True)
        print("done...\n")

if __name__ == '__main__':
    main()