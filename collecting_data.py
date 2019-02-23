import numpy as np
from grab_test_image import grab_screen
import cv2
import time
from getkeys import key_check
import os
#          w a d s 
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

starting_value = 1

while True:
    file_name = 'D:/My Documents/GitHub/SDC/training_data/training_data-{}.npy'.format(starting_value)

    if os.path.isfile(file_name):
        print('File exists, moving along',starting_value)
        starting_value += 1
    else:
        print('File does not exist, starting fresh!',starting_value)
        
        break

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


def main(file_name, starting_value):
    file_name = file_name
    starting_value = starting_value
    training_data = []
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    last_time = time.time()
    paused = False
    print('STARTING!!!')
    while(True):
        
        if not paused:
            screen = grab_screen(region=(0,200,1920,980))
            last_time = time.time()
            # resize to something a bit more acceptable for a CNN
            screen = cv2.resize(screen, (480,270))
            # run a color convert:
            # screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
            
            keys = key_check()
            output = keys_to_output(keys)
            print(output)
            training_data.append([screen,output])

            #print('loop took {} seconds'.format(time.time()-last_time))
            last_time = time.time()
            cv2.imshow('window',cv2.resize(screen,(640,360)))
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break

            if len(training_data) % 100 == 0:
                print(len(training_data))
                
                if len(training_data) == 500:
                    np.save(file_name,training_data)
                    print('SAVED')
                    training_data = []
                    starting_value += 1
                    file_name = 'D:/My Documents/GitHub/SDC/training_data/training_data-{}.npy'.format(starting_value)

                    
        keys = key_check()
        if 'T' in keys:
            if paused:
                paused = False
                print('unpaused!')
                time.sleep(1)
            else:
                print('Pausing!')
                paused = True
                time.sleep(1)


main(file_name, starting_value)
