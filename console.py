#!/usr/bin/python3

"""console for hbnb"""

import cmd


class HBNBCommand(cmd.Cmd):
    """hbnb console class"""
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """exits the console program on EOF"""
        return True

    def do_quit(self, arg):
        """exits the console program if user enters 'quit'"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
