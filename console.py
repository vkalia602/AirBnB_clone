#!/usr/bin/python3

"""
Console: module for the HBNBCommand class
Contains the following commands used to work with the models:

        create - creates a new instance of a model
        show - prints the string representation of an instance
        destroy - deletes an instance from storage
        all - displays all instances of a class or all classes
        update - updates the attributes of an instance
        EOF - allows Ctrl-D / Ctrl-Z to exit the console
        quit - allows the console to exit when user enters 'quit'
        emptyline - does nothing if user doesn't enter a command

Valid models: BaseModel, User, Place, State, City, Amenity, Review
"""

import cmd
import json
from models.base_model import BaseModel
from models import storage
from datetime import datetime
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class: utilizes cmd.Cmd to create a shell interface that allows
    users to create, display, update, and/or delete models.
    """

    prompt = '(hbnb) '
    classes = {'BaseModel', 'User', 'Place',
               'State', 'City', 'Amenity', 'Review'}
    # ^^^^^ these are considered valid models
    fp = storage._FileStorage__file_path
    # ^^^^^ alias for the storage file path

    def do_create(self, token):
        """
        creates a new instance of a model if it's valid, saves it to the
        json file (set in engine.FileStorage), then prints it's id.

        usage: create <class_name>
        """
        if token == '':
            print('** class name missing **')
        elif token not in self.classes:
            print('** class doesn\'t exist **')
        else:
            new = eval(token)()
            new.save()
            print(new.id)

    def do_show(self, line):
        """
        prints the string representation of an instance

        usage: show <class_name> <id>
        """
        tokens = line.split()   # tokens[0] will be 1st arg (<class name>)
        if len(tokens) == 0:
            print('** class name missing **')
        elif tokens[0] not in self.classes:
            print('** class doesn\'t exist **')
        elif len(tokens) < 2:
            print('** instance id missing **')
        else:
            try:
                with open(self.fp, encoding='utf-8') as f:
                    data = json.load(f)
            except FileNotFoundError:
                data = None
                print('** no instance found **')
                return
            if data:
                clas = tokens[0]
                uuid = tokens[1]
                keystring = "{}.{}".format(clas, uuid)
                for key, val in data.items():
                    del val['__class__']
                    if keystring in data.keys():
                        obj_dict = data[key]
                        obj = eval(clas)(**obj_dict)
                        print(obj)
                        return
            print('** no instance found **')

    def do_destroy(self, line):
        """
        destroy: deletes an instance and saves the changes into storage

        usage: destroy <class_name> <id>
        """
        tokens = line.split()   # tokens[0] will be 1st arg (<class name>)
        if len(tokens) == 0:
            print('** class name missing **')
        elif tokens[0] not in self.classes:
            print('** class doesn\'t exist **')
        else:
            if len(tokens) < 2:
                print('** instance id missing **')
            elif len(tokens) > 1:
                try:
                    with open(self.fp, encoding='utf-8') as f:
                        data = json.load(f)
                except FileNotFoundError:
                    data = None
                if data:
                    class_name = tokens[0]
                    instance_id = tokens[1]
                    key = "{}.{}".format(class_name, instance_id)
                    if key in data.keys():
                        del data[key]
                        storage._FileStorage__objects = data
                        storage.save()
                    else:
                        print('** no instance found **')

    def do_all(self, line):
        """
        all: prints the string representation of all objects

        usage: all [<class_name>]
        """
        try:
            with open(self.fp, encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = None
        tokens = line.split()   # tokens[0] will be 1st arg (<class name>)
        models = []
        if len(tokens) > 0 and tokens[0] in self.classes:
            class_name = tokens[0]
        elif len(tokens) > 0 and tokens[0] not in self.classes:
            print('** class doesn\'t exist **')
            return
        else:
            class_name = None   # if class_name is none, display ALL instances
        if data:
            if class_name is not None:
                for key, val in data.items():
                    if val['__class__'] == class_name:
                        del val['__class__']
                        model = eval(class_name)(**val)
                        models.append(model)
            elif class_name is None:
                for key, val in data.items():
                    class_name = val['__class__']
                    del val['__class__']
                    model = eval(class_name)(**val)
                    models.append(model)
            if len(models) > 0:
                print(models)
        if data is None and len(tokens) > 0 and class_name is not None:
            # example: all BaseModel should print nothing is there's no data
            pass

    def do_update(self, line):
        """
        update: updates an instance and saves the changes to storage

        usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        tokens = line.split()
        if len(tokens) == 0:
            print('** class name missing **')
        elif tokens[0] not in self.classes:
            print('** class doesn\'t exist **')
        elif len(tokens) < 2:
            print('** instance id missing **')
        else:
            try:
                with open(self.fp, encoding='utf-8') as f:
                    data = json.load(f)
            except FileNotFoundError:
                data = None
            if data:
                for instance in data.values():
                    if instance['id'] == tokens[1]:
                        if len(tokens) < 3:
                            print('** attribute name missing **')
                            return
                        elif len(tokens) < 4:
                            print('** value missing **')
                            return
                        else:
                            attr_name = tokens[2]
                            attr_value = tokens[3]
                            # values need to be wrapped in double quotes ("")
                            # if there is whitespace
                            attr_values = []
                            for word in tokens[3:]:
                                if word[0] == '"':
                                    attr_values.append(word.replace('"', ''))
                                elif word[-1] == '"':
                                    attr_values.append(word.replace('"', ''))
                                else:
                                    attr_values.append(word)
                            instance[attr_name] = " ".join(attr_values)
                            instance['updated_at'] = datetime.now().isoformat()
                            key = '{}.{}'.format(tokens[0], tokens[1])
                            storage._FileStorage__objects[key] = instance
                            storage.save()
                            return
                else:
                    print('** no instance found **')

    def do_EOF(self, line):
        """
        EOF: exits the console program on EOF (Ctrl-D / Ctrl-Z)
        """
        return True

    def do_quit(self, line):
        """
        quit: exits the console program if user enters 'quit'
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
