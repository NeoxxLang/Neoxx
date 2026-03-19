import sys
from nxx.nxx import run_file

def main():
    if len(sys.argv) < 2:
        print("Usage: nxxc <file.nx/.nxx>")
        return

    run_file(sys.argv[1])

if __name__ == "__main__":
    main()
