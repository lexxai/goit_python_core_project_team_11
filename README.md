# goit_python_core_project_team_11

Школа GoIT. Курс Python Core. Куросва командна робота. Команада 11.

## Virtual environment

```
python -m venv .venv
.\.venv\Scripts\activate
```

### INSTALL PACKAGE

```
>pip list
Package    Version
---------- -------
pip        23.2.1
setuptools 65.5.0

>pip install .
Processing ..\goit_python_core_project_team_11
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Installing backend dependencies ... done
  Preparing metadata (pyproject.toml) ... done
Building wheels for collected packages: assistant-bot
  Building wheel for assistant-bot (pyproject.toml) ... done
  Created wheel for assistant-bot: filename=assistant_bot-0.1.0-py3-none-any.whl size=12443 sha256=07e66b2545bc1521395506e13b6e9832bf0ecfa4677c6684f196d9c329b77f5d
  Stored in directory: C:\Users\......c0792fdab6fa52ae179f8
Successfully built assistant-bot
Installing collected packages: assistant-bot
Successfully installed assistant-bot-0.1.0

>pip list
Package       Version
------------- -------
assistant-bot 0.1.0
pip           23.2.1
setuptools    65.5.0

>assistant_bot
Enter your command >>> ?
List of commands: add address ('+a'), add address book ('+ab'), add birthday ('+b'), add email ('+e'), add note ('+an'), backup ('bak'), change phone ('=p'), delete address ('-a'), delete all records ('---'), delete birthday ('-b'), delete email ('-e'), delete phone ('-p'), delete user ('-'), export csv ('e csv'), good bye ('close','exit','q','quit'), hello, help ('?'), import csv ('i csv'), list csv ('l csv'), list versions ('l v'), restore ('res'), search address book ('?ab='), show address ('?a'), show address book ('list address book','lab'), show birthday ('?b'), show csv ('?csv'), show email ('?e'), show notes ('?n'), show page ('?p'), show phone ('?p'), to birthday ('2b')
Enter your command >>> q
Goodbye. We are looking forward to seeing you again.
```

Якщо треба оновити пакет:

```
>pip install --upgrade .
Processing ...\goit_python_core_project_team_11
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Installing backend dependencies ... done
  Preparing metadata (pyproject.toml) ... done
Building wheels for collected packages: assistant-bot
  Building wheel for assistant-bot (pyproject.toml) ... done
  Created wheel for assistant-bot: filename=assistant_bot-0.1.0-py3-none-any.whl size=12648 sha256=f126fbbb95ce70b4547a6b65357e877e4e44921ce70285cf8ee92298389e53ac
  Stored in directory: ...d0d301d91e4f7e5d08cbf7c0792fdab6fa52ae179f8
Successfully built assistant-bot
Installing collected packages: assistant-bot
  Attempting uninstall: assistant-bot
    Found existing installation: assistant-bot 0.1.0
    Uninstalling assistant-bot-0.1.0:
      Successfully uninstalled assistant-bot-0.1.0
Successfully installed assistant-bot-0.1.0
```

## TESTS

Тестування:

1. Використовується tests\test_a_bot.py
   файл для підключення пакету assistant_bot та створення екземпляра класу Assistant_bot
2. Тестуємо у теці _tests_ тому що тут же будуть записуватися файли серіалізації та експорту.
3. При створенні екземпляра класу Assistant_bot використана назва сесії (`session = "user-session-000001"`), тому всі файли будуть автоматично створені з префіксом назви сесії.
4. Щоб не додавати в ручну початкові значення для тестування. Команди виконуються через `api`, це емулює команди користувача: `assistant.api("add note", "Note 1", "#tag2", "#tag3")`
   (Вибачте я лежачий постійно вводити команди для тестування)
5. Тестуючи видаліть пакет якщо він був встановлений

```
pip uninstall assistant-bot
Found existing installation: assistant-bot 0.1.0
Uninstalling assistant-bot-0.1.0:
  Would remove:
    ...\goit_python_core_project_team_11\.venv\lib\site-packages\assistant_bot-0.1.0.dist-info\*
    ...\goit_python_core_project_team_11\.venv\lib\site-packages\assistant_bot\*
    ...\goit_python_core_project_team_11\.venv\scripts\assistant_bot.exe
Proceed (Y/n)?
  Successfully uninstalled assistant-bot-0.1.0
```

```
cd tests
python test_a_bot.py
api command 'add address book': Done
api command 'add email': Done
api command 'add address': Done
api command 'add birthday': Done
api command 'add note': Done
api command 'add note': Done
api command 'add note': Done
api command 'add note': Done
Enter your command >>>?
List of commands: add address ('+a'), add address book ('+ab'), add birthday ('+b'), add email ('+e'), add note ('+an'), backup ('bak'), change phone ('=p'), delete address ('-a'), delete all records ('---'), delete birthday ('-b'), delete email ('-e'), delete phone ('-p'), delete user ('-'), export csv ('e csv'), good bye ('close','exit','q','quit'), hello, help ('?'), import csv ('i csv'), list csv ('l csv'), list versions ('l v'), restore ('res'), search address book ('?ab='), show address ('?a'), show address book ('list address book','lab'), show birthday ('?b'), show csv ('?csv'), show email ('?e'), show notes ('?n'), show page ('?p'), show phone ('?p'), to birthday ('2b')
Enter your command >>> q
Goodbye. We are looking forward to seeing you again.
```

### COMMANDS

HELP:

```
Enter your command >>> help
List of commands: add address ('+a'), add address book ('+ab'), add birthday ('+b'), add email ('+e'), add note ('+an'), backup ('bak'), change phone ('=p'), delete address ('-a'), delete all records ('---'), delete birthday ('-b'), delete email ('-e'), delete phone ('-p'), delete user ('-'), export csv ('e csv'), good bye ('close','exit','q','quit'), hello, help ('?'), import csv ('i csv'), list csv ('l csv'), list versions ('l v'), restore ('res'), search address book ('?ab='), show address ('?a'), show address book ('list address book','lab'), show birthday ('?b'), show csv ('?csv'), show email ('?e'), show notes ('?n'), show page ('?p'), show phone ('?p'), to birthday ('2b')
```

HELP за частиною команди:

```
Enter your command >>> add
List of commands: add address ('+a'), add address book ('+ab'), add birthday ('+b'), add email ('+e'), add note ('+an')
Enter your command >>> show
List of commands: show address ('?a'), show address book ('list address book','lab'), show birthday ('?b'), show csv ('?csv'), show email ('?e'), show notes ('?n'), show page ('?p'), show phone ('?p')
```

HELP для параметрів команди:

```
Enter your command >>> add birthday ?
Add or replace the user's birthday. Required username, birthday, please use ISO 8601 date format
```

Помилки:

```
Enter your command >>> add birthday ?
Add or replace the user's birthday. Required username, birthday, please use ISO 8601 date format
Enter your command >>> add birthday
Sorry, there are not enough parameters or their value may be incorrect tuple index out of range. Please use the help for more information.
Enter your command >>> list address book
name: Jon-00, phones: +38044333223;+38044333221, email: jon05@example.com, address: вул. Ворота Гетьмана, буд. 02, офіс. 121-344, birthday: 1999-08-11
Enter your command >>> add birthday Jon-00
Sorry, there are not enough parameters or their value may be incorrect tuple index out of range. Please use the help for more information.
Enter your command >>> add birthday Jon-00 9999-999
Sorry, there are not enough parameters or their value may be incorrect Invalid isoformat string: '9999-999'. Please use the help for more information.
Enter your command >>> add birthday Jon-00 2001-03-05
Done
Enter your command >>> list address book
name: Jon-00, phones: +38044333223;+38044333221, email: jon05@example.com, address: вул. Ворота Гетьмана, буд. 02, офіс. 121-344, birthday: 2001-03-05
```

Аліаси команд:

```
Enter your command >>> show
List of commands: show address ('?a'), show address book ('list address book','lab'), show birthday ('?b'), show csv ('?csv'), show email ('?e'), show notes ('?n'), show page ('?p'), show phone ('?p')
Enter your command >>> lab
name: Jon-00, phones: +38044333223;+38044333221, email: jon05@example.com, address: вул. Ворота Гетьмана, буд. 02, офіс. 121-344, birthday: 2001-03-05
Enter your command >>> ?b Jon-00
2001-03-05
Enter your command >>> ?n
1: note: Note 1, tags: tag1 #tag2
2: note: Note 2, tags: tag1 #tag2
3: note: Note 1, tags: tag1 #tag2
4: note: Note 1, tags: tag2 #tag3
Enter your command >>> q
Goodbye. We are looking forward to seeing you again.

```
