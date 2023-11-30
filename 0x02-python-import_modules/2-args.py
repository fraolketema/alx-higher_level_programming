#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg_len = len(sys.argv)
    
    print(f"{arg_len - 1} {'argument' if arg_len == 2 else 'arguments'}:")
    
    [print(f"{i}: {sys.argv[i]}") for i in range(1, arg_len)]
