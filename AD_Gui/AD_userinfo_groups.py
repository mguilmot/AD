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

Displays group memberships about AD users, loops through a list or a file.
Default: filename = in.txt
Output: output.txt
usenames = a list of usernames, ex usernames=["aduser1","aduser2"]

set specific filenames with
filename="filename.txt" for input
writefile="writefile.txt" for output
use none or both!
"""
### Variables <-- the only thing we should worry about
use_file=True
usernames=["aduser1","aduser2"] # not used if file is used
show_groups=False

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
def UserData(usernames):
    data=""
    line="\n"
    for i in range(len(usernames)):
        UN=AD_Classes.UserName(usernames[i])
        dictDetails=UN.get_details()
        data+="User: " + str(dictDetails["username"])
        data+="\nGroup memberships:\n"
        data+=UN.get_groupmembership()
        data+="\n"
    return data

# Display info from 1 list of users 'usernames'
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
        data=AD_Classes.FileData(filename,writefile)
    except NameError:
        data=AD_Classes.FileData()
    usernames=data.readlines()
    data.writelines(UserData(usernames))
else:
    print(UserData(usernames))



