#!/usr/bin/python3
"""Module for a working console for AirBnB project
"""

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def emptyline(self):
        """Does not do anything on an emptyline
        """
        pass

    def do_quit(self, arg):
        """ Quits out of the console
        """
        quit()

    def do_EOF(self, arg):
        """ End of File: Quits out of console
        """
        quit()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
