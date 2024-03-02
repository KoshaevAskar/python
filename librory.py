# import cowsay
# cowsay.cow('Hello World')
# print(cowsay.get_output_string('cow', 'Hello World'))
# from colorama import Fore, Back, Style
# print(Fore.MAGENTA + 'some blue retext')
# print(Fore.BLUE + 'and with a green background')
# print(Fore.RED + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')
import time
from progress.spinner import MoonSpinner
bar = MoonSpinner('загрузка', max=100)
for i in range(101):
    time.sleep(0.1)
    bar.next()
bar.finish()
