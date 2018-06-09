#!/usr/bin/python3
"""entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
from shlex import split
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    classes = {"BaseModel",
               "User", "State", "City", "Amenity", "Place", "Review"}

    def do_quit(self, line):
        "Quit command to exit the program"
        return True

    do_EOF = do_quit

    def do_create(self, line):
        """creates an object"""
        if not len(line):
            print("** class name missing **")
            return
        if line not in HBNBCommand.classes:
            print("**class doesn't exist**")
            return
        newObject = eval(line)()
        print(newObject.id)
        newObject.save()

    def do_show(self, line):
        """shows an object"""
        if not len(line):
            print("** class name missing **")
            return
        strings = split(line)
        if strings[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(strings) == 1:
            print("** instance id missing **")
            return
        keyValue = strings[0] + '.' + strings[1]
        if keyValue not in storage.all().keys():
            print("** no instance found **")
        else:
            print(storage.all()[keyValue])

    def do_destroy(self, line):
        """deletes an object"""
        if not len(line):
            print("** class name missing **")
            return
        strings = split(line)
        if strings[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(strings) == 1:
            print("** instance id missing **")
            return
        keyValue = strings[0] + '.' + strings[1]
        if keyValue not in storage.all().keys():
            print("** no instance found **")
            return
        del storage.all()[keyValue]
        storage.save()

    def do_all(self, line):
        """prints all"""
        if not len(line):
            for obj in storage.all().values():
                print(obj)
            return
        strings = split(line)
        if strings[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        for obj in storage.all().values():
            if strings[0] == type(obj).__name__:
                print(obj)

    def do_update(self, line):
        """updates an object"""
        if not len(line):
            print("** class name missing **")
            return
        strings = split(line)
        for string in strings:
            if string.startswith('"') and string.endswith('"'):
                string = string[1:-1]
        if strings[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(strings) == 1:
            print("** instance id missing **")
            return
        keyValue = strings[0] + '.' + strings[1]
        if keyValue not in storage.all().keys():
            print("** no instance found **")
            return
        if len(strings) == 2:
            print("** attribute name missing **")
            return
        if len(strings) == 3:
            print("** value missing **")
            return
        setattr(storage.all()[keyValue], strings[2], strings[3])

    def emptyline(self):
        """passes"""
        pass

    def default(self, line):
        """defaults"""
        strings = line.split('.')
        if strings[0] not in HBNBCommand.classes:
            print("*** Unknown syntax: {}".format(line))
            return
        if strings[1] == "all()":
            self.do_all(strings[0])
        if strings[1] == "count()":
            count = 0
            for obj in storage.all().values():
                if strings[0] == type(obj).__name__:
                    count += 1
            print(count)
            return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
