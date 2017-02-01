#!/usr/bin/env python2
#!encoding=utf-8

""" A simple script to build order list.

The style of Index.md must like this:

```
# Index of pwntools

'Some title and introduction'

---

About pwntools
Installation
from pwn import *
......
```
"""

def main():
    file_name = "Index.md"
    begin_index = -1
    
    with open(file_name, "r") as fp:
        lines = fp.readlines()
    
    # find begin position.
    for i, line in enumerate(lines):
        if line == "---\n":
            begin_index = i + 2

    # check find result
    if begin_index == -1:
        print("Find index failed.")
        return
    
    for index, i in enumerate(range(begin_index, len(lines))):
        index_text = str(index + 1)
        if len(index_text) == 1:
            # turn '1, 2, 3' into '01, 02, 03'
            index_text = "0" + index_text 
    
        lines[i] = index_text + ". " + lines[i]
    
    with open(file_name, "w") as fp:
        fp.writelines(lines)

if __name__ == '__main__':
    main()
