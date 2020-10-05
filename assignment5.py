import os
import pickle


# class StrToBytes:
#     def __init__(self, fileobj):
#         self.fileobj = fileobj
#     def read(self, size):
#         return self.fileobj.read(size).encode()
#     def readline(self, size=-1):
#         return self.fileobj.readline(size).encode()


class  ConfigKeyError(Exception):
    def __init__(self, this, key):
        self.key = key
        self.keys =this.keys()
    def __str__(self):
        return 'key "{0} not found. Available keys: ({1})'.format(self.key, ', '.join(self.keys))


class ConfigPickleDict(dict):

    config_dir = "C:\\Users\\super\\Desktop\\Pickles"

    def __init__(self, picklename):

        self.filename = os.path.join(ConfigPickleDict.config_dir, picklename + '.pickle')
        if not os.path.isfile(self.filename):
            with open(self.filename, 'wb') as fh:
                dicto = {'2':'2', '1':'3', '9':'hola'}
                # pickle.dump(StrToBytes({}), fh)
                pickle.dump(dicto, fh)

        with open(self.filename, 'rb') as fh:
            # pkl = pickle.load(StrToBytes(fh))
            pkl = pickle.load(fh)
            self.update(pkl)
            print(self)





    def __getitem__(self, key):
        if not key in self:
            raise ConfigKeyError(self, key)
        return dict.__getitem__(self, key)

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        print(self)


        with open(self.filename, 'wb') as fh:
            # pickle.dump(StrToBytes(self), StrToBytes(fh))
            pickle.dump(self, fh)

# cc =ConfigDict('configu.txt')