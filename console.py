#!/usr/bin/python3
"""entry point of the command interpreter"""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_quit(self, line):
        "Quit command to exit the program"
        return True

    do_EOF = do_quit

    def do_create(self, line):
        if not len(line):
            print("** class name missing **")
        for x in line:
            print(x)

if __name__=='__main__':
    HBNBCommand().cmdloop()
