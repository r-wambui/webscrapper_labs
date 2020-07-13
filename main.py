import os
from flask import Flask
from flask_pymongo import PyMongo

import json
from bson import json_util

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/analytics_db"
mongo = PyMongo(app)


@app.route('/jobs', methods=["GET"])
def get_jobs():
    jobs_query = mongo.db.jobs.find()
    all_jobs = []
    if jobs_query.count() is not 0:
        for job in jobs_query:
            all_jobs.append({
                "id":job["_id"],
                "Job_titile":job["job_title"],
                "Company": job["company"],
                "Location": job["location"],
                "Time_posted": job["time_posted"]
            })
        return json.dumps(all_jobs, default=str), 200
    else:
        return "No jobs available", 404

@app.route('/jobs/<title>', methods=["GET"])
def search_job(title):
    search_query = mongo.db.jobs.find({ "$text": {"$search": title}})
    print("----", search_query.count())
    results = []
    if search_query.count() is not 0:
        for job_search in search_query:
            results.append({
                "id":job_search["_id"],
                "Job_titile":job_search["job_title"],
                "Company": job_search["company"],
                "Location": job_search["location"],
                "Time_posted": job_search["time_posted"]
            })
        return json.dumps(results, default=str), 200
    else:
        return {"error": "No such jobs available"}, 404

@app.route('/tenders', methods=["GET"])
def get_tenders():
    tenders_query = mongo.db.tenders.find()
    all_tenders = []
    if tenders_query.count() is not 0:
        for tender in tenders_query:
            all_tenders.append({
                "tender_code": tender["tender_code"],
                "tender_type": tender["tender_type"],
                "organisation_name": tender["org_name"],
                "tender_title": tender["tender_title"],
                "reference_no": tender["tender_reference_no"],
                "publication_date": tender["publication_date"],
                "closing_date": tender["closing_date"]
            })
        return json.dumps(all_tenders, default=str), 200
    else:
        return "No tenders available", 404

@app.route('/tenders/<title>', methods=["GET"])
def search_tender(title):
    search_query = mongo.db.tenders.find({ "$text": {"$search": title}})
    results = []
    if search_query.count() is not 0:
        for search in search_query:
            results.append({
                "tender_code": search["tender_code"],
                "tender_type": search["tender_type"],
                "organisation_name": search["org_name"],
                "tender_title": search["tender_title"],
                "reference_no": search["tender_reference_no"],
                "publication_date": search["publication_date"],
                "closing_date": search["closing_date"]
            })
        return json.dumps(results, default=str), 200
    else:
        return {"error": "No such jobs available"}, 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get("PORT", 5000))