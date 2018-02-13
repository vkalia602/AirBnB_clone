#!/usr/bin/python3
"""Module for a working console for AirBnB project
"""

import cmd
import json
from  models.base_model import BaseModel
from models import storage
import sys
class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    class_list = ('BaseModel')

    def do_create(self, arg):
        if arg is None or arg is "":
            print ("** class name missing **")
        elif arg in self.class_list:
            new = eval(arg)()
            new.save()
            print (new.id)
        else:
            print("** class doesn\'t exist **")

    def do_show(self, line):
        args = line.split()
        data = None
        if args is None or args is "":
            print ("** class name missing **")
        elif args[0] not in self.class_list:
            print ("** class doesn\'t exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[1] is None or args[1] is "":
            print("** instance id missing **")
        obj_list = storage.all()
        class_uuid = "{}.{}". format(args[0], args[1])
        try:
            value = obj_list[class_uuid]
            print(value)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):
        args = line.split()
        if args is None or args is "":
            print ("** class name missing **")
        elif args[0] not in self.class_list:
            print ("** class doesn\'t exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[1] is None or args[1] is "":
            print("** instance id missing **")
        obj_list = storage.all()
        class_uuid = "{}.{}". format(args[0], args[1])
        try:
           del(obj_list[class_uuid])
        except KeyError:
            print("** no instance found **")

    def all(self, line):
        args = line.split()
        if args[0] not in self.class_list:
            print ("** class doesn\'t exist **")
            
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
