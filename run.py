import os,sys,platform
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('chmod +x maharaj')
    os.system('./maharaj')
elif bit == '32bit':
    os.system('chmod +x maharaj32')
    os.system('./maharaj32')
else:
    print('device not supported')
