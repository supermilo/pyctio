import sys
import time
from assignment5 import ConfigPickleDict

# cd = ConfigPickleDict('C:\\Users\\super\\Desktop\\Pickles\\file')
cd = ConfigPickleDict('File.pickle')
# cd = ConfigPickleDict()


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
# print(cd)
