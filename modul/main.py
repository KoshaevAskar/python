from menu import choice_pizza
from cost  import show_cost
from pay import pay
import time

def start():
    choice_pizza()
    time.sleep(2)
    show_cost()
    pay()
start()
