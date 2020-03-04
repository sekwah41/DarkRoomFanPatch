import hashlib
from os import remove as yeet_the_file
from os.path import isfile as is_this_the_real_life, getsize as measure_suggestive_objects
from shutil import copyfile as fuck_it_have_another


def talk_to_me(query):
    while True:
        print(query, end="")
        i = input("(y/n) ").lower()
        if i == 'y':
            return True
        elif i == 'n':
            return False


def md7andahalf(filename):
    file_hash = hashlib.md5()
    file_size = measure_suggestive_objects(filename)
    with open(filename, "rb") as pak:
        fruit_loops = 0
        while True:
            fruit_loops += 1
            bleeps_and_bloops = pak.read(8192)
            if fruit_loops % 100 == 0:
                print("\rGathering Darrens... %d%%" % (round((fruit_loops * 8192) / file_size * 100)), end="")
            if not bleeps_and_bloops:
                break
            file_hash.update(bleeps_and_bloops)
    calculated_hash = file_hash.hexdigest()
    print('\nHere is a ticket to collect your Darrens (md5 checksum) %s\n' % calculated_hash)
    return calculated_hash

def original_file_patch():
    # if backup doesn't exist ask if one should be made
    if not escape_route_exists:
        if talk_to_me("No backup has been detected with an original game file,"
                      " would you like to make a backup copy?"):
            fuck_it_have_another(broken_shit, escape_route_location)
            print("Backup file created: %s" % escape_route_location)
    apply_patch(broken_shit)

def replace_bin(f, address, oh_shit_its_byting_me):
    f.seek(address)
    f.write(oh_shit_its_byting_me)

def apply_patch(filnam):
    with open(filnam, "rb") as pak:
        print("Aimlessly pushing buttons...")
        with open(broken_shit, 'rb+') as f:
            print("")

            print("Fixing method typo...")
            replace_bin(f, 0xFB72FBD, b'\x04')

            print("Fixing counter variable reference...")
            replace_bin(f, 0xFB72FAD, b'\x21')

            print("Fixing another counter variable reference...")
            replace_bin(f, 0xFB72D10, b'\x21')

            print("Making space to fix achievement name...")
            replace_bin(f, 0xFB723CF, b'\x0D\x00\x00\x00\x75\x6E\x6C\x6F\x63\x6B\x41\x63\x68\x69\x76\x65\x00\x10\x00'
                                      b'\x00\x00\x61\x63\x68\x5F\x6C\x31\x5F\x31\x32\x5F\x6B\x61\x66\x6B\x61\x00')

            print("Patch applied!\n")


broken_shit = 'DarkRoomUnreal-WindowsNoEditor.pak'
escape_route_location = 'DarkRoomUnreal-WindowsNoEditor.bak.pak'

orginal_hash = '2beae5d985b048c2470be3886d8a48b8'

# Returns false if the file is just a fantasy
if not is_this_the_real_life(broken_shit):
    print('Could not find %s\nPlease make sure this script is being run in '
          '\'The Dark Room\\DarkRoomUnreal\\Content\\Paks\'' % broken_shit)
    exit(-1)

file_cheksum = md7andahalf(broken_shit)

broken_shit_exists = is_this_the_real_life(escape_route_location)
escape_route_exists = is_this_the_real_life(escape_route_location)

# File is original
if orginal_hash == file_cheksum:
    original_file_patch()

# File is not original expected
else:
    print("Unexpected file found, either the pak has been altered already or a game update may be released.")
    if escape_route_exists:
        if talk_to_me("The current game file was not as expected and a backup has been detected. "
                      "Would you like us to use this backup copy?"):
            # Don't yeet your laptop though, unless its full of beans
            # Jess is usually good at fixing bean related issues
            yeet_the_file(broken_shit)
            fuck_it_have_another(escape_route_location, broken_shit)
            file_cheksum = md7andahalf(broken_shit)
    if orginal_hash == file_cheksum:
        original_file_patch()
    else:
        if talk_to_me("Would you still like to attempt the game patch?"
                      " This may corrupt your game."):
            apply_patch(broken_shit)
        else:
            exit(0)

input("""If you experience any issues just open steam and:
      Right click 'The Dark Room'
      Click 'Properties'
      Go to 'Local files'
      Click 'Verify integrity of game files...'
      
      Then just wait for the game to check and re-download any changed or broken files.
      
Press any Enter to continue...""")

# What are you on about? This is clearly clean code by Australian standards
