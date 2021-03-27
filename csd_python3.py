#write a python program to print the last line of a file
def lastline(fname):
    with open(fname) as file:
        for line in (file.readlines() [-1:]):
            print(line,end='')
if __name__=='__main__':
    fname="csd_python1.txt"
    lastline(fname)
        
