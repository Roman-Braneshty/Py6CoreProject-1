# Py6CoreProject №1
![command bot](https://img.shields.io/pypi/pyversions/pyth?color=orange&label=Command%20Bot&logo=R)
![lic](https://img.shields.io/pypi/l/clu?color=orange&label=Py6Core%20Group%E2%84%961%20License&logo=R)
![bot work](https://img.shields.io/github/commit-activity/m/Roman-Braneshty/Py6CoreProject-1?color=orange&label=Bot%20Work&logo=R)
![start project](https://img.shields.io/date/1655672400?color=orange&label=start%20project)
## Group№1

### Roles:
___
1) **Team Lead** - **[Роман Бранешты](https://github.com/Roman-Braneshty)** 
2) **Scrum Master** - **[Екатерина Климентенко](https://github.com/klymentenkokate)**
3) **Technical Guide** - **[Александр Романюк](https://github.com/romaniuk-o)**

### Description of the bot:
Бот "Cli_assistant" создан для записи,редактирования и удаления\
контактов, а также отдельных заметок. \
Теперь ваше пользование адресной книгой станет ещё проще и продуктивнее.\
Вы не забудете свои действия в адресной книге, ведь\
с помощью заметок можете записывать каждую проделанную\
работу и помечать их ~~тегами~~ ключевыми словами.

### Instructions for install:
#### Install script on your pc:
    pip install -i https://test.pypi.org/simple/ cli-assis-teem01
#### Command for call:
    cli_assistant

### Instructions for start working with the bot:
При запуске бота выберите с какой веткой вы хотите работать\
(подробнее в консольном окне при запуске).\
После выбора ветки своей деятельности введите: **'help'**.\
Далее вам будут доступны все команды для вашей работы.\
Для возвращения на выбор веток своей работы введите: **'back'.**\
Для закрытия бота в меню выбора веток работы введите: **'X'**.
#### **P.s. Не переживайте, вся информация сохраняется автоматически.**

### All bot commands:
#### AdressBook commands:
| Commands       |             Enter              |                                                              Description |
|----------------|:------------------------------:|-------------------------------------------------------------------------:|
| help           |               -                |                                                    Выводит список команд |
| hello          |               -                |                                                    Приветствуется с вами |
| add            |    name, phone, (birthday)     |     создаёт контакта с Телефоном и датой рождения(может быть не введена) |
| new phone      |     name, phone, new phone     |                                           Меняет старый телефон на новый |
| show all       |               -                |                                                  Показывает все контакты |
| delete         |          name, phone           |                                          Удаляет номер телефона контакта |                                                                       
| birthday       |              name              |                                           Выводит дату рождения контакта |                                                                                 
| soon birthday  |      days before birthday      | Показывает контактов, у кого день рождение в течении заданных параметров |
| find           |         any arguments          |              Находит определённых контактов по имени/номеру/почте/адресу |                                            
| email          |          name, email           |                                            Добавляет почту для контактов |                                                                                 
| new email      |   name, old email, new email   |                                             Меняет старую почту на новую |                                                        
| new adress     | name, old address, new address |                                             Меняет старый адрес на новый |                                            
| adress         |         name, address          |          Добавляет адрес для контакта, формат адреса: city,street,number |                                       
| remove contact |              name              |                    Удаляет контакта и все его данные из контактной книги |  
 | back           |               -                |                                          Возвращает в выбор веток работы |
#### Notate commands:
| Commands    |          Enter          |                                                               Description |
|-------------|:-----------------------:|--------------------------------------------------------------------------:|
| help        |            -            |                                                     Выводит список команд |
| hello       |            -            |                                                     Приветствуется с вами |
| add         |          note           |                                         Добавляет заметки в Книгу Заметок |
| tag         | number of note and tags | Добавляет ~~теги~~ ключевые слова для заметок в формате 'tag1, tag2, ...' |
| del         | the number of the note  |                                     Удаляет заметку по порядковому номеру |
| del tag     | the number of the note  |                      Удаляет ~~теги~~ ключевые слова определённой заметки |
| change      | the number of the note  |                                             Изменяет определённую заметку |
| find notate |   text of the notate    |                                    Находит заметку по тексту и выводит её |
| find tag    |  tag(s) of the notate   |                  Находит заметку по ~~тегу~~ ключевому слову и выводит её |
| show        |            -            |                                                     Выводит Книгу Заметок |
| clear       |            -            |                                                     Очищает книгу заметок |
| back        |            -            |                                           Возвращает в выбор веток работы |

## License: 
The module is available as open source under the terms of the [Python6Core Group№1 License, Apache, Version 2.0 ](http://www.apache.org/licenses/)
