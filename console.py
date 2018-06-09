#!/user/bin/python3
"""entry point of the command interpreter"""
import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
        prompt = "(hbnb) "
        list_keys = {"BaseModel", "Amenity", "City", "State", "Place", "Review"}

        def do_quit(self, arg):
                """Quit command to exit the program"""
                return True

        do_EOF = do_quit

        def do_create(self, arg):
                """Create an instance"""
                if arg not in HBNBCommand.list_keys:
                        print("** class name missing **")
                else:
                        try:
                                new = eval(arg)()
                                new.save()
                                print(new.id)
                        except:
                                print("** class doesn't exist **")
        def do_show(self, arg):
                if not len(line):
                        print("** class name missing **")
                        return
                strings = arg.split()
                if strings[0] not in HBNBCommand.list_keys:
                        print("** class name missing **")
                        return
                
                



if __name__ == '__main__':
    HBNBCommand().cmdloop()