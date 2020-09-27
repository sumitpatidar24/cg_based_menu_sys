#! /usr/bin/python4
print("Content-type: text/html")
print()

import subprocess as sp
import webbrowser as wb
import cgi

inpl=cgi.FieldStorage()

uinp=inpl.getvalue("user_input")

if "date" in uinp:
        out=sp.getoutput("date")
        print(out)


elif "calender" in uinp:
        out=sp.getoutput("cal")
        print(out)

elif "docker" in uinp:
        out="sudo docker run -d -i -t --name {} ubuntu".format(uinp.split()[1])
        op=sp.getstatusoutput(out)
        if op[0]==0:
                print("hurray")
        else:
                print(op[1])
elif "add user" in uinp:
        out="sudo adduser {}".format(uinp.split()[2])
        op=sp.getstatusoutput(out)
        if op[0]==0:
                print("user addedd succesfully")
        else:
                print(op[1])
else:
        out="sudo {}".format(uinp)
        op=sp.getstatusoutput(out)
        if op[0]==0:
                print("worked somehow")
        else:
                print(op[1])
