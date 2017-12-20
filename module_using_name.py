import sys

if __name__ == '__main__':
    print("This module is using by itself")
else:
    print("This module is using by",__name__)


print(sys.path)