#!/usr/bin/env python3
"""module - the console"""

import cmd
import models
from models.base_model import BaseModel


classes = {"BaseModel": BaseModel}

class HBNBCommand(cmd.Cmd):
    """ the command line for the hbnb """

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program\n"""

        return True

    def do_EOF(self, line):
        """quit the program on end of file"""

        print()
        return True
    def emptyline(self):
        """ the command line should do nothing"""
        pass

    def do_help(self, line):
        """ display help information about the commands"""
        cmd.Cmd.do_help(self, line)

    def do_create(self, args):
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        new_instance = classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """prints the string representation of an instance"""
        args = args.split(" ")
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_id = args[1]
        all_instances = models.storage.all()
        found = False
        for key, instance in all_instances.items():
            if class_name in key and class_id in key:
                found = True
                print(instance)
                break
        if not found:
            print("** no instance found **")

    def do_destroy(self, args):
        """ deleting an instance"""
        args = args.split(" ")
        if len(args) < 1:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id is missing **")
            return

        found = False
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_instances = models.storage.all()
        instance = all_instances.pop(key)
        if instance:
            del(instance)
            models.storage.save()
            found = True
        if not found:
            print("** no instance found **")

    def do_all(self, args):
        """ function to print all the string representation of based no ornot based on the classes"""
        args = args.split(" ")
        class_name = args[0]
        if class_name:
            if class_name not in classes:
                print("** class doesn't exist **")
                return
        else:
            all_instances = models.storage.all()
            for key, instances in all_instances.items():
                print([str(instances)])
        if class_name in classes:
            all_instances = models.storage.all()
            for key, instance in all_instances.items():
                if class_name in key:
                    print([str(instance)])

    def do_update(self, args):
        """ update an instance based on a class name an id"""
        args = args.split(" ")
        class_name = args[0]

        if len(args) < 1:
            print("** class name missing **")
            return
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        found = False
        key = "{}.{}".format(class_name, instance_id)
        all_instances = models.storage.all()
        if len(args) < 3:
            print("** atribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_name = args[2]
        attribute_value = args[3]

        for key, instance in all_instances.items():
            if instance_id in key:
                found = True
                if len(args) < 5:
                    setattr(instance, attribute_name, attribute_value.strip('"'))
                    models.storage.save()

        if not found:
            print("** no instance found **")
            return

        


if __name__ == '__main__':
    HBNBCommand().cmdloop()
