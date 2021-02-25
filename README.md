# WAPL

## Download

python >= 3.6

```
pip install wapl
```

Solve SSL Error https://stackoverflow.com/questions/54135206/requests-caused-by-sslerrorcant-connect-to-https-url-because-the-ssl-module

## Testing example

### Login and enter space example
```
from wapl import WAPL
from time import sleep

# your webdriver path
bot = WAPL('C:/Users/Downloads/chromedriver_win32/chromedriver.exe')

sleep(5)

# login by id, pw
bot.login(id, pw)

sleep(5)

# enter space
bot.enter_space_by_name('tmax')
```

### App interactions
#### Navbar click
```
bot.goto_friends_list()

bot.goto_rooms_list()

bot.goto_mail_list()
```
#### Room
```
# enter first room
bot.goto_nth_room(0)
```

#### Talk
```
# Send talk message (!you must be in room)
bot.send_talk_msg('hi')
```
