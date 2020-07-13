from crontab import CronTab

my_cron = CronTab(user='your username')

job = my_cron.new(command='python /home/jay/writeDate.py')