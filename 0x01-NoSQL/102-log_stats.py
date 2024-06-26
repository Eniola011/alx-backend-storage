#!/usr/bin/env python3
"""
Provide some stats about Nginx logs stored in MongoDB.
Add top 10 of the most present IPs
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_db = client.logs.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    total_logs = nginx_db.count_documents({})
    print(f'{total_logs} logs')

    print("Methods:")
    for method in methods:
        count_method = nginx_db.count_documents({'method': method})
        print(f'\tmethod {method}: {count_method}')

    # Number of documents with method=GET and path=/status
    status_check_count = nginx_db.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")

    # Calculate and Print the top 10 most present IPs
    print("IPs:")
    ips = nginx_db.aggregate([
        {"$group":
            {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
        },
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {
            "_id": 0,
            "ip": "$_id",
            "count": 1
        }}
    ])

    for ip in ips:
        print(f"\t{ip.get('ip')}: {ip.get('count')}")
