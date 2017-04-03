"""
@author: Mike Guilmot - mguilmot+nospam@gmail.com

Requires: 
    pyad
    pywin32

installs: 
    pywin32:
        https://sourceforge.net/projects/pywin32
    pyad:
        pip install https://github.com/zakird/pyad/archive/master.zip

Displays group memberships, loops through a list or a file.
Default: filename = in.txt
Output: 'groupname'.txt
groupnames = a list of usernames, ex groupnames=["adgroup1","adgroup2"]
"""

### Variables <-- the only thing we should worry about
use_file=True
groupnames=["ant site admins","a-mak-adm","a-tra-adm"] # not used if file is used

### Import needed modules
try:
    import AD_Classes
except:
    err="AD_Classes.py missing"
    raise ImportError(err)
try:
    from pyad import *
except:
    err="Please read the requirements. Install the correct modules first."
    raise ImportError(err)

### Functions
def WriteGroupData(groupnames):
    global writefile
    orig=writefile
    for i in range(len(groupnames)):
        users=""
        group=AD_Classes.UserGroup(groupnames[i])
        data=group.get_members()
        writefile=str(groupnames[i]) + ".txt"
        for j in range(len(data)):
            string=str(data[j])
            string=string.split(",")[0][12:]
            users+=string
            users+="\n"
        # let's discard groups that do not exist, else write the file
        check=users.strip("\n")
        if len(check)>1:
            members=AD_Classes.FileData(writefile=writefile)
            members.writelines(users)
    writefile=orig

def PrintGroupData(groupnames):
    for i in range(len(groupnames)):
        text=""
        group=AD_Classes.UserGroup(groupnames[i])
        text+="Members for " + str(groupnames[i]) + "\n"
        data=group.get_members()
        for j in range(len(data)):
            string=str(data[j])
            string=string.split(",")[0][12:]
            text+=string
            text+="\n"
        print(text)
    return text

# Display info from file, output to files
try:
    test=filename
except:
    filename="in.txt"

try:
    test=writefile
except:
    writefile="output.txt"

if use_file:
    try:
        data=AD_Classes.FileData(filename)
    except NameError:
        data=AD_Classes.FileData()
    groupnames=data.readlines()
    WriteGroupData(groupnames)
else:
    PrintGroupData(groupnames)

