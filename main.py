import sys
import shutil
import os
import subprocess

def execute_command(c):
    for d in os.get_exec_path():
        if os.access(fullpath := os.path.join(d, c), os.X_OK):
            return fullpath

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        user_input = input()
        if not user_input:
            continue

        command = user_input
        cmd_name = command
        file_name = cmd_name.split()[0]
        tokens = cmd_name.split()

        if cmd_name == "exit":
            break

        elif command.startswith("echo "):
            print(command[5:])

        elif cmd_name.startswith("type "):
            cmd_type = cmd_name[5:]

            if cmd_type in ["type","exit","echo"]:
                print(f"{cmd_type} is a shell builtin")

            elif path := shutil.which(cmd_type):
                print(f"{cmd_type} is {path}")

            else:
                print(f"{cmd_name[5:]}: not found")

        elif execute_command(file_name):
            subprocess.run(tokens)

        else:
            print(f"{cmd_name}: command not found")



if __name__ == "__main__":
    main()
