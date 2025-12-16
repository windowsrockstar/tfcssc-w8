import subprocess

def run_command(cmd):
    # DANGER: Passing 'shell=True' allows command injection attacks.
    # If 'cmd' comes from a user, they could run malicious commands.
    subprocess.run(cmd, shell=True)