#!/usr/bin/python3
"""entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_quit(self, line):
        "Quit command to exit the program"
        return True

    do_EOF = do_quit

    def do_create(self, line):
        key = ["BaseModel"]
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
        classes = ["BaseModel"]
        if not len(line):
            print("** class name missing **")
            return
        strings = line.split()
        if strings[0] not in classes:
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
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
