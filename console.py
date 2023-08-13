#!/usr/bin/python3
"""AirBnB Clone Console."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter
    Attributes:
        prompt: The command prompt.
    """
    prompt = '(hbnb)'

    def do_quit(self, line):
        """quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Command to exit the program"""
        return True
    def emptyline(self):
        """Empty line does nothing"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

