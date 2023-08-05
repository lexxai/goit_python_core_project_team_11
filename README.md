# goit_python_core_project_team_11

Школа GoIT. Курс Python Core. Куросва командна робота. Команада 11.

## Virtual environment

```
python -m venv .venv
.\.venv\Scripts\activate
```

### INSTALL PACKAGE

```
(.venv) > pip list
Package    Version
---------- -------
pip        23.2.1
setuptools 65.5.0

(.venv) > pip install .
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

(.venv) > assistant_bot
Enter your command >>> ?
List of commands: add address ('+a'), add address book ('+ab'), add birthday ('+b'), add email ('+e'), add note ('+an'), backup ('bak'), change phone ('=p'), delete address ('-a'), delete all records ('---'), delete birthday ('-b'), delete email ('-e'), delete phone ('-p'), delete user ('-'), export csv ('e csv'), good bye ('close','exit','q','quit'), hello, help ('?'), import csv ('i csv'), list csv ('l csv'), list versions ('l v'), restore ('res'), search address book ('?ab='), show address ('?a'), show address book ('list address book','lab'), show birthday ('?b'), show csv ('?csv'), show email ('?e'), show notes ('?n'), show page ('?p'), show phone ('?p'), to birthday ('2b')
Enter your command >>> q
Goodbye. We are looking forward to seeing you again.
```

Якщо треба оновити пакет:

```
(.venv) > pip install --upgrade .
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

## EXPORT PACKAGE (.whl)

```
(.venv) > pip install build
Collecting build
  Using cached build-0.10.0-py3-none-any.whl (17 kB)
Collecting packaging>=19.0 (from build)
  Using cached packaging-23.1-py3-none-any.whl (48 kB)
Collecting pyproject_hooks (from build)
  Using cached pyproject_hooks-1.0.0-py3-none-any.whl (9.3 kB)
Collecting colorama (from build)
  Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Installing collected packages: pyproject_hooks, packaging, colorama, build
Successfully installed build-0.10.0 colorama-0.4.6 packaging-23.1 pyproject_hooks-1.0.0

(.venv) > pip list
Package         Version
--------------- -------
build           0.10.0
colorama        0.4.6
packaging       23.1
pip             23.2.1
pyproject_hooks 1.0.0
setuptools      65.5.0

(.venv) > dir /B dist
assistant_bot-0.1.0-py3-none-any.whl
assistant_bot-0.1.0.tar.gz

(.venv) >pip install dist\assistant_bot-0.1.0-py3-none-any.whl
Processing .... goit_python_core_project_team_11\dist\assistant_bot-0.1.0-py3-none-any.whl
Installing collected packages: assistant-bot
Successfully installed assistant-bot-0.1.0

(.venv) >pip list
Package         Version
--------------- -------
assistant-bot   0.1.0
build           0.10.0
colorama        0.4.6
packaging       23.1
pip             23.2.1
pyproject_hooks 1.0.0
setuptools      65.5.0

(.venv) >deactivate
> assistant_bot
Enter your command >>> ?
List of commands: add address ('+a'), add address book ('+ab'), add birthday ('+b'), add email ('+e'), add note ('+n'), backup ('bak'), change phone ('=p'), delete address ('-a'), delete all records ('---'), delete birthday ('-b'), delete email ('-e'), delete phone ('-p'), delete user ('-'), export csv ('e csv'), good bye ('close','exit','q','quit'), hello, help ('?'), import csv ('i csv'), list csv ('l csv'), list versions ('l v'), restore ('res'), search address book ('?ab='), show address ('?a'), show address book ('list address book','lab'), show birthday ('?b'), show csv ('?csv'), show email ('?e'), show notes ('?n'), show page ('?pg'), show phone ('?p'), sort folder ('sorting'), to birthday ('2b')
Enter your command >>>

```

## TESTS

Тестування:

1. Використовується `tests\test_a_bot.py`
   файл для підключення пакету _assistant_bot_ та створення екземпляра класу _Assistant_bot_
2. Тестуємо у теці _tests_ тому що тут же будуть записуватися файли серіалізації та експорту.
3. При створенні екземпляра класу _Assistant_bot_ використана назва сесії (`session = "user-session-000001"`), тому всі файли будуть автоматично створені з префіксом назви сесії.
4. Щоб не додавати в ручну початкові значення для тестування. Команди виконуються через `api`, це емулює команди користувача: `assistant.api("add note", "Note 1", "#tag2", "#tag3")`
   (Вибачте я ледачий постійно вводити команди для тестування)
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

### BACKUP / RESTORE

1. Automatic mode on start/end.
   Автоматичний режим може бути вимкнений при створенні об'єкту класу `Assistant_bot`, за замовчуванням він ввімкнутий.

   ```
      asistant = Assistant_bot(id=session, auto_restore=False, auto_backup=False)

   ```

2. Automatic backup mode після операцій що змінюють данні.
   Через декоратори: `@backup_data_address_book`, `@backup_data_note`

3. Manual

   - через команду: `backup ('bak')` - збереження резервної копії

     ```
     Enter your command >>> backup ?
     Backup all records. Optional parameter is the version. P.S. it done automatically after any changes on records
     Enter your command >>> backup 3
     Done
     ```

   - через команду: `restore ('res')` - відновлення резервної копії

     ```
     Enter your command >>> restore ?
     Restore all records. Optional parameter is the version.
     Enter your command >>> restore 3
     Done
     ```

   - через команду: `list versions ('l v')` - список версій резервних копій

     ```
     Enter your command >>> list versions
     version: 1
     version: 2
     version: 3
     ```

     Локальні файли при цьому такі:

     ```
     (.venv) ..\tests> dir /B \*.bin
     user-session-000001_assistant_bot.bin
     user-session-000001_assistant_bot_1.bin
     user-session-000001_assistant_bot_2.bin
     user-session-000001_assistant_bot_3.bin
     ```
