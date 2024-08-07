from templates.commons import decorator, qty_chars
from colorama import Fore


# Banner del sistema.
def banner():
    name_system = 'PyMarkTime-Console'
    spaces = qty_chars(name_system)
    print(Fore.BLUE)
    decorator()
    print('|' + ' ' * spaces + name_system + ' ' * spaces + '|')
    decorator()
    print(Fore.WHITE)
