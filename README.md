# ShitPosterBot
Telegram bot to send a daily, random image on Telegram

## Basic usage
`admins.txt` contains the admins chat ids, who can send photos. `groups.txt` contains the groups which receive the random photo. You can get add yourself to the admins by sending your password to the bot. You can add a group to the bot by sending `/here` in the group.
Leave `admin.py` running costantly, and set up a cronjob to send the daily pic.
### admin.py usage
```
python3 admin.py -t '[TOKEN]' -d 'memes/' -p password
```
### bot.py cron job
```
0 14 * * * pkill -f admin.py; cd [ShitPosterBotDir]; python3 bot.py -t '[TOKEN]' -p 'memes/' > py.log 2> error.log
``` 
This sends a meme every day at 14:00. Make sure to restart admin.py after sending it. (Telegram wants a single active session).
