import pickle
from collections import UserDict
from pathlib import Path


class Field:
    def __init__(self, value: str) -> None:
        self.__value = None
        self.value = value

    def __str__(self) -> str:
        return f'{self.value}'

    def __eq__(self, other) -> bool:
        return self.value == other.value


class Text(Field):
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str) -> None:
        if value:
            self.__value = value
        else:
            self.__value = 'You have not entered any text'
        print(self.__value)

    def __str__(self) -> str:
        return f'{self.value}'


class Note:
    def __init__(self, name, text: str) -> None:
        self.text = text
        self.name = name

    def __str__(self):
        return f"Note: {self.name} {self.text}"


class NoteBook(UserDict):

    def __init__(self, filename: str) -> None:
        super().__init__()
        self.filename = Path(filename)
        if self.filename.exists():
            with open(self.filename, 'rb') as db:
                self.data = pickle.load(db)

    def save(self):
        with open(self.filename, 'wb') as db:
            pickle.dump(self.data, db)


def add_note(notates, *args):
    name = args[0]
    text = ' '.join(args)
    note = Note(text)
    return f'Text: {text} added to note {name}'


def close(notates, *args):
    notates.save()
    return 'Good bye!'


COMMANDS = {close: ['good bye', 'close', 'exit', '.'], add_note: ['add_note']}


def parse_command(user_input: str):
    for k, v in COMMANDS.items():
        for i in v:
            if user_input.lower().startswith(i.lower()):
                return k, user_input[len(i):].strip().split(" ")


def notates():
    notates = NoteBook(notebook.dat)
    while True:
        user_input = input(">>>")
        result, data = parse_command(user_input)
        print(result(notates, *data), '\n')
        if result is close:
            break





