#!/usr/bin/python3
"""AirBnB Clone Console."""

class HBNBCommand(cmd.Cmd):
    """Command interpreter"""
     prompt = '(hbnb) '

    def do_quit(self, line):
        """quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

