# import time

# def sync_task(name, delay):
#     print(f"Starting {name}")
#     time.sleep(delay)  # Yeh block karta hai
#     print(f"Finished {name}")

# # Run karo
# start = time.time()
# sync_task("Task1", 1)
# sync_task("Task2", 1)
# sync_task("Task3", 1)
# end = time.time()
# print(f"Total time: {end - start} seconds")


# import asyncio
# import time

# async def async_task(name, delay):
#     print(f"Starting {name}")
#     await asyncio.sleep(delay)  # Yeh suspend karta hai, block nahi
#     print(f"Finished {name}")

# # Run karo (event loop chalaane ke liye)
# async def main():
#     start = time.time()
#     await asyncio.gather(  # Yeh multiple coroutines ko parallel run karta hai
#         async_task("Task1", 1),
#         async_task("Task2", 1),
#         async_task("Task3", 1)
#     )
#     end = time.time()
#     print(f"Total time: {end - start} seconds")

# # Event loop start karo
# asyncio.run(main())


# import asyncio
# import random

# # ----------- Fake async APIs / DB calls -------------
# async def fetch_user_profile():
#     await asyncio.sleep(2)  # slow API
#     return {"name": "Rahul", "age": 25}

# async def fetch_user_posts():
#     await asyncio.sleep(3)  # slower API
#     return ["post1", "post2", "post3"]

# async def fetch_user_settings():
#     await asyncio.sleep(1)  # fast DB read
#     return {"theme": "dark", "language": "en"}

# # -------------- Main Logic --------------------------
# async def main():
#     print("Loading dashboard...")

#     # 1️⃣ tasks ko background me start kr do
#     profile_task = asyncio.create_task(fetch_user_profile())
#     posts_task   = asyncio.create_task(fetch_user_posts())
#     settings_task = asyncio.create_task(fetch_user_settings())

#     # 2️⃣ ab hum unke finish hone ka wait krte hain
#     profile = await profile_task
#     posts = await posts_task
#     settings = await settings_task

#     # 3️⃣ final output
#     print("\n=== Dashboard ===")
#     print("User:", profile)
#     print("Posts:", posts)
#     print("Settings:", settings)

# asyncio.run(main())

# _____________________________________________________________
#without asyncio
# import time
# import asyncio

# start = time.time()

# def async_task():
#     print("start1 async_task1 ")
#     time.sleep(5)
#     print("end1 async_task1")

# def async_task2():
#     print("start2 async_task2 ")
#     time.sleep(3)
#     print("end2 async_task2")

# def async_task3():
#     print("start3 async_task3 ")
#     time.sleep(2)
#     print("end3 async_task3")

# async_task()
# async_task2()
# async_task3()

# end = time.time()

# print("process time taken :", end-start,"secs")

# _______________________________________________________________
# with asyncio

import time
import asyncio

start = time.time()
async def async_task():
    print("start1 async_task1 ")
    await asyncio.sleep(5)
    print("end1 async_task1")

async def async_task2():
    print("start2 async_task2 ")
    await asyncio.sleep(3)
    print("end2 async_task2")

async def async_task3():
    print("start3 async_task3 ")
    await asyncio.sleep(2)
    print("end3 async_task3")

async def main():
    await asyncio.gather(
        async_task(),
        async_task2(),    #this all functions now has corountine
        async_task3()

    )
    
asyncio.run(main())

end = time.time()

print("process time taken :", end-start,"secs")