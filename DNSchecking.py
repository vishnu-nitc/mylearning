import os
file = open("open.txt","r").read().split('\n')
for line in file :
        response = os.system("ping -c 1 " + line + " |& tee -a output.txt" )
        if response == 0:
                 fh   = open("out.csv","a")
                 fh.write(line+",yes" + "\n")
                 fh.close()
        else:
                 fh   = open("out.csv","a")
                 fh.write(line+",no" + "\n")
                 fh.close()
