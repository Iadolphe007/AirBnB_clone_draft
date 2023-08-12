#!/usr/bin/python3
"""entry point of command line interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """command line interpreter"""
    prompt = "(hbnb)"

    def emptyline(self):
        """empty line + ENTER"""
        pass

    def do_EOF(self, line):
        """handle EOF"""
        print()
        return true
    def do_quit(self, line):
        """exit program command"""
        return true
    def do_create(self, line):
        """create a new instance"""
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            b = storage.classes()[line]()
            b.save()
            print(b.id)

    def do_show(self, line):
        """print string representation"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args = line.split(' ')
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                class_name = args[0]
                instance_id = args[1]
                isntance = storage.all()
                key = class_name + "." + instance_id

                if key in instances:
                    print(instances[key])
                else:
                    print("** no instance found **")




if __name__ == '__main__':
        HBNBCommand().cmdloop()
