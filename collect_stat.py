# Steps to create the dataset:

# Download and build parsec benchmark
# wget http://parsec.cs.princeton.edu/download/3.0/parsec-3.0.tar.gz
# tar -xzf parsec-3.0.tar.gz
# source env.sh

import subprocess
import pandas as pd


def parse_output_data():
    with open("output.txt", "r") as f:
        lines = f.readlines()

    d = []

    for line in lines[2:]:
        values = line.split(",")
        event_value = values[0]
        event_name = values[2]
        if event_name.startswith('instructions'):
            d.append(float(event_value)) # tot instr.
            d.append(float(values[5])) # instructions per second
        elif event_name.startswith('cache-misses'):
            d.append(float(event_value))
            d.append(float(values[5]))
        elif event_name.startswith('branch-misses'):
            d.append(float(values[5])) # branch misses
        else:
            d.append(float(event_value))

    return d


repeat_time = 15
data = []


def construct(pkg_name):
    package_name = pkg_name
    input_size = ['simsmall', 'simmedium', 'simlarge']

    thread = 1
    for i in range(repeat_time):
        for size in input_size:
            print(i, pkg_name, size)
            cmd = subprocess.Popen('perf stat -o output.txt --field-separator=, -e branch-instructions,branch-misses,cache-misses,cache-references,cycles,instructions,cpu-clock,page-faults,L1-dcache-loads,L1-icache-load-misses,LLC-load-misses -- parsecmgmt -a run -p ' + package_name + ' -n ' + str(thread) + ' -i ' + size, shell=True, stdout=subprocess.PIPE)
            cmd.wait()
            ret = parse_output_data()
            data.append([pkg_name, size] + ret)


def main():
    modules = [
        'blackscholes',
        'bodytrack',
        'canneal',
        'facesim',
        'fluidanimate',
        'freqmine',
        'streamcluster',
        'swaptions',
        'vips'
    ]

    for module in modules:
        print(module)
        construct(module)

    df = pd.DataFrame(
        data=data,
        columns=[
            'Name',
            'Size',
            'branch-instructions',
            'branch-misses in %',
            'L3-cache-misses',
            'L3-cache-miss-rate in %',
            'L3-cache-references',
            'cpu-cycles',
            'total-instructions',
            'IPC',
            'cpu-clock',
            'page-faults',
            'L1-data-cache-loads',
            'L1-instruction-cache-load-misses',
            'LLC-load-misses'
        ]
    )

    df.to_csv('stat_single_thread.csv')

if __name__ == "__main__":
    main()
