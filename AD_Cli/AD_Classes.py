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

File use:
    input: in.txt in script directory. 1 username or AD group per line
    output: out.txt in script directory for usernames, 1 file per group for AD groups

"""
import sys
sys.dont_write_bytecode = True

 ### Import needed modules
 ### Use this in your python script to be able to use these classes
try:
    from pyad import *
    import pyad.adquery
except:
    err="Please read the requirements. Install the correct modules first."
    raise ImportError(err)
    
### Building the classes
class UserName(object):
    def __init__(self,username):
        self.givenuser=username
        try:
            self.username=pyad.aduser.ADUser.from_cn(self.givenuser)
        except:
            self.username=""
    def get_username(self):
        return self.givenuser.upper()
    def get_displayname(self):
        try:
            result=self.username.get_attribute("displayName")[0]
            if result=="":
                result="No Data"
            return result
        except:
            return "No Data"
    def get_lastset(self):
        try:
            return self.username.get_password_last_set()
        except:
            return "No data"
    def get_lastlogin(self):
        try:
            return self.username.get_last_login()
        except:
            return "No data"
    def IsEnabled(self):
        ''' 
            Returns if user is enabled or not.
            AD attribut userAccountControl returns
            512	Enabled Account
            514	Disabled Account
            544	Enabled, Password Not Required
            546	Disabled, Password Not Required
            66048	Enabled, Password Doesn't Expire
            66050	Disabled, Password Doesn't Expire
            66080	Enabled, Password Doesn't Expire & Not Required
            66082	Disabled, Password Doesn't Expire & Not Required
            262656	Enabled, Smartcard Required
            262658	Disabled, Smartcard Required
            262688	Enabled, Smartcard Required, Password Not Required
            262690	Disabled, Smartcard Required, Password Not Required
            328192	Enabled, Smartcard Required, Password Doesn't Expire
            328194	Disabled, Smartcard Required, Password Doesn't Expire
            328224	Enabled, Smartcard Required, Password Doesn't Expire & Not Required
            328226	Disabled, Smartcard Required, Password Doesn't Expire & Not Required
        '''
        enabledlist=[512,544,66048,66080,262656,262688,328192,328224]
        try:
            result=self.username.get_attribute("userAccountControl")[0]
            if result in enabledlist:
                return True
            else:
                return False
        except:
            return False
    def get_groupmembership(self):
        try:
            result=""
            groups=sorted(self.username.get_attribute("memberOf"))
            for i in range(len(groups)):
                #print(groups[i])
                group=groups[i].split(",")[0]
                gname=group.split("CN=")[1]
                result+=str(gname)+"\n"
            return result
        except:
            return "None"
    def get_homedirectory(self):
        try:
            result=self.username.get_attribute("homeDirectory")[0]
        except:
            result="No data"
        return result
    def get_loginscript(self):
        try:
            result=self.username.get_attribute("scriptPath")[0]
        except:
            result="No data"
        return result
    def get_details(self):
        dictDetails={}
        dictDetails["username"]=self.get_username()
        dictDetails["displayname"]=self.get_displayname()
        dictDetails["homedirectory"]=self.get_homedirectory()
        dictDetails["loginscript"]=self.get_loginscript()
        dictDetails["lastset"]=self.get_lastset()
        dictDetails["lastlogin"]=self.get_lastlogin()
        dictDetails["status"]=self.IsEnabled()
        return dictDetails
    def get_attributes(self):
        try:
            lst=""
            att=self.username.get_allowed_attributes()
            for i in range(len(att)):
                lst+=str(att[i])+"\n"
            return lst
        except:
            return "No data"

class UserGroup(object):
    def __init__(self,gname):
        try:
            self.gname=pyad.adgroup.ADGroup.from_cn(gname)
        except:
            self.gname="IncorrectLine"
    def get_gname(self):
        return self.gname
    def get_members(self):
        try:
            return pyad.adgroup.ADGroup.get_members(self.gname,True,True)
        except:
            return "No data"
        
class FileData(object):
    def __init__(self,filename="in.txt",writefile="output.txt"):
        self.filename=filename
        self.writefile=writefile
        try:
            file=open(self.filename,"r")
            file.close()
        except:
            err="File in.txt does not exist.\nEither create it or provide your own filename to 'FileData()'."
            print(err)
            a=input("\nPress enter to continue")
            raise ImportError(err)
    def readlines(self):
        file=open(self.filename,"r")
        filedata=file.read().split("\n")
        data=[]
        for line in filedata:
            if len(line)>0:
                data.append(line.strip("\n"))
        file.close()
        return data
    def writelines(self,data):
        file=open(self.writefile,"w")
        file.write(data)
        file.close()

'''
# Examples below:    
#=====================

## Display info from 1 list of users 'usernames'
### Variables
#usernames=["evlil","eocbt"]
# for i in range(len(usernames)):
#     test=UserName(usernames[i])
#     print(test.get_details(),"\n")
#     #print(test.get_groupmembership())

## Display memberships of 1 group
# Gp=UserGroup("A-Mak-Adm")
# GpUsr=Gp.get_members()
# for i in range(len(GpUsr)):
#     usr=GpUsr[i]
#     usr=str(usr)
#     usr=(usr[12:].split(",")[0])
#     user=UserName(usr)
#     print(usr,"-",user.get_displayname())

# # Display memberships of a series of groups from file in.txt
# f=open("in.txt","r")
# lines=f.read().split("\n")
# f.close()
# for line in lines:
#     if len(line)>0: # only handle non-empty lines
#         print("Memberships for",line)
#         line.strip("\n")
#         Gp=UserGroup(line)
#         try:
#             GpUsr=Gp.get_members()
#             for i in range(len(GpUsr)):
#                 usr=GpUsr[i]
#                 usr=str(usr)
#                 usr=(usr[12:].split(",")[0])
#                 user=UserName(usr)
#                 print(usr,"-",user.get_displayname())
#             print()
#         except:
#             print("InvalidLine")

'''



