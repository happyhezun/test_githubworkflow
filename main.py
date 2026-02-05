from fastapi import FastAPI
from pymemcache.client.base import Client
import json

app = FastAPI()

memcached_client = Client('localhost', 11211)


def get_data_from_db(item_id: int):
    print("Fetching from databeae...")
    return {"item_id": item_id, "data": "Some expensive data"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    cache_key = f"item:{item_id}"
    cached_data = memcached_client.get(cache_key)
    if cached_data:
        print("Returning from cache...")
        return json.loads(cached_data)
    data = get_data_from_db(item_id)
    memcached_client.set(cache_key, json.dumps(data), expire=60)
    return data
