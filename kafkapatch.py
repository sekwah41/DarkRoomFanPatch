import hashlib
from os.path import isfile


def md5(filename):
    file_hash = hashlib.md5()
    with open(filename, "rb") as pak:
        while True:
            data = pak.read(8192)
            if not data:
                break
            file_hash.update(data)
    return file_hash.hexdigest()


file_name = 'DarkRoomUnreal-WindowsNoEditor.pak'

original_hash = '2beae5d985b048c2470be3886d8a48b8'

if not isfile(file_name):
    print('Could not find %s\nPlease make sure this script is being run in '
          '\'The Dark Room\\DarkRoomUnreal\\Content\\Paks\'' % file_name)
    exit(-1)
