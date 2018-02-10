#!/usr/bin/python3

"""console for hbnb"""

import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """hbnb console class"""
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """exits the console program on EOF"""
        return True

    def do_quit(self, arg):
        """exits the console program if user enters 'quit'"""
        return True

    def do_create(self, arg):
        """creates a new instance of BaseModel, saves it to JSON file and prints the
        id of the BaseModel instance"""
        if arg is None:
            print('** class name missing **')
            return
        valid_classes = {'BaseModel'}
        if arg not in valid_classes:
            print('** class doesn\'t exist **')
            return
        new = BaseModel()
        new.save()
        print(new.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
