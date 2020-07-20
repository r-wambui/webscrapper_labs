from apscheduler.schedulers.blocking import BlockingScheduler
import pymongo
import subprocess

sched = BlockingScheduler()

MONGO_URI = "mongodb+srv://analytics:nevermind@cluster0.ngveb.mongodb.net/<analytics_db>"
db = "analytics_db"

client = pymongo.MongoClient(MONGO_URI)



@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17, minute=41)
def scheduled_job():
    mongo_db = client[db]
    mongo_db["jobs"].remove()
    subprocess.call('./scrape.sh', shell=True)
    print("Finished daily run")
    
sched.start()