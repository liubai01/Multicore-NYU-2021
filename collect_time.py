# Steps to create the dataset:

# Download and build parsec benchmark
# wget http://parsec.cs.princeton.edu/download/3.0/parsec-3.0.tar.gz
# tar -xzf parsec-3.0.tar.gz
# source env.sh

import subprocess
import pandas as pd


# Extracting the real execution time of a parsec program from stdout
def get_real_time(cmd_output):
    for line in cmd_output:
        line = line.decode("ascii")
        if line.__contains__('real'):
            line = line.split("\t")
            real_time = line[1]
            m, s = real_time.split('m')
            s, seconds = s.split('s')
            real_time = int(m) * 60 + float(s)
            break
    return real_time


repeat_time = 10
data = []


def construct(pkg_name):
    package_name = pkg_name
    input_size = ['simsmall', 'simmedium', 'simlarge']
    threads = [1, 2, 4, 8, 16, 32]

    for i in range(repeat_time):
        for thread in threads:
            for size in input_size:
                print("repeat-{}, thread-{}, pkg-{}, size-{}".format(i, thread, pkg_name, size))
                cmd = subprocess.Popen('parsecmgmt -a run -p ' + package_name + ' -n ' + str(thread) + ' -i ' + size, shell=True, stdout=subprocess.PIPE)
                cmd.wait()
                real_time_seconds = get_real_time(cmd.stdout.readlines())
                print("time_cost: {:.3f}".format(real_time_seconds))
                data.append([pkg_name, size, thread, real_time_seconds])


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
                'Thread',
                'Time'
            ]
        )

        df.to_csv('data_time.csv')

if __name__ == "__main__":
    main()
