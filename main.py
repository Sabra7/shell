import sys
import shutil
import os

def main():
    while True:
        sys.stdout.write("$ ")
        pass
        command = input()

        if command == "exit":
            break

        elif command.startswith("echo "):
            print(command[5:])

        elif command.startswith("type "):
            cmd_type = command[5:]
            if cmd_type in ["type","exit","echo"]:
                print(f"{cmd_type} is a shell builtin")
            elif path := shutil.which(cmd_type):
                print(f"{cmd_type} is {path}")

            else:
                print(f"{command[5:]}: not found")

        else:
            print(f"{command}: command not found")





if __name__ == "__main__":
    main()
