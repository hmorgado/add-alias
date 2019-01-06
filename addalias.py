import sys
from collections import namedtuple
import pathlib

if len(sys.argv) != 3:
    print('I need THREE arguments.')
    exit(1)

home = str(pathlib.PosixPath.home())
file = '{}/.bashrc'.format(home)

with open(file, mode='r') as my_file:
    filedata = my_file.read()

NewCommand = namedtuple('NewCommand', 'alias actual_command')
new_alias = NewCommand(sys.argv[1], sys.argv[2])

alias = new_alias.alias
actual_command = new_alias.actual_command
cmd = "alias {}='{}'".format(alias, actual_command)
final_cmd = "# alias_here\n" + cmd

filedata = filedata.replace('# alias_here', final_cmd)

with open(file, mode='w') as my_file:
    my_file.write(filedata)

print('Added new alias:', cmd)
