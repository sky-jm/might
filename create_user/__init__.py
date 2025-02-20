from mite.datapools import RecyclableIterableDataPool
import uuid
from mite_http import mite_http

datapool = RecyclableIterableDataPool([(i, i+2) for i in range(5000)])

def create_user_scenario():
    return [["create_user:create_user_journey", datapool, lambda start, end: 100]]

@mite_http
async def create_user_journey(ctx, arg1, arg2):
    username = uuid.uuid4().hex
    async with ctx.transaction("Create user"):
        await ctx.http.post(ctx.config.get("app_url") + "/users/create",
                            json={"username": username, "password": "test1234"})

        ctx.send("data_created", name="users", data={"username": username})
