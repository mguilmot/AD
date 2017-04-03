### User functions

from AD_Classes import UserName, UserGroup

def txt2lst(text=""):
    '''
        Converts text from our input fields to lists.
        Expects a text string as input, returns a list as output
        
        Example:
        text="hello\nworld\nThis\nIs\nMe"
        print(txt2lst(text))
        ==> ['hello','world','This','Is','Me']
    '''

    lst = filter(None,text.split("\n"))
    return [item.strip() for item in lst if len(item)>1]
    
def userInfo(lst=[],request="info",resulttxtFile="output.txt",resultcsvFile="output.csv",csv=False):
    '''
        Returns AD information about a provided AD username
        Expects:
        - list of users (list lst)
        - the requested information (string request)
            * info
            * groups
        - if output should be csv (bool csv)
        Returns a tuple with 
        - Success or error
        - the output text
    '''
    
    text=""
    
    def headers_csv():
        return "username,displayname,lastset,lastlogin,status,homedirectory,loginscript\n"
    def writeplain(text="",mode="a",filename="output.txt"):
        writeFile(text=text,filename=filename,mode=mode)
    def writecsv(header=False,text=text,mode="a",filename="output.csv"):
        if header==False:
            writeFile(text=text,filename=filename,mode="a")
        else:
            writeFile(text=headers_csv(),filename=filename,mode="w")

    success=0
    success_dicts=[]
    success_lsts=[]
    errors=[]
    
    # Getting user data
    for user in lst:    
        userobj = UserName(user)
        if userobj.get_displayname() == "No Data":
            errors.append(user)
        else:
            success+=1
            if request=="info":
                dictDetails=userobj.get_details()
                success_dicts.append(dictDetails)
            elif request=="groups":
                lstGroups = userobj.get_groupmembership()
                success_lsts.append(lstGroups)
    
    # Did our function succeed
    if success>0:
        succeeded=True
        # Create the new files and add data
        if csv == True:
            writecsv(header=True,filename=resultcsvFile,mode="w")
            if success_dicts:
                for dictDetails in success_dicts:
                    writecsv(text=convertToText(dictDetails=dictDetails,csv=True),filename=resultcsvFile,mode="a")
        else:
            writeplain(text="",filename=resulttxtFile,mode="w")
            if success_dicts:
                for dictDetails in success_dicts:
                    writeplain(text = convertToText(dictDetails=dictDetails,csv=False)+"\n",filename=resulttxtFile,mode="a")

        if len(errors)>0:
            resulttext = ", but with errors."
        else:
            resulttext = "without errors."
    else:
        succeeded=False
        resulttext = ": user name(s) do not exist."
    
    # For debugging
    # print("errors:",errors)
    # print("success:",success)
    
    # Return the results
    return (succeeded,resulttext)
    
def groupInfo(lst=[],request="members",resulttxtFile="output.txt"):
    '''
        Returns AD information about a provided AD group
        Expects:
        - list of AD groups (list lst)
        - the requested information (string request)
            * members
        Returns a tuple with 
        - Success or error
        - the output text
    '''
    errors=[]
    success=[]
    success_lsts=[]
    
    def groupheader(groupName=""):
        return "Members for group: " + str(groupName) + "\n"
    
    if request == "members":
        for groupName in lst:
            groupObj = UserGroup(groupName)
            groupObj_name = groupObj.get_gname()
            if groupObj_name == "IncorrectLine":
                errors.append(groupName)
            else:
                success.append(groupObj_name)
                success_lsts.append(list(groupObj.get_members()))

    if len(success)>0:
        if len(errors)>0:
            text = ", but with errors."
        else:
            text = "without errors."
        succeeded = True
        writeFile(text="",filename=resulttxtFile,mode="w")
        for num,lstGroups in enumerate(success_lsts):
            name = str(success[num])[13:].split(',')[0]
            writeFile(text=groupheader(name),filename=resulttxtFile,mode="a")
            writeFile(text=convertToText(lstGroups=lstGroups) + "\n",filename=resulttxtFile,mode="a")
    else:
        succeeded = False
        text = "Groupname(s) do not exist."
                
    return (succeeded,text)

def convertToText(dictDetails={},lstGroups=[],csv=False):
    '''
        Converts the dictionary or list to readable text.
        returns this text so it can be written to file.
    '''
    text = ""
    if dictDetails:
        if csv == False:
            line = "\n"
            text = "User: " + dictDetails["username"].upper()
            text+= line
            text+= "Homedir: " + dictDetails["homedirectory"]
            text+= line
            text+= "Loginscript: " + dictDetails["loginscript"]
            text+= line
            text+= "Name: " + dictDetails["displayname"]
            text+= line
            text+= "Password last set: " + str(dictDetails["lastset"])
            text+= line
            text+= "Last login: " + str(dictDetails["lastlogin"])
            text+= line
            text+= "Enabled: " + str(dictDetails["status"])
            text+= line
        else:
            text = dictDetails["username"].upper() + ","
            text+= dictDetails["displayname"] + ","
            text+= str(dictDetails["lastset"]) + ","
            text+= str(dictDetails["lastlogin"]) + ","
            text+= str(dictDetails["status"]) + ","
            text+= dictDetails["homedirectory"] + ","
            text+= dictDetails["loginscript"] + "\n"
    else:
        for group in lstGroups:
            text += str(group)[9:-1].split(',')[0][3:]
            text += "\n"
    return(text)

def writeFile(text="",filename="output.txt",mode="a"):
    '''
        Writes requested information to chosen filename.
        Expects:
        - The text to write (string text)
        - The filename to write to (string filename, default="output.txt")
    '''
    f = open(filename,mode)
    f.writelines(text)
    f.close()
    return

