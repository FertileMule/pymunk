import sys
import os

def main():
    os.system('''sphinx-build -b html ../docs/src/source ../docs/html''')
    #os.system('''sphinx-build -E -b html ../docs/src/source ../docs/html''')

if __name__ == "__main__":
    sys.exit(main())
    
    
    
    