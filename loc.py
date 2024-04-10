# this program will be run from the command line. It should take a single argument, a command. The option -o should also be possible.
from rich import print
import sys
from subprocess import Popen, PIPE
import argparse
from pathlib import WindowsPath
import os

# program can either be run "loc {command}" or "loc -o {command}"
# you can also get python modules' locations by running "loc -py {module}"

def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-o", "--open", action="store_true")
    parser.add_argument("-py", "--python", action="store_true")
    parser.add_argument("command", type=str)
    args = parser.parse_args()
    if args.python:
        try:
            location = WindowsPath(__import__(args.command).__file__).parent.absolute()
            if args.open:
                os.system(f"explorer {location}")
            else:
                print(f"[link=file://{location.as_uri()}]{location}[/link]")
            
            
        except ImportError:
            print(f"Module '{args.command}' not found")
            sys.exit(1)
    
    else:
        # to run this, you need to have which installed. I use github's version.
        location = Popen(f"where {args.command}".split(), stdout=PIPE, stderr=PIPE).communicate()[0].decode()
        if not location:
            print(f"Command '{args.command}' not found")
            sys.exit(1)

        location = WindowsPath(location.strip()) 
        
        if args.open:
            os.system(f"explorer {location.parent.absolute()}")
        else:
            print(f"[link=file://{location.parent.absolute().as_uri()}]{location.parent.absolute()}[/link]")
        
main()