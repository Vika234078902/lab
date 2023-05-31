import datetime
import os
from colorama import init, Fore, Back, colorama_text
import json
import re
init()

class Strategy:
    name: str
    settings: dict
    parent: 'Strategy'
    topics: dict = {}
    botName: str = 'Lab-GPT'
    isOperation: bool = False
    needInput: bool = True

    def __init__(self, settings: dict) -> None:
        
        if 'botName' in settings:
            self.botName = settings['botName']
        self.logName = 'dialogue-'+str(datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")) + '.txt'  
        if 'logPath' in settings:
            self.logPath = settings['logPath']
        else:
            self.logPath = './log_copy.txt'
        
    
    def _clear(self, line):
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        return ansi_escape.sub('', line)
    
    def print(self, msg: str):
        print(Back.LIGHTWHITE_EX + Fore.CYAN + msg + Fore.RESET+Back.RESET)
        self.log(self._clear(msg), 'bot')
    
    def log(self, msg: str, sender: str):
            
        with open(os.path.join(self.logName), 'a', encoding="utf-8") as f:
            f.write(sender + ': ' + msg + '\n')
        with open(os.path.join(self.logPath), 'a', encoding="utf-8") as f:
            f.write(sender + ': ' + msg + '\n')
        
    def writeWow(self):
        ...
        
    def setInput(self, inp: str):
        self.input = inp
        self.processInput()
    
    def processInput(self):
        ... 
    
    def writeStarter(self):
        raise NotImplementedError("writeStarter not implemented")
    
    def writeTopics(self):
        self.print(str.join(', ', self.topics))
        