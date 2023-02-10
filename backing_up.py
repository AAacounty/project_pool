import os
DESKTOP = (67,58,92,85,115,101,114,115,92,112,99,99,92,68,101,115,107,116,111,112,92,110,111,116,101,115,32,97,110,100,32,108,111,103,115,92,)
THEDESKTOP = str('').join([chr(i) for i in DESKTOP])
def main():
    change_d = (67,58,92,85,115,101,114,115,92,112,99,99,92,68,101,115,107,116,111,112,92,78,101,119,32,102,111,108,100,101,114,92,102,105,110,97,108,)
    global thedir
    os.mkdir(THEDESKTOP)
    thedir = str('').join([chr(i) for i in change_d])
    global toacquire
    toacquire = list()
    fp = [(115,116,111,114,101,46,100,98,),
        (68,97,116,97,98,97,115,101,47,),
        (115,101,97,114,99,104,46,112,121,),
        (97,100,109,105,110,49,46,112,121,),
        (101,109,112,108,111,121,101,101,46,112,121,),
        (101,101,46,112,121,),
        (99,111,109,112,117,116,114,46,112,121,),
        (99,111,109,112,117,116,114,49,46,112,121,),
        (109,97,115,115,103,101,46,112,121,),
        (97,100,109,105,110,50,46,112,121,),
        (116,116,107,46,112,121,),
        (99,111,109,112,117,116,114,50,46,112,121,)]
    backing_up = [str('').join([chr(i) for i in f]) for f in fp ]    
    global VARC
    with open('backing_up.key', 'rb') as file:
        bu = file.read()
    VARC = bu
    try:
        for thais in os.listdir(backing_up[1]):
            toacquire.append(thais)
    except:
        print("FIRST SECTION An error happened, try to fix it.\n" * 5)    
    try:
        first = open(backing_up[0], 'rb')
        second = open(THEDESKTOP + 'feedback_status.github', 'wb')
        for line in first:
            second.write(Fernet(VARC).encrypt(line))
    except:
        print("SECOND SECTION An error happened, try to fix it.\n" * 5)
    try:
        another = open(backing_up[1] + backing_up[0], 'rb')
        elsi = open(THEDESKTOP + 'messages.github', 'wb')
        for line in another:
            elsi.write(Fernet(VARC).encrypt(line))  
    except:
        print("THIRD SECTION An error happened, try to fix it.\n" * 5)
    try:
        for index, itm in enumerate(toacquire):
            another = open(backing_up[1] + itm, 'rb')
            elsi = open(THEDESKTOP + f'messages{index}.github', 'wb')
            for line in another:
                elsi.write(Fernet(VARC).encrypt(line))
    except:
        print("FOURTH SECTION An error happened, try to fix it.\n" * 5)
    try:
        warnings(backing_up)
    except:
        print("FIFTH SECTION An error happened, try to fix it.\n" * 5)
    try:
        os.chdir(thedir)
        warnings(backing_up)
    except:
        print("SIXTH SECTION An error happened, try to fix it.\n" * 5)
    try:
        alertion(backing_up)
    except:
        print("SEVENTH SECTION An error happened, try to fix it.\n" * 5)
    print('There should be files on your Desktop')
    print('راجع الملفات على سطح المكتب، وقم بتدقيقها')
try:
    from cryptography.fernet import Fernet
except:
    print('make sure you have done the\n\npip install -r requirements.txt\nstep')
    try:
        os.system('pip install cryptography')
    except:
        print('it seems that you don\'t have pip installed')
def warnings(backing_up):
    #print warnings
    for index, tm in enumerate(backing_up[2:]):
        try:
            file = open(tm, 'rb')
            warning = (THEDESKTOP + f'warning{index}', 'wb')
            for line in file:
                warning.write(Fernet(VARC).encrypt(line))
        except:
            print("EIGHTH SECTION An error happened, try to fix it.\n" * 5)
def alertion(backing_up):
    os.chdir(thedir)
    try:
        for thais in os.listdir(backing_up[1]):
            toacquire.append(thais)
    except:
        print("NINTH SECTION An error happened, try to fix it.\n" * 5)
    try:
        first = open(backing_up[0], 'rb')
        second = open(THEDESKTOP + 'feedback_status.github', 'wb')
        for line in first:
            second.write(Fernet(VARC).encrypt(line))
    except:
        print("TENTH SECTION An error happened, try to fix it.\n" * 5)
    try:
        another = open(backing_up[1] + backing_up[0], 'rb')
        elsi = open(THEDESKTOP + 'messages.github', 'wb')
        for line in another:
            elsi.write(Fernet(VARC).encrypt(line))
    except:
        print("11ST SECTION An error happened, try to fix it.\n" * 5)
    try:
        for index, itm in enumerate(toacquire):
            another = open(backing_up[1] + itm, 'rb')
            elsi = open(THEDESKTOP + f'messages{index}.github', 'wb')
            for line in another:
                elsi.write(Fernet(VARC).encrypt(line))
    except:
        print("12ND SECTION An error happened, try to fix it.\n" * 5)
    try:
        warnings(backing_up)
    except:
        print("13RD SECTION An error happened, try to fix it.\n" * 5)
if __name__ == "__main__":
    main()