# this program will be run from the command line. It should take a single argument, a command. The option -o should also be possible.
from rich.console import Console
from rich import print
import sys
import os
import argparse
from pathlib import WindowsPath
console = Console()

# program can either be run "loc {command}" or "loc -o {command}"

def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-o", "--open", action="store_true")
    parser.add_argument("command", type=str)
    args = parser.parse_args()
    # to run this, you need to have which installed. I use github's version.
    location = os.popen(f"where {args.command}").read()
    if f"INFO: Could not find files for the given pattern(s)." in location:
        print(f"Command '{args.command}' not found")
        sys.exit(1)
    
    location = WindowsPath(location.strip()) 
    
    if args.open:
        os.system(f"explorer {location.parent.absolute()}")
    else:
        print(f"[link=file://{location.parent.absolute()}]{location.parent.absolute()}[/link]")
    
main()