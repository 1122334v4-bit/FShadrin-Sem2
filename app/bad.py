import subprocess

def run(cmd):
    return subprocess.call(cmd, shell=True)

def calc(expr):
    return eval(expr)