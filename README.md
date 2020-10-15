# Feigi Bot
Vk bot to get the schedule of Chuvash State University

<img src="images/feigibot.png">


## Contributing

For information security purposes, some configuration files have been added to the .gitignor, e.g. group token from the configuration directory.
To start programming, you need to add the files **database.py** and **group.py** to the directory **/config**.

database.py - information for connection to the database.
```py
DB_NAME = "feigibot"
DB_USER = ""
DB_PASSWORD = ""
DB_HOST = "127.0.0.1"
DB_PORT = 5432
```

group.py - information for binding bot to a group
```py
# bot vk group configurations
TOKEN = ""
GROUP_ID = 196517515
```
