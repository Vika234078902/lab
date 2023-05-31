import os
import string
import time
from strategy import Strategy
import datetime
import random
import math
from colorama import Back, Fore, init
init()


class BaseStrategy(Strategy):
    def __init__(self, parent: 'Strategy') -> None:
        self.parent = parent
        self.botName = parent.botName
        self.logPath = parent.logPath
        self.logName = parent.logName

    def writeWow(self):
        if random.random() < 0.3:
            self.print(f"Вау! {self.name} - це круто!")

    def writeStarter(self):
        self.print(f"Ви обрали {self.name}.")


class InitStrategy(Strategy):
    def __init__(self, settings: dict) -> None:
        super().__init__(settings)
        self.topics = {
            'математика': MathStrategy(self),
            'фізика': PhysicsStrategy(self),
            'філологія': PhilologyStrategy(self),
            'географія': GeographyStrategy(self),
            'робота з текстом': TextStrategy(self),
            'загальні': GeneralStrategy(self),
            'інші':  OthersStrategy(self),
        }
        self.parent = self

    def writeStarter(self):
        self.print(f"Вітаю, мене звати {self.botName}.")

    def writeTopics(self):
        self.print(
            f"Ви можете задати мені питання з наступних тем: {str.join(Back.RESET+Fore.RESET+', '+Back.BLUE+Fore.WHITE, self.topics)}.")

############################################################################################################


class MathStrategy(BaseStrategy):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.name = 'математика'
        self.topics = {
            "квадратне рівняння": SeqStrategy(self),
            "площа трапеції": TrapStrategy(self),
            "число пі": PiStrategy(self),
            "знаходження центру кола": CircleStrategy(self),
        }

    def writeTopics(self):
        self.print(
            f"Вам доступні наступні обрахунки: {str.join(Back.RESET+Fore.RESET+', '+Back.BLUE+Fore.WHITE, self.topics)}.")
############# ----------------------------------------------------------#################


class SeqStrategy(BaseStrategy):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.name = "розв'язання квадратного рівняння"
        self.isOperation = True

    def writeStarter(self):
        self.print(f"Ви обрали {self.name}.")
        self.print("Введіть коофіцієнти a, b, c через пробіл.")

    def processInput(self):
        a, b, c = [float(i) for i in self.input.split()]
        if (b**2 - 4*a*c) > 0:
            self.print("Відповідь: " + Back.CYAN + Fore.WHITE + str((-b + (b**2 - 4*a*c)
                       ** 0.5)/(2*a)) + ", " + str((-b - (b**2 - 4*a*c)**0.5)/(2*a)))
        elif (b**2 - 4*a*c) == 0:
            self.print("Відповідь: " + Back.CYAN + Fore.WHITE + str(-b/(2*a)))
        else:
            self.print("Відповідь: " + Back.CYAN +
                       Fore.WHITE + "Немає дійсних коренів.")


class TrapStrategy(BaseStrategy):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.name = "знаходження площі трапеції"
        self.isOperation = True

    def writeStarter(self):
        self.print(f"Ви обрали {self.name}.")
        self.print("Введіть сторони основ і висоту через пробіл -  a, b, h:")

    def processInput(self):
        a, b, h = [float(i) for i in self.input.split()]
        self.print("Відповідь: " + Back.CYAN + Fore.WHITE + str((a+b)*h/2))


class CircleStrategy(BaseStrategy):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.name = "знаходження центру кола"
        self.isOperation = True

    def writeStarter(self):
        self.print(f"Ви обрали {self.name}.")
        self.print(
            "Введіть координати трьох точок на колі через пробіл (6 чисел):")

    def processInput(self):
        x1, y1, x2, y2, x3, y3 = [float(i) for i in self.input.split()]

        x0 = ((x1**2 + y1**2)*(y2-y3) + (x2**2 + y2**2)*(y3-y1) + (x3**2 +
              y3**2)*(y1-y2)) / (2*(x1*(y2-y3) - y1*(x2-x3) + x2*y3 - x3*y2))
        y0 = ((x1**2 + y1**2)*(x3-x2) + (x2**2 + y2**2)*(x1-x3) + (x3**2 +
              y3**2)*(x2-x1)) / (2*(x1*(y2-y3) - y1*(x2-x3) + x2*y3 - x3*y2))

        self.print("Відповідь: " + Back.CYAN + Fore.WHITE + str((x0, y0)))


class PiStrategy(BaseStrategy):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.name = "виведення числа пі"
        self.isOperation = True
        self.needInput = False

    def processInput(self):
        self.print("Відповідь: " + Back.CYAN + Fore.WHITE + str(math.pi))

############################################################################################################


class PhysicsStrategy(BaseStrategy):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.name = 'фізика'
        self.topics = {
            "закон Стефана-Больцмана": BoltsmanStrategy(self),
            "гравітаційна стала": GStrategy(self),
            "кулонівська стала": KStrategy(self),
        }

    def writeTopics(self):
        self.print(
            f"Вам доступні наступні обрахунки: {str.join(Back.RESET+Fore.RESET+', '+Back.BLUE+Fore.WHITE, self.topics)}.")
############# ----------------------------------------------------------#################


class BoltsmanStrategy(BaseStrategy):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.name = 'Обрахунок за законом Стефана-Больцмана'
        self.isOperation = True

    def writeStarter(self):
        self.print("Ви обрали обрахунок потужності за законом Стефана-Больцмана.")
        self.print(
            "Введіть температуру в Кельвінах та площу поверхні в метрах квадратних через пробіл.")

    def processInput(self):
        t, s = [float(i) for i in self.input.split()]
        self.print("Відповідь: " + Back.CYAN +
                   Fore.WHITE + str(5.6704e-8 * t**4 * s))


class GStrategy(BaseStrategy):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.name = 'виведення гравітаційної сталої'
        self.isOperation = True
        self.needInput = False

    def processInput(self):
        self.print("Відповідь: " + Back.CYAN + Fore.WHITE + str(6.6738480e-11))


class KStrategy(BaseStrategy):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.name = 'виведення кулонівської сталої'
        self.isOperation = True
        self.needInput = False

    def processInput(self):
        self.print("Відповідь: " + Back.CYAN +
                   Fore.WHITE + str(8.987742438e+9))


############################################################################################################
class GeographyStrategy(BaseStrategy):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.name = 'географія'
        self.topics = {
            "найбільше в світі озеро": LakeStrategy(self),
            "відстань між точками": PathStrategy(self),
        }

    def writeTopics(self):
        self.print(
            f"Вам доступні наступні обрахунки: {str.join(Back.RESET+Fore.RESET+', '+Back.BLUE+Fore.WHITE, self.topics)}.")
############# ----------------------------------------------------------#################


class LakeStrategy(BaseStrategy):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.name = 'дізнатися, яке найбільше в світі озеро?'
        self.isOperation = True
        self.needInput = False

    def processInput(self):
        self.print("Відповідь: " + Back.CYAN + Fore.WHITE +
                   "Каспійське море, його площа - 371 000 км²")


class PathStrategy(BaseStrategy):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.name = 'відстань між точками'
        self.isOperation = True

    def writeStarter(self):
        self.print("Ви обрали обрахунок відстані між точками.")
        self.print("Введіть координати двох точок через пробіл (4 числа):")

    def processInput(self):
        x1, y1, x2, y2 = [float(i) for i in self.input.split()]
        self.print("Відповідь: " + Back.CYAN + Fore.WHITE +
                   str(math.sqrt((x1-x2)**2 + (y1-y2)**2)))

############################################################################################################


class PhilologyStrategy(BaseStrategy):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.name = 'філологія'
        self.topics = {
            "часи в англійській мові": EngTimeStrategy(self),
            "питальні речення в англійській мові": EngQuestionStrategy(self),
        }

    def writeTopics(self):
        self.print(
            f"Вам доступні наступні теми: {str.join(Back.RESET+Fore.RESET+', '+Back.BLUE+Fore.WHITE, self.topics)}.")
############# ----------------------------------------------------------#################


class EngTimeStrategy(BaseStrategy):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.name = 'часи в англійській мові'
        self.isOperation = True
        self.needInput = False

    def writeStarter(self):
        self.print("Які часи в англійській мові?")

    def processInput(self):
        self.print("Відповідь: " + Back.CYAN + Fore.WHITE + "Present Simple, Present Continuous, Present Perfect, Present Perfect Continuous, Past Simple, Past Continuous, Past Perfect, Past Perfect Continuous, Future Simple, Future Continuous, Future Perfect, Future Perfect Continuous")


class EngQuestionStrategy(BaseStrategy):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.name = 'питальні речення в англійській мові'
        self.isOperation = True
        self.needInput = False

    def writeStarter(self):
        self.print("Як утворюються питальні речення в англійській мові?")

    def processInput(self):

        self.print(Back.CYAN + Fore.WHITE + """Речення утворюються за допомогою допоміжних слів та основного дієслова - див. таблицю нижче.
        +----------------+----------------+----------------+----------------+
        |                | Present Simple | Present        | Present Perfect|
        |                |                | Continuous     |                |
        +----------------+----------------+----------------+----------------+
        | Do             | Do             | Am             | Have           |
        | Does           | Does           | Is             | Has            |
        | Did            | Did            | Was            | Had            |
        +----------------+----------------+----------------+----------------+
        |                | Past Simple    | Past           | Past Perfect   |
        |                |                | Continuous     |                |
        +----------------+----------------+----------------+----------------+
        | Did            | Did            | Was            | Had            |
        +----------------+----------------+----------------+----------------+
        |                | Future Simple  | Future         | Future Perfect |
        |                |                | Continuous     |                |
        +----------------+----------------+----------------+----------------+
        | Will           | Will           | Will           | Will           |
        | Shall          | Shall          | Shall          | Shall          |
        +----------------+----------------+----------------+----------------+
        """)


############################################################################################################


class TextStrategy(BaseStrategy):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.name = 'роботу з текстовими файлами'
        self.topics = {
            "знайти паліндроми": PalindromStrategy(self),
            "вивести навпаки": ReverseStrategy(self),
            "вивести слова довше 10 символів": LongWordStrategy(self),
        }

    def writeTopics(self):
        self.print(
            f"Вам доступні наступні засоби роботи з текстовим файлом: {str.join(Back.RESET+Fore.RESET+', '+Back.BLUE+Fore.WHITE, self.topics)}.")

############# ----------------------------------------------------------#################


class PalindromStrategy(BaseStrategy):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.name = 'знайти паліндроми'
        self.isOperation = True

    def writeStarter(self):
        self.print(
            "Ви вибрали пошук паліндромів у тексті. Введіть ім'я вхідного файлу, та вихідного: ")

    def processInput(self):
        f1, f2 = self.input.split()
        with open(f1, 'r') as f:
            text = f.read()
            words = text.split()
        palindromes = []
        for word in words:
            if word == word[::-1]:
                palindromes.append(word)
        self.print("Відповідь: " + Back.CYAN +
                   Fore.WHITE + str.join(', ', palindromes))
        with open(f2, 'w') as f:
            f.write(str.join('\n', palindromes))


class ReverseStrategy(BaseStrategy):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.name = 'вивести навпаки'
        self.isOperation = True

    def writeStarter(self):
        self.print(
            "Ви вибрали виведення тексту навпаки. Введіть ім'я вхідного файлу, та вихідного: ")

    def processInput(self):
        f1, f2 = self.input.split()
        with open(f1, 'r') as f:
            text = f.read()
        self.print("Відповідь: " + Back.CYAN + Fore.WHITE + text[::-1])
        with open(f2, 'w') as f:
            f.write(text[::-1])


class LongWordStrategy(BaseStrategy):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.name = 'вивести слова довше 10 символів'
        self.isOperation = True

    def writeStarter(self):
        self.print(
            "Ви вибрали виведення слів довше 10 символів. Введіть ім'я вхідного файлу, та вихідного: ")

    def processInput(self):
        f1, f2 = self.input.split()
        with open(f1, 'r') as f:
            text = f.read()
            words = text.split()
        longWords = []
        for word in words:
            if len(word) > 10:
                longWords.append(word)
        self.print("Відповідь: " + Back.CYAN +
                   Fore.WHITE + str.join('\n', longWords))
        with open(f2, 'w') as f:
            f.write(str.join('\n', longWords))


class GeneralStrategy(BaseStrategy):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.name = 'загальні питання'
        self.topics = {
            "який рік": YearStrategy(self),
            "скільки до нового року": NewYearStrategy(self),
            "який зараз місяць": MonthStrategy(self),
            "гра": GameStrategy(self),
        }

    def writeStarter(self):
        self.print("Ви обрали загальні питання.")

    def writeTopics(self):
        self.print(
            f"Вам доступні наступні теми: {str.join(Back.RESET+Fore.RESET+', '+Back.BLUE+Fore.WHITE, self.topics)}.")

############# ----------------------------------------------------------#################


class YearStrategy(BaseStrategy):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.name = 'який рік'
        self.isOperation = True
        self.needInput = False

    def writeStarter(self):
        self.print("Ви обрали виведення поточного року.")

    def processInput(self):
        self.print("Відповідь: " + Back.CYAN + Fore.WHITE +
                   str(datetime.datetime.now().year))


class NewYearStrategy(BaseStrategy):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.name = 'скільки до нового року'
        self.isOperation = True
        self.needInput = False

    def writeStarter(self):
        self.print("Ви обрали виведення кількості днів до нового року.")

    def processInput(self):
        now = datetime.datetime.now()
        newYear = datetime.datetime(now.year + 1, 1, 1)
        self.print("Відповідь: " + Back.CYAN +
                   Fore.WHITE + str((newYear - now).days) + " днів")


class MonthStrategy(BaseStrategy):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.name = 'який зараз місяць'
        self.isOperation = True
        self.needInput = False

    def writeStarter(self):
        self.print("Ви обрали виведення поточного місяця.")

    def processInput(self):
        self.print("Відповідь: " + Back.CYAN + Fore.WHITE +
                   str(datetime.datetime.now().month))


class GameStrategy(BaseStrategy):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.name = 'гра'
        self.isOperation = True

    def writeStarter(self):
        self.print("Ви обрали гру. Вам потрібно відгадати число від 1 до 10.")

    def processInput(self):
        inputNumber = int(self.input)
        if inputNumber == 5:
            self.print(Back.GREEN + Fore.WHITE + "Вітаємо! Ви виграли!")
        else:
            self.print(Back.RED+Fore.YELLOW+"Невірно! Ви програли.")

############# ----------------------------------------------------------#################

class OthersStrategy(BaseStrategy):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.name = 'інші(додаткові) функції'
        self.topics = {
            "випадкове число": RandomIntStrategy(self),
            "unix-час": UnixStrategy(self),
            "випадкове слово": RandomWordStrategy(self),
            "вивести веселку": RainbowStrategy(self),
            "вивести вміст папки": FolderStrategy(self),
            "випадковий телефон": RandomPhoneStrategy(self),
            "випадкові кольори": RandomColorStrategy(self),
        }

    def writeTopics(self):
        self.print(f"Вам доступні наступні можливості: {str.join(Back.RESET+Fore.RESET+', '+Back.BLUE+Fore.WHITE, self.topics)}.")

############# ----------------------------------------------------------#################

class RandomIntStrategy(BaseStrategy):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.name = 'випадкове число'
        self.isOperation = True

    def writeStarter(self):
        self.print("Ви обрали виведення випадкового числа від a до b.")
        self.print("Введіть проміжок чисел [a;b] через пробіл:")

    def processInput(self):
        a, b = self.input.split()
        a, b = int(a), int(b)

        self.print("Відповідь: " + Back.CYAN + Fore.WHITE +
                   str(random.random() * (b - a) + a))

class UnixStrategy(BaseStrategy):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.name = 'виведення unix-часу.'
        self.isOperation = True
        self.needInput = False

    def processInput(self):
        self.print("Відповідь: " + Back.CYAN + Fore.WHITE +
                   str(int(time.time()))+" секунд")
        
class RandomWordStrategy(BaseStrategy):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.name = 'виведення випадкового слова'
        self.isOperation = True
        self.needInput = False

    def processInput(self):
        self.print("Відповідь: " + Back.CYAN + Fore.WHITE +
                   ''.join([random.choice(string.ascii_letters) for i in range(random.randint(4, 15))]))
        
class RainbowStrategy(BaseStrategy):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.name = 'виведення веселки'
        self.isOperation = True
        self.needInput = False

    def processInput(self):
        self.print(Fore.WHITE + Back.RED + "R" +  Back.YELLOW + "A" + Back.GREEN + "I" + Back.CYAN + "N" + Back.BLUE + "B" + Back.MAGENTA + "O" + Back.RED + "W")
        
        
class FolderStrategy(BaseStrategy):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.name = 'виведення вмісту папки'
        self.isOperation = True

    def processInput(self):
        path = self.input
        if not os.path.exists(path):
            self.print(Back.RED + Fore.YELLOW + "Такої папки не існує.")
            return

        self.print(Back.GREEN + Fore.WHITE + "Вміст папки:")
        for file in os.listdir(path):
            self.print(Back.CYAN + Fore.WHITE + file)
        
class RandomPhoneStrategy(BaseStrategy):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.name = 'виведення випадкового телефонного номеру.'
        self.isOperation = True
        self.needInput = False

    def processInput(self):
        self.print("Відповідь: " + Back.CYAN + Fore.WHITE +
                  "+380"+ ''.join([random.choice('0123456789') for i in range(9)]))

class RandomColorStrategy(BaseStrategy):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.name = 'виведення випадкового кольору'
        self.isOperation = True
        self.needInput = False

    def processInput(self):
        self.print("Відповідь: " + Back.CYAN + Fore.WHITE +
                  random.choice(list(vars(Back).values())) + " "*256)