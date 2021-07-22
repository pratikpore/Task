import subprocess

def execute(command):
    com = command.split()
    a = subprocess.run(com,capture_output=True,text=True)
    if "create" in com:
        return a.returncode
    else:
        return a.stdout

