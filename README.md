# Бот-помічник з консольним інтерфейсом
## Запуск
У папці з проектом запустіть `main.py`:
```cmd
python main.py
```
## Налаштування 
* Конфігурація задаються у файлі `settings.json`
* Діалог зберігається до файлу `./dialogue-{time/date}.txt`. Також, він дублюється у файл, вказаний у полі `"logPath"` .
* Ім'я бота вказується у полі `"botName"`

## Правила додавання нових тем і функцій

### Загальні
* Потрібно наслідуватися від `BaseStrategy`, та базуватися на ініціалізації від нього: `super().__init__(parent)`
* Ініціалізуйте поле `self.name` для стандартного повідомлення про вибір теми, операції
АБО перевантажте метод `writeStarter` 
* Користуйтеся лише методом `self.print` для виводу бота (обробляє логування)

```python
class YourStrategy(BaseStrategy):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.name = "назва елемента"

    def writeStarter(self):
        self.print("Власний текст")

```


### Для теми
 * Можна перевантажити метод `writeTopics` для зміни повідомлення виводу підтем, операцій з стандартного на власний
 * Підтеми і операції разом із назвами необхідно вказати y словнику `self.topics`
```python
class YourStrategy(BaseStrategy):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.topics = {
            'підтема': FooStrategy(self),
            'операція': BarStrategy(self),
        }

    def writeStarter(self):
        self.print("Текст в темі")

    def writeTopics(self):
        self.print(f"Власний перелік підтем: {str.join(', ', self.topics)}.")
```
## Для операції
* Встановіть поле `self.isOperation = True`
*  поле `self.isOperation = True`
* Перевантажте метод `processInput` для визначення операції. Він буде викликаний після виклику `writeStarter` і вводом користувачем вхідних данних
* Ввід користувача знаходиться y `self.input`
```python
class OpStrategy(BaseStrategy):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.name = "операція"
        self.isOperation = True

    def processInput(self):
        self.print(f"Ввід користувача - {self.input}")
```
* Якщо не потрібен ввід данних, встановіть `self.needInput = False` для уникнення очукування вводу
```python
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.name = "операція"
        self.isOperation = True
        self.needInput = False
```
