import logging
import os
import pymongo
import subprocess

from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

MONGO_URI = os.environ.get("MONGO_URI")
db = os.environ.get("MONGO_DATABASE")

client = pymongo.MongoClient(MONGO_URI)



@sched.scheduled_job('cron', day_of_week='mon-fri', hour=10, minute=40)
def scheduled_job():
    mongo_db = client[db]
    mongo_db["jobs"].remove()
    subprocess.call('./scrape.sh', shell=True)
    logging.debug("Finished daily run")
    
sched.start()