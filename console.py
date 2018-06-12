#!/user/bin/python3
"""entry point of the command interpreter"""
import cmd
import models
import shlex
from ast import literal_eval
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    set_classes = {
        "Amenity",
        "BaseModel",
        "City",
        "Place",
        "Review",
        "State",
        "User"}

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    do_EOF = do_quit

    def do_create(self, arg):
        """Create an instance"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg not in HBNBCommand.set_classes:
            print("** class doesn't exist **")
            return
        else:
            try:
                new = eval(arg)()
                new.save()
                print(new.id)
            except BaseException:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Shows data on particular objects"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        strings = arg.split()
        if strings[0] not in HBNBCommand.set_classes:
            print("** class doesn't exist **")
            return
        if len(strings) < 2:
            print("** instance id missing **")
            return
        try:
            print(storage.all()[strings[0] + "." + strings[1]])

        except BaseException:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Destroy aparticular object"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        strings = arg.split()
        if strings[0] not in HBNBCommand.set_classes:
            print("** class doesn't exist **")
            return
        if len(strings) < 2:
            print("** instance id missing **")
            return
        try:
            del(storage.all()[strings[0] + "." + strings[1]])
            storage.save()
        except BaseException:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all objects saved or all of a particular class"""
        if len(arg) == 0:
            print([value for key, value in storage.all().items()])
            return
        strings = arg.split()
        if strings[0] not in HBNBCommand.set_classes:
            print("** class doesn't exist **")
            return
        else:
            print([value for key, value in storage.all().items()
                   if strings[0] == type(value).__name__])
            return

    def do_update(self, arg):
        """
        Updates a specific instance saved in file.json
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        if len(arg) == 0:
            print("** class name missing **")
            return
        strings = shlex.split(arg)
        if strings[0] not in HBNBCommand.set_classes:
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

        search = strings[0] + "." + strings[1]
        for key, value in storage.all().items():
            if key == search:
                setattr(value, strings[2], strings[3])
                value.save()
                return
        print("** no instance found **")
        return

    def emptyline(self):
        pass

    def new_strip(self, arg):
        beg_paren = arg.find("(")
        end_paren = arg.find(")")
        new = arg[beg_paren + 1:end_paren]
        
        new = new.split(", ")
        new[0] = new[0].replace('"', '')
        return new
    
    def count(self, arg):
        count = 0
        for value in storage.all().values():
            if type(value).__name__ == arg:
                count += 1
        return count

    def dict_strip(self, st):
        """tries to find a dict while stripping"""
        newstring = st[st.find("(")+1:st.rfind(")")]
        try:
            newdict = newstring[newstring.find("{")+1:newstring.rfind("}")]
            return eval("{" + newdict + "}")
        except:
            return None

    def default(self, arg):
        new_list = self.new_strip(arg)
        arg_shlip = list(shlex.shlex(arg, posix=True))
        if arg_shlip[0] in HBNBCommand.set_classes:
            if arg_shlip[2] == "all":
                self.do_all(arg_shlip[0])
                return
            elif arg_shlip[2] == "count":
                print(self.count(arg_shlip[0]))
                return
            elif arg_shlip[2] == "show":
                key = arg_shlip[0] + " " + new_list[0]
                self.do_show(key)
                return
            elif arg_shlip[2] == "destroy":
                key = arg_shlip[0] + " " + new_list[0]
                self.do_destroy(key)
                return
            elif arg_shlip[2] == "update":
                id_key = arg_shlip[0] + "." + new_list[0]
                try:
                    literal_eval(new_list[1])
                    new_list[1] = new_list[1].replace('"', '')
                    new_list[2] = new_list[2].replace('"', '')
                    new_command = arg_shlip[0] + " " + new_list[0] + " " + new_list[1] + " " + new_list[2]
                    self.do_update(new_command)
                    
                except:
                    obj = storage.all()[id_key]
                    check = self.dict_strip(arg)
                    if (isinstance(check, dict)):
                        new_list[1] = check
                    else:
                        print("Input a dictionary")
                        return
                    for key, value in new_list[1].items():
                        setattr(obj, key, value)
            else:
                print("*** Unknown syntax: {}".format(arg))
                return
        else:
            print("*** Unknown syntax: {}".format(arg))
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
