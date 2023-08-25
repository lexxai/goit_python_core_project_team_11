# "Персональний помічник" – Assistant bot.

Персональний помічник допоможе Вам зберігати список Ваших контактів (телефон, email, дату народження, адресу),
робити нотатки та сортувати файли у вказаній директорії. Під час додавання або редагування інформації буде перевірятись правильного вводу телефонного номеру, email та дати народження.

За окремим запитом Помічник вміє виводити список контактів у котрих день народження приходиться протягом вказаної Вами кількості днів.

При створенні нотаток можливо додавання ключових слів, за якими можна проводити сортування та пошук. Сортування файлів у теці проводиться за типами файлів: аудіо-, відео-, документи, зображення, архіви, інше. Повний список команд виводиться після вводу "?".

Синтаксис кожної команди можливо переглянути задавши "?" через пробіл після команди.

- [Інструкція з встановлення програми](https://github.com/lexxai/goit_python_core_project_team_11/wiki/%D0%92%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BB%D0%B5%D0%BD%D0%BD%D1%8F-%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%B8)

- [Інструкція користувача](https://github.com/lexxai/goit_python_core_project_team_11/wiki/%D0%86%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%86%D1%96%D1%8F-%D0%BA%D0%BE%D1%80%D0%B8%D1%81%D1%82%D1%83%D0%B2%D0%B0%D1%87%D0%B0)

- [Підтримка користувачів](https://github.com/lexxai/goit_python_core_project_team_11/issues)

![image](https://github.com/lexxai/goit_python_core_project_team_11/assets/3278842/2bf37685-e950-4be4-838d-08d36b309cec)
![image](https://github.com/lexxai/goit_python_core_project_team_11/assets/3278842/f9ac1a44-6316-4789-9d3d-a7513eface25)

- YouTube video:

  - Презентація проєкту: https://youtu.be/ZYg62JWlqEw
  - Встановлленя додатку в середовищі Linux та приклад роботи додатку для презентації (v.0.6.0): https://youtu.be/oPinojZh5rg

- [README розробнику ](https://github.com/lexxai/goit_python_core_project_team_11/wiki/README-%D1%80%D0%BE%D0%B7%D1%80%D0%BE%D0%B1%D0%BD%D0%B8%D0%BA%D1%83)

# ABS Home Work 1

```
usage: assistant_bot [-h] [-u USERNAME] [-sort PATH] [-V] [-dar] [-dab] [--output_console {1,2,3,4}]

Assistant bot of GoIT project team 11

options:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        user name of the Assistant bot
  -sort PATH, --sorting PATH
                        run sorting commands for selected folder. Use path to folder as argument
  -V, --version         show version
  -dar, --disable_auto_restore
                        disable auto_restore
  -dab, --disable_auto_backup
                        disable auto_backup
  --output_console {1,2,3,4}
                        Output console (1: TERMINAL, 2: TERMINAL_RICH, 3: TELEGRAM, 4: VIBER), default: 2
```

`assistant_bot --output_console 1`

```
Enter your command >>>?
Send to TerminalOutput:
The full command syntax is available on request: command ? [Example: +a ?]
List of commands:
add address ('+a'), add address book ('+ab'), add birthday ('+b'), add email ('+e'), add note ('+n'), app version ('version'), backup ('bak'), change note ('=n'), change phone ('=p'), clear notes ('---n'), delete address ('-a'), delete all records ('---'), delete birthday ('-b'), delete email ('-e'), delete note ('-n'), delete phone ('-p'), delete user ('-'), export csv ('e csv'), hello, help ('?'), help full ('??'), import csv ('i csv'), list csv ('l csv'), next birthdays ('+nb'), quit ('exit','q'), restore ('res'), search address book ('?ab='), search notes ('?n='), show address ('?a'), show address book ('?ab'), show birthday ('?b'), show csv ('?csv'), show email ('?e'), show notes ('?n'), show page ('?pg'), show phone ('?p'), show versions ('?v'), sort folder ('sorting'), sort notes ('sn'), to birthday ('2b')

```

`assistant_bot --output_console 2`

```
Enter your command >>>?
Send to TerminalRichOutput


List of commands. The full command syntax is available on request: command ? [Example: +a ?]
Send to TerminalRichOutput

┏━━━━━━━━━━━━━━┳━━━━━━━┓┏━━━━━━━━━━━━━━┳━━━━━━━┓┏━━━━━━━━━━━━━━┳━━━━━━━┓┏━━━━━━━━━━━━━┳━━━━━━━┓┏━━━━━━━━━━━━━━┳━━━━━━━┓┏━━━━━━━━━━━━━━┳━━━━━━━┓
┃ Command      ┃ Alias ┃┃ Command      ┃ Alias ┃┃ Command      ┃ Alias ┃┃ Command     ┃ Alias ┃┃ Command      ┃ Alias ┃┃ Command      ┃ Alias ┃
┡━━━━━━━━━━━━━━╇━━━━━━━┩┡━━━━━━━━━━━━━━╇━━━━━━━┩┡━━━━━━━━━━━━━━╇━━━━━━━┩┡━━━━━━━━━━━━━╇━━━━━━━┩┡━━━━━━━━━━━━━━╇━━━━━━━┩┡━━━━━━━━━━━━━━╇━━━━━━━┩
│ add address  │ +a    ││ delete birt… │ -b    ││ show addres… │ ?ab   ││ import csv  │ i csv ││ search notes │ ?n=   ││ help full    │ ??    │
│ add address… │ +ab   ││ delete email │ -e    ││ show birthd… │ ?b    ││ list csv    │ l csv ││ show notes   │ ?n    ││ quit         │ exit… │
│ add birthday │ +b    ││ delete phone │ -p    ││ show email   │ ?e    ││ show csv    │ ?csv  ││ sort folder  │ sort… │├──────────────┼───────┤
│ add email    │ +e    ││ delete user  │ -     ││ show page    │ ?pg   │├─────────────┼───────┤│ sort notes   │ sn    ││ backup       │ bak   │
│ change phone │ =p    ││ next birthd… │ +nb   ││ show phone   │ ?p    ││ add note    │ +n    │├──────────────┼───────┤│ restore      │ res   │
│ delete addr… │ -a    ││ search addr… │ ?ab=  ││ to birthday  │ 2b    ││ change note │ =n    ││ app version  │ vers… ││ show versio… │ ?v    │
│ delete all … │ ---   ││ show address │ ?a    │├──────────────┼───────┤│ clear notes │ ---n  ││ hello        │       │└──────────────┴───────┘
└──────────────┴───────┘└──────────────┴───────┘│ export csv   │ e csv ││ delete note │ -n    ││ help         │ ?     │
                                                └──────────────┴───────┘└─────────────┴───────┘└──────────────┴───────┘

```

`assistant_bot --output_console 3`

```Enter your command >>>?
Send
The full command syntax is available on request: command ? [Example: +a ?]
List of commands:
add address ('+a'), add address book ('+ab'), add birthday ('+b'), add email ('+e'), add note ('+n'), app version ('version'), backup ('bak'), change note ('=n'), change phone ('=p'), clear notes ('---n'), delete address ('-a'), delete all records ('---'), delete birthday ('-b'), delete email ('-e'), delete note ('-n'), delete phone ('-p'), delete user ('-'), export csv ('e csv'), hello, help ('?'), help full ('??'), import csv ('i csv'), list csv ('l csv'), next birthdays ('+nb'), quit ('exit','q'), restore ('res'), search address book ('?ab='), search notes ('?n='), show address ('?a'), show address book ('?ab'), show birthday ('?b'), show csv ('?csv'), show email ('?e'), show notes ('?n'), show page ('?pg'), show phone ('?p'), show versions ('?v'), sort folder ('sorting'), sort notes ('sn'), to birthday ('2b') to Telegram
```

`assistant_bot --output_console 4`

```Send
The full command syntax is available on request: command ? [Example: +a ?]
List of commands:
add address ('+a'), add address book ('+ab'), add birthday ('+b'), add email ('+e'), add note ('+n'), app version ('version'), backup ('bak'), change note ('=n'), change phone ('=p'), clear notes ('---n'), delete address ('-a'), delete all records ('---'), delete birthday ('-b'), delete email ('-e'), delete note ('-n'), delete phone ('-p'), delete user ('-'), export csv ('e csv'), hello, help ('?'), help full ('??'), import csv ('i csv'), list csv ('l csv'), next birthdays ('+nb'), quit ('exit','q'), restore ('res'), search address book ('?ab='), search notes ('?n='), show address ('?a'), show address book ('?ab'), show birthday ('?b'), show csv ('?csv'), show email ('?e'), show notes ('?n'), show page ('?pg'), show phone ('?p'), show versions ('?v'), sort folder ('sorting'), sort notes ('sn'), to birthday ('2b') to Viber
```

