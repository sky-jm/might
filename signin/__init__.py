import asyncio
import uuid

from mite_http import mite_http
from mite.datapools import RecyclableIterableDataPool, IterableDataPool
from msgpack import Unpacker

usernames = []
with open("recorder_data/users.msgpack", "rb") as handle:
    for msg in iter(Unpacker(handle, raw=False, use_list=False)):
        usernames.append((msg["username"],))
print("LENGTH =", len(usernames))

username_datapool = IterableDataPool(usernames)

@mite_http
async def signin(ctx, username):
    async with ctx.transaction("Log in"):
        await ctx.http.post(ctx.config.get("app_url") + "/users/login",
                            json={"username": username, "password": "test1234"})


def signin_scenario():
    return [["signin:signin", username_datapool, lambda start, end: 100]]

