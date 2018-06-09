#!/user/bin/python3
"""entry point of the command interpreter"""
import cmd
import models
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
        prompt = "(hbnb) "

        def do_quit(self, arg):
                """Quit command to exit the program"""
                return True

        do_EOF = do_quit

        def do_create(self, arg):
                """Create an instance"""
                if len(arg) == 0:
                        print("** class name missing **")
                        return
                if arg not in dir(models.base_model):
                        print("** class doesn't exist **")
                        return
                else:
                        try:
                                new = eval(arg)()
                                new.save()
                                print(new.id)
                        except:
                                print("** class doesn't exist **")
        def do_show(self, arg):
                if len(arg) == 0:
                        print("** class name missing **")
                        return
                strings = arg.split()
                if strings[0] not in dir(models.base_model):
                        print("** class doesn't exist **")
                        return
                if len(strings) < 2:
                        print("** instance id missing **")
                        return
                try:
                        print(storage.all()[strings[0] + "." + strings[1]])
                                
                except:
                        print("** no instance found **")

        def do_destroy(self, arg):
                if len(arg) == 0:
                        print("** class name missing **")
                        return
                strings = arg.split()
                if strings[0] not in dir(models.base_model):
                        print("** class doesn't exist **")
                        return
                if len(strings) < 2:
                        print("** instance id missing **")
                        return
                try:
                        del(storage.all()[strings[0] + "." + strings[1]])
                        storage.save()
                except:
                        print("** no instance found **")

        def do_all(self, arg):
                if len(arg) == 0:
                        print([value for key, value in storage.all().items()])
                        return
                strings = arg.split()
                if strings[0] not in dir(models.base_model):
                        print("** class doesn't exist **")
                        return
                else:
                        print([value for key, value in storage.all().items() if strings[0] == type(value).__name__])
                        return

        def do_update(self, arg):
                """
                Updates a specific instance saved in file.json
                Usage: update <class name> <id> <attribute name> "<attribute value>"
                """
                if len(arg) == 0:
                        print("** class name missing **")
                        return
                strings = arg.split()
                if strings[0] not in dir(models.base_model):
                        print("** class doesn't exist **")
                        return
                elif len(strings) < 2:
                        print("** instance id missing **")
                        return
                elif len(strings) < 3:
                        print("** attribute name missing **")
                        return
                elif len(strings) < 4:
                        print("** value missing **")
                        return
                try:
                        search = strings[0] + "." + strings[1]
                        for key, value in storage.all().items():
                                if key == search:
                                        value.strings[2] = strings[3]
                                        value.save()
                                        return

                                
                except:
                        print("** no instance found **")
                


if __name__ == '__main__':
    HBNBCommand().cmdloop()