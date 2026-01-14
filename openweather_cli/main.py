import cmd
import os
from api_funcs import *

class OpenWeatherCLI(cmd.Cmd):
    intro = """
============ OPENWEATHERCLI ============

To begin, type 'help' to list available commands.

========================================
    """    
    prompt = 'OpenWeatherCLI>> '
    
    def __init__(self):
        super().__init__()
        self.current_directory = os.getcwd()

    def do_searchname(self, arg):
        "Search for a city by name. EX: searchname Philadelphia"
        try:
            search_name(arg)
        except Exception as e:
            print("Error: Input was either forgotten or not found")

    def do_searchfav(self,arg):
        "Search for a city based off of favorites. EX: searchfav 1"
        try:
            search_favorites()
        except ValueError:
            print("Unable to search given the input")

    def do_listfav(self, arg):
        "List all user specified favorite cities. Takes no args"
        list_favorites()

    def do_addfav(self, arg):
        "Add a city to your favorites. EX: addfav New York"
        try:
            add_favorites(arg)
        except Exception as e:
            print("Error: Input was either forgotten or not found")

    def do_delfav(self, arg):
        "Delete a city from your favorites. Takes no args."
        delete_favorites()

    def do_quit(self, line):
        """Quits the program."""
        return True

    def postcmd(self, stop, line):
        print()  
        return stop

if __name__ == '__main__':
    OpenWeatherCLI().cmdloop()
