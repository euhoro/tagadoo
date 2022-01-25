import itertools
from collections import Counter
from typing import List, Dict

import uvicorn
from fastapi import FastAPI

from models import Term
from mongo_repo import MongoRepo

records_repository = MongoRepo()
app = FastAPI()


@app.get('/records', tags=["Records"])
def read_all() -> List[Term]:
    records = records_repository.get_all_records('NLP', 'TERMS')
    return records


@app.get('/records/{id}', tags=["Records"], response_model=Dict[str, int])
def read_one(id: int) -> dict:
    records = records_repository.get_one_grouped('NLP', 'TERMS', id)
    return records


@app.get('/', tags=["Records"], response_model=str)
def root():
    return 'tagado## - use /docs /records /records_py'


@app.get('/records_py/{id}', tags=["Records"], response_model=Dict[str, int])
def read_one(id: int) -> List[Term]:
    records = records_repository.get_all_records('NLP', 'TERMS')
    records_filtered = [term.terms for term in records if term.type == id]
    all_terms = list(itertools.chain.from_iterable(records_filtered))
    return Counter(all_terms)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8080, debug=True)
