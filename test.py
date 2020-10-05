import sys
import time
from assignment3 import ConfigDict

cd = ConfigDict('Configo6_file.txt')

if len(sys.argv) == 3:
    # a = sys.argv[1]
    # b = sys.argv[2]
    # print('writing data:  {0}, {1}'.format(a, b))
    #
    # cd[a] = b
    key = sys.argv[1]
    value = sys.argv[2]
    print('writing data:  {0}, {1}'.format(key, value))

    cd[key] = value

else:
    print('reading data')
    for key in cd.keys():
              print('    {0} -- {1}'.format(key, cd[key]))
              time.sleep(3)
print(cd)