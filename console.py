#!/user/bin/python3
"""entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
        prompt = "(hbnb) "

        def do_quit(self, arg):
                """Quit command to exit the program"""
                return True

        do_EOF = do_quit

        def do_create(self, arg):
                """Create an instance"""
                if len(arg) < 1:
                        print("** class name missing **")
                else:
                        try:
                                new = eval(arg)()
                                new.save()
                                print(new.id)
                        except:
                                print("** class doesn't exist **")
        def do_show

if __name__ == '__main__':
    HBNBCommand().cmdloop()