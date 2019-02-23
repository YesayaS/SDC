import win32api as wapi
import time

W       = [1,0,0,0,0,0,0,0,0,0]
A       = [0,1,0,0,0,0,0,0,0,0]
D       = [0,0,1,0,0,0,0,0,0,0]
SPACE   = [0,0,0,1,0,0,0,0,0,0]
WA      = [0,0,0,0,1,0,0,0,0,0]
WD      = [0,0,0,0,0,1,0,0,0,0]
SPACEa  = [0,0,0,0,0,0,1,0,0,0]
SPACEd  = [0,0,0,0,0,0,0,1,0,0]
Q       = [0,0,0,0,0,0,0,0,1,0]
nk      = [0,0,0,0,0,0,0,0,0,1]

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
     0    1    2  3  4   5      6       7    8     9
    [W, Space, A, D, WA, WD, SpaceA, SpaceD, Q,  NOKEY] boolean values.
    '''
    output = [0,0,0,0,0,0,0,0,0,0]

    if 'W' in keys:
        output = W
    elif 'SPACE' in keys:
        output = SPACE
    elif 'A' in keys:
        output = A
    elif 'D' in keys:
        output = D
    elif 'Q' in keys:
        output = Q
        
    elif 'WA' in keys or 'AW' in keys:
        output = WA
    elif 'WD' in keys or 'DW' in keys:
        output = WD
    elif 'SPACEA' in keys or 'ASPACE' in keys:
        output = SPACEa
    elif 'SPACED' in keys or 'DSPACE' in keys:
        output = SPACEd
        
    else:
        output = nk        
    return output

for i in range(8):
    time.sleep(1)
    f = key_check()
    out = keys_to_output(f)
    print(out)        
    print(type(f))
