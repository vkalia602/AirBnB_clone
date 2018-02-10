#!/usr/bin/python3

"""console for hbnb"""

import cmd
import json
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """hbnb console class"""
    prompt = '(hbnb) '
    valid_classes = {'BaseModel'}
    # ^^^^ used to check arguments of create() and show()

    def do_EOF(self, arg):
        """exits the console program on EOF"""
        return True

    def do_quit(self, arg):
        """exits the console program if user enters 'quit'"""
        return True

    def do_create(self, arg):
        """creates a new instance of BaseModel, saves it to JSON file and prints the
        id of the BaseModel instance"""
        if arg == "":
            print('** class name missing **')
        elif arg not in HBNBCommand.valid_classes:
            print('** class doesn\'t exist **')
        else:
            new = BaseModel()
            new.save()
            print(new.id)

    def do_show(self, line):
        """prints the string representation of an instance based on the class
        name and id"""
        if line == "":
            print('** class name missing **')
        elif line.split()[0] not in HBNBCommand.valid_classes:
            print('** class doesn\'t exist **')
        else:
            if len(line.split()) > 1:
                with open(storage.file_path, encoding='utf-8') as f:
                    data = json.load(f)
                clas = line.split()[0]
                instance_id = line.split()[1]
                key = "{}.{}".format(clas, instance_id)
                if key in data.keys():
                    obj_dict = data[key]
                    obj = BaseModel(**obj_dict)
                    print(obj)
                else:
                    print('** no instance found **')
            elif len(line.split()) < 2:
                print('** instance id missing **')

    def do_destroy(self, line):
        """deletes an instance based on the class name and id and saves the
        changes into the JSON file"""
        if line == "":
            print('** class name missing **')
        elif line.split()[0] not in HBNBCommand.valid_classes:
            print('** class doesn\'t exist **')
        else:
            if len(line.split()) > 1:
                with open(storage.file_path, encoding='utf-8') as f:
                    data = json.load(f)
                clas = line.split()[0]
                instance_id = line.split()[1]
                key = "{}.{}".format(clas, instance_id)
                if key in data.keys():
                    del data[key]
                    storage.objects = data
                    storage.save()
                else:
                    print('** no instance found **')
            elif len(line.split()) < 2:
                print('** instance id missing **')

    def do_all(self, line):
        """prints all string representation of all instances based or not on the
        class name"""
        try:
            with open(storage.file_path, encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = None
        if data is not None:
            if len(line.split()) > 0:
                clas = line.split()[0]
            else:
                clas = None
            for k, v in data.items():
                if clas == 'BaseModel' or clas is None:
                    print(BaseModel(**v))
                else:
                    print('** class doesn\'t exist **')
                    break


if __name__ == '__main__':
    HBNBCommand().cmdloop()
