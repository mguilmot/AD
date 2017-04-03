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
        returns every setting in format key=value as a dictionary
        Default line in ini file example:
        setting=value
        Returned dictionary example:
        {'setting':'value'}        
    '''

    settingsDict = {}

    try:
        f = open(filename,'r')
        fulltext = f.readlines()
        f.close()
    except:
        '''
            File we try to read does not exist
            Chose not to raise an error, as not everything might need an ini file
        '''
        settingsDict['error']='ini file not found or does not exist'
        return settingsDict

    for line in fulltext:
        if line[0] == '[' or line[0] == '#' or len(line)<2:
            pass
            # This is  either:
            #   a comment line, ignore
            #   an empty line (\n), ignore
        else:
            try:
                # remove trailing '\n'
                text = line[0:-1]
                textlst = text.split('=')
                key = textlst[0]
                val = textlst[1]
                settingsDict[key] = val
            except:
                # Some text with errors, ignore (i.e. value instead of key=value
                pass

    return settingsDict