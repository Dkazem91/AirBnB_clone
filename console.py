#!/usr/bin/python3
"""entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    classes = ["BaseModel"]

    def do_quit(self, line):
        "Quit command to exit the program"
        return True

    do_EOF = do_quit

    def do_create(self, line):
        if not len(line):
            print("** class name missing **")
        else:
            try:
                newObject = eval(line)()
                print(newObject.id)
                newObject.save()
            except:
                print("** class doesn't exist **")

    def do_show(self, line):
        if not len(line):
            print("** class name missing **")
            return
        strings = line.split()
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
        if not len(line):
            print("** class name missing **")
            return
        strings = line.split()
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
        if not len(line):
            for obj in storage.all().values():
                print(obj)
            return
        strings = line.split()
        if strings[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        for obj in storage.all().values():
            if strings[0] == type(obj).__name__:
                print(obj)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
