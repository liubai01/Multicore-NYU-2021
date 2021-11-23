import os
import subprocess

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
    cmd = subprocess.Popen('parsecmgmt -a build -p ' + module, shell=True)
    cmd.wait()
