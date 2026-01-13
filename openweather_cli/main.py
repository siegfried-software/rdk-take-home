import cmd
import os

class OpenWeatherCLI(cmd.Cmd):
    intro = """
============ OPENWEATHERCLI ============\n
To begin, type 'help' to list available commands.\n
========================================\n
    """    
    prompt = 'OpenWeatherCLI>> '
    
    def __init__(self):
        super().__init__()
        self.current_directory = os.getcwd()

    def do_quit(self, line):
        """Quits the program."""
        return True

    def postcmd(self, stop, line):
        print()  
        return stop

if __name__ == '__main__':
    OpenWeatherCLI().cmdloop()
