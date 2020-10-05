import os

class ConfigDict(dict):

    def __init__(self,filename):

        self.filename = filename
        if os.path.isfile(self.filename):
            with open(self.filename) as fh:
                for line in fh:
                    line = line.rstrip()
                    ke, val = line.split('=', 1)
                    dict.__setitem__(self,ke,val)

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        with open(self.filename, 'w') as fh:
            for k, v in self.items():
                fh.write('{0} = {1}\n'.format(k,v))

# cc =ConfigDict('configu.txt')


