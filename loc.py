# this program will be run from the command line. It should take a single argument, a command. The option -o should also be possible.
import rich
from rich.console import Console
from rich import print
import sys
import os
import argparse

console = Console()

# program can either be run "loc {command}" or "loc -o {command}"

def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("command", type=str, help="The command to run")
    parser.add_argument("-o", "--open", action="store_true", help="Open the command in the default program")
    args = parser.parse_args()
    # to run this, you need to have which installed. I use github's version.
    location = os.popen(f"which {args.command}").read()
    if f"no {args.command} in" in location:
        print(f"Command '{args.command}' not found")
        sys.exit(1)
    
    # this is not great, I think this also only works on the C:/ drive. Will possibly fix later.
    location = os.path.abspath(os.path.dirname(location)[2:])
    
    if args.open:
        os.system(f"explorer {location}")
    else:
        print(f"[link=file://{location}]{location}[/link]", end="")
    
main()