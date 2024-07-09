import json
from pymongo import MongoClient
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime, timedelta
MONGO_URI = "mongodb://localhost:27017/"
MONGO_DB = "mqtt_data"
MONGO_COLLECTION = "status_messages"

app = FastAPI()

mongo_client = MongoClient(MONGO_URI)
db = mongo_client[MONGO_DB]
collection = db[MONGO_COLLECTION]

class TimeRange(BaseModel):
    start_time: datetime
    end_time: datetime

@app.post("/count")
def status_count(time_range: TimeRange):
    if time_range.start_time >= time_range.end_time:
        raise HTTPException(status_code=400, detail="Start time must be less than end time")

    pipeline = [
        {"$match": {"timestamp": {"$gte": time_range.start_time, "$lte": time_range.end_time}}},
        {"$group": {"_id": "$status", "count": {"$sum": 1}}}
    ]
    result = list(collection.aggregate(pipeline))
    return {str(doc["_id"]): doc["count"] for doc in result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)