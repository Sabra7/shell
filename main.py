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

        user_input = input().strip().split()
        if not user_input:
            continue

        cmd_name = user_input[0]
        tokens = user_input
        arg_w = user_input[1:]
        arg_t = " ".join(arg_w)
        builtin = ["type","exit","echo"]
# exit fun is done
# TODO: use sys.exit(int(arg_t)) - handle empty arg
        if cmd_name == "exit": break
            
# echo fun is done
        elif cmd_name == "echo": print(" ".join(arg_w))
            
# type fun is working
        elif cmd_name == "type":
            if arg_t in builtin: print(f"{arg_t} is a shell builtin")
                
            elif path := shutil.which(arg_t): print(f"{arg_t} is {path}")
                
            else: print(f"{arg_t}: not found")
                
# execute fun working< i think in windows isn't will work well
        elif execute_command(cmd_name): subprocess.run(tokens)

# to get back ans let user know the command not found
        else: print(f"{cmd_name}: command not found")



if __name__ == "__main__":
    main()
