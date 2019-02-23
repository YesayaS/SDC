import win32api as wapi
import time

W = [1,0,0,0,0,0,0,0,0]
A = [0,1,0,0,0,0,0,0,0]
D = [0,0,1,0,0,0,0,0,0]
SPACE = [0,0,0,1,0,0,0,0,0]
WA = [0,0,0,0,1,0,0,0,0]
AW = WA
WD = [0,0,0,0,0,1,0,0,0]
DW = WD
SPACEA = [0,0,0,0,0,0,1,0,0]
ASPACE = SPACEA
SPACED = [0,0,0,0,0,0,0,1,0]
DSPACE = SPACED
#q = 
nk = [0,0,0,0,0,0,0,0,1]

keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'£$/\\":
    keyList.append(char)

def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            if key == ' ':
                key = 'SPACE'
            keys.append(key)
    if keys == []:
        keys = ['nk']
    keys = ''.join(keys)
    return keys

def keys_to_output(keys):
    '''
    Convert keys to a ...multi-hot... array
     0  1  2  3  4   5   6   7    8
    [W, S, A, D, WA, WD, SA, SD, NOKEY] boolean values.
    '''
    a = keys
    exec("%s = %s" % (a,keys))
    output = a
    return output

for i in range(8):
    time.sleep(1)
    f = key_check()
    try :
        out = keys_to_output(f)
        print(out)        
        print(type(out))
    except :
        NameError : None
