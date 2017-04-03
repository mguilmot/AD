import os, webbrowser

def openUrl(url='http://www.google.com'):
    webbrowser.open_new_tab(url)
    return

def openFile(filename='README.txt'):
    os.startfile(filename)
    return

def returnIniSettings(filename='settings.ini'):
    '''
        Expects a plain text ini file as argument. 
        Default filename = settings.ini
        returns every setting in format key=value via a dictionary
        Ignores every non 'key=value' line
    '''

    import os
    if not os.path.isfile(filename):
        err = "Error with file: " + filename + ". It does not exist."
        raise FileExistsError(err)

    settingsDict = {}

    def gen_readfile(f):
        '''
            Generator which returns line per line.
            Expects an open("file") object as input
        '''
        for line in f:
            if line.startswith("#") or line.startswith("[") or line.startswith("\n") or "=" not in line:
                continue
            else:
                yield line

    with open(filename,"r") as f:
        for line in gen_readfile(f):
            key = line.split("=")[0]
            value = line.split("=")[1].strip("\n")
            settingsDict[key]=value

    return settingsDict