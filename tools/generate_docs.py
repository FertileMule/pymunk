import sys
import os

def main():
    os.system('''sphinx-build -b html ../docs/src ../docs/html''')

if __name__ == "__main__":
    sys.exit(main())
    
