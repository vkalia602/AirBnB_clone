#!/usr/bin/python3

"""console for hbnb"""

import cmd
import json
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """hbnb console class"""
    prompt = '(hbnb) '
    valid_classes = {'BaseModel'}
    # ^^^^ used to check arguments of create() and show()

    def do_create(self, token):
        """creates a new instance of BaseModel, saves it to JSON file and prints
        the id of the BaseModel instance"""
        if token == "":
            print('** class name missing **')
        elif token not in HBNBCommand.valid_classes:
            print('** class doesn\'t exist **')
        else:
            if token == 'BaseModel':
                new = BaseModel()
            new.save()
            print(new.id)

    def do_show(self, line):
        """prints the string representation of an instance based on the class
        name and id"""
        tokens = line.split()   # tokens[0] will be 1st arg (<class name>)
        if len(tokens) == 0:
            print('** class name missing **')
        elif tokens[0] not in HBNBCommand.valid_classes:
            print('** class doesn\'t exist **')
        elif len(tokens) < 2:
            print('** instance id missing **')
        else:
            try:
                with open(storage._FileStorage__file_path, encoding='utf-8') as f:
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
                        obj = BaseModel(**obj_dict)
                        print(obj)
                        return
            print('** no instance found **')

    def do_destroy(self, line):
        """deletes an instance based on the class name and id and saves the
        changes into the JSON file"""
        tokens = line.split()   # tokens[0] will be 1st arg (<class name>)
        if len(tokens) == 0:
            print('** class name missing **')
        elif tokens[0] not in HBNBCommand.valid_classes:
            print('** class doesn\'t exist **')
        else:
            if len(tokens) < 2:
                print('** instance id missing **')
            elif len(tokens) > 1:
                try:
                    with open(storage._FileStorage__file_path, encoding='utf-8') as f:
                        data = json.load(f)
                except FileNotFoundError:
                    data = None
                if data:
                    clas = tokens[0]
                    uuid = tokens[1]
                    key = "{}.{}".format(clas, uuid)
                    if key in data.keys():
                        del data[key]
                        storage._FileStorage__objects = data
                        storage.save()
                    else:
                        print('** no instance found **')

    def do_all(self, line):
        """prints all string representation of all instances based or not on the
        class name"""
        try:
            with open(storage._FileStorage__file_path, encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = None
        tokens = line.split()   # tokens[0] will be 1st arg (<class name>)
        if data:
            models = []
            clas = tokens[0] if len(tokens) > 0 else None
            #print(data)
            for k, v in data.items():
                del v['__class__']
                if clas == 'BaseModel' or clas is None:
                    pass
                    models.append(BaseModel(**v))
                else:
                    print('** class doesn\'t exist **')
                    return
            print(models)
        if len(tokens) > 0 and data is None:
            if tokens[0] not in HBNBCommand.valid_classes:
                print('** class doesn\'t exist **')

    def do_update(self, line):
        """updates an instance based on the class name and id by adding or
        updating attribute and saves the change into the JSON file

        usage: update <class name> <id> <attribute name> "<attribute value>"""
        tokens = line.split()
        if len(tokens) == 0:
            print('** class name missing **')
        # tokens[0] is <class name>
        elif tokens[0] not in HBNBCommand.valid_classes:
            print('** class doesn\'t exist **')
        # tokens[1] is <id>
        elif len(tokens) < 2:
            print('** instance id missing **')
        else:
            try:
                with open(storage._FileStorage__file_path, encoding='utf-8') as f:
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
                            attr_values = []
                            for word in tokens[3:]:
                                if word[0] == '"':
                                    attr_values.append(word.replace('"', ''))
                                elif word[-1 ] == '"':
                                    attr_values.append(word.replace('"', ''))
                                else:
                                    attr_values.append(word)
                            instance[attr_name] = " ".join(attr_values)
                            instance['updated_at'] = datetime.now().isoformat()
                            key = '{}.{}'.format(tokens[0], tokens[1])
                            storage._FileStorage__objects[key] = instance
                            storage.save()
                            return
            print('** no instance found **')

    def do_EOF(self, line):
        """exits the console program on EOF"""
        return True

    def do_quit(self, line):
        """exits the console program if user enters 'quit'\n"""
        return True

    def emptyline(self):
        """does nothing when user presses enter"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
