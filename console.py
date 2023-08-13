#!/usr/bin/python3
"""AirBnB Clone Console."""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
import re
import shlex
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """Command interpreter
    Attributes:
        prompt: The command prompt.
    """
    prompt = '(hbnb)'
    __clone_classes = {
        "BaseModel",
        "User"
    }

    def do_quit(self, line):
        """quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Command to exit the program"""
        return True

    def emptyline(self):
        """Empty line does nothing"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        """
        argline = parse(line)
        if len(argline) == 0:
            print("** class name missing **")
        elif argline[0] not in self.__clone_classes:
            print("** class doesn't exist **")
        else:
            print(eval(argline[0])().id)

    def do_show(self, line):
        """Prints the string representation of an instance
         based on the class name and id"""
        command = self.parseline(line)[0]
        arg = self.parseline(line)[1]
        if command is None:
            print('** class name missing **')
        elif command not in self.allowed_classes:
            print("** class doesn't exist **")
        elif arg == '':
            print('** instance id missing **')
        else:
            inst_data = models.storage.all().get(command + '.' + arg)
            if inst_data is None:
                print('** no instance found **')
            else:
                print(inst_data)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""
        command = self.parseline(line)[0]
        args = self.parseline(line)[1]
        if command is None:
            print('** class name missing **')
        elif command not in self.__clone_classes:
            print("** class doesn't exist **")
        elif args == '':
            print('** instance id missing **')
        else:
            k = command + '.' + args
            inst_data = models.storage.all().get(k)
            if inst_data is None:
                print('** no instance found **')
            else:
                del models.storage.all()[k]
                models.storage.save()

    def do_all(self, line):
        """Prints all string representation of all
        instances based or not on the class name.
        """
        command = self.parseline(line)[0]
        objs = models.storage.all()
        if command is None:
            print([str(objs[obj]) for obj in objs])
        elif command in self.__clone_classes:
            keys = objs.keys()
            print([str(objs[key]) for key in keys if key.startswith(command)])
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        """
        args = shlex.split(line)
        size_args = len(args)
        if size_args == 0:
            print('** class name missing **')
        elif args[0] not in self.__clone_classes:
            print("** class doesn't exist **")
        elif size_args == 1:
            print('** instance id missing **')
        else:
            key = args[0] + '.' + args[1]
            inst_data = models.storage.all().get(key)
            if inst_data is None:
                print('** no instance found **')
            elif size_args == 2:
                print('** attribute name missing **')
            elif size_args == 3:
                print('** value missing **')
            else:
                args[3] = self.analyze_parameter_value(args[3])
                setattr(inst_data, args[2], args[3])
                setattr(inst_data, 'updated_at', datetime.now())
                models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

