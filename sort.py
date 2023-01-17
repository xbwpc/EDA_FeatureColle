import sys

if __name__=="__main__":
    if len(sys.argv)<2:
        print("Oops, no text file specified.")
        exit(0)
    
    f = open(sys.argv[1],"r")
    lines = f.readlines()
    f.close()
    
    new_lines = []
    for line in lines:
        l = line.strip(" \r\n")
        if l not in new_lines:
            new_lines.append(l)
    new_lines.sort()
    
    f = open(sys.argv[1],"w",newline='\n')
    for line in new_lines:
        f.write(line+"\n")
    f.close()
