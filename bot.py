import json
from random import random
from strategy import Strategy 
from themes import *
from colorama import init, Fore, Back
init()

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Bot(metaclass=Singleton):
    
    strategy: Strategy
    
    def __init__(self) -> None:
        with open('settings.json', 'r') as f:
            self.settings =json.load(f)
                
    def setStrategy(self, strategy: Strategy):
        self.strategy = strategy
    
    def start(self):
        self.setStrategy(InitStrategy(self.settings)) 
        while True:
            self.strategy.writeStarter()
            
            if not self.strategy.isOperation:
                self.strategy.writeTopics()
                
            if not self.strategy.needInput and self.strategy.isOperation:
                self.strategy.setInput(None)
                self.setStrategy(self.strategy.parent)
            else:
                inp = input()
                self.strategy.log(inp, 'user')
                
                if inp == 'назад':
                    self.setStrategy(self.strategy.parent)
                    continue
                elif inp == 'вихід':
                    self.strategy.print("До побачення!")
                    break
                elif inp == 'допомога':
                    self.strategy.print(Back.GREEN+ Fore.LIGHTRED_EX +"Для виходу, напишіть «вихід». Для повернення до останньої теми напишіть «назад».")
                elif self.strategy.isOperation:
                    self.strategy.setInput(inp)
                    self.setStrategy(self.strategy.parent)
                elif inp in self.strategy.topics:
                    self.setStrategy(self.strategy.topics[inp])
                    self.strategy.writeWow()
                    continue
                else:
                    self.strategy.print(Back.LIGHTRED_EX+ Fore.YELLOW +"Помилка, такого варіанту вибору немає. Спробуйте ще раз.")
 