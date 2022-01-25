from typing import List

import pymongo

from models import Term


class MongoRepo:
    def __init__(self):
        conn = "mongodb+srv://developer:{password}@cluster0.juo1t.mongodb.net/NLP?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
        host_conn = conn.format(password="devo1234")
        self.client = pymongo.MongoClient(host=host_conn, connect=False)

    def get_all_records(self, db, collection) -> List[Term]:
        result = list(self.client[db][collection].find({}))
        return [Term(**x) for x in result]

    def get_one_grouped(self, db, collection, id):
        result = self.client[db][collection].aggregate([
            {"$match": {"type": id}},
            {"$unwind": "$terms"},
            {"$group": {"_id": "$terms", "count": {"$sum": 1}}}
        ])
        res = dict([(r['_id'], r['count']) for r in result])
        return res
