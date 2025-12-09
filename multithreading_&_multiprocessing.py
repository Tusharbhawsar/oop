# # Multithreading in Python allows multiple threads (smaller units of a process) to run concurrently,
# #  enabling efficient multitasking. It is especially useful for I/O-bound tasks like file handling,
# #  network requests, or user interactions.

# # What is a Process?
# # A process is an executing program with:

# # Program code (instructions to run)
# # Data (variables, buffers, workspace)
# # Execution context (state of the process)
# # What is a Thread?
# # A thread is the smallest unit of execution inside a process.

# # A process can have multiple threads.
# # Threads share the same code and global data but have their own registers and local variables (stack).
# # Think of a thread as a lightweight subprocess.

# # How Multithreading Works
# # On single-core CPUs, Python achieves concurrency using context
# #  switching (frequent switching between threads).

# # This makes threads appear to run in parallel (multitasking).

# # Multiple threads help in performing background tasks without blocking the main program.

# # A single-threaded process executes only one task at a time.

# # A multithreaded process can run multiple tasks in parallel by having separate stacks/registers for 
# # each thread, but sharing the same code and data.

# #checking with multithreading how long it take
# import time
# import threading

# def calc_square(numbers):
#     print("calculate square numbers")
#     for n in numbers:
#         time.sleep(0.2)
#         print("square :", n*n)

# def calc_cube(numbers):
#     print("calcuate cube of numbers")
#     for n in numbers:
#         time.sleep(0.2)
#         print("cube :",n*n*n)

# arr = [2,3,8,9]

# t = time.time()

# t1 = threading.Thread(target = calc_square,args = (arr,))
# t2 = threading.Thread(target = calc_cube,args = (arr,))  

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("done in :" , time.time()-t,"secs" )
# print("hah....i am done with my all work")



# # ThreadPoolExecutor (Simpler Thread Management)
# # The concurrent.futures.ThreadPoolExecutor makes it easier to manage multiple threads without 
# # manually creating them.

# import time
# from concurrent.futures import ThreadPoolExecutor

# def calc_square(numbers):
#     print("calculate square numbers")
#     for n in numbers:
#         time.sleep(0.2)
#         print("square :", n * n)

# def calc_cube(numbers):
#     print("calculate cube of numbers")
#     for n in numbers:
#         time.sleep(0.2)
#         print("cube :", n * n * n)

# arr = [2, 3, 8, 9]

# t = time.time()

# # Using ThreadPoolExecutor instead of manually creating threads
# with ThreadPoolExecutor (max_workers=2) as executor:
#     future1 = executor.submit(calc_square,arr)
#     future2 = executor.submit(calc_cube,arr)
    
#     future1.result()
#     future2.result()


# print("done in :", time.time() - t, "secs")
# print("hah....i am done with my all work")

# #_______________________________________________________________________________________

# # Multiprocessing means running multiple processes at the same time, where each process 
# # has its own Python interpreter and memory.
# # Because of this, multiprocessing can run truly in parallel on multiple CPU cores.

# # 🔥 Why do we need multiprocessing?

# # Python has a GIL (Global Interpreter Lock) that stops threads from running CPU-heavy work in parallel.
# # But processes don’t share the same interpreter → no GIL → true parallel execution.

# # ✔ Simple definition

# # Multiprocessing = running code in parallel using many CPU cores.

# # Each process:

# # Has its own memory

# # Has its own Python interpreter

# # Runs independently

# # ✔ Example (CPU work that benefits from multiprocessing)

# # If you need to do heavy calculations like:

# # image processing

# # video processing

# # machine learning preprocessing

# # mathematical computation

# # encryption / hashing

# # Then multiprocessing is much faster than threading.

# # ✔ Threading vs Multiprocessing (easy comparison)
# # Feature	Threading	Multiprocessing
# # Runs truly parallel?	❌ No (because of GIL)	✅ Yes
# # Shares memory?	Yes	No
# # Best for	I/O tasks (sleep, network, file read)	CPU-heavy tasks
# # Risk	Race conditions	High RAM usage
# # Speed for CPU tasks	Slow	Fast
# # ✔ One-line summary

# # 👉 Use threading for waiting tasks.
# # 👉 Use multiprocessing for heavy computation.

import time
from multiprocessing import Process

def calc_square(numbers):
    print("calculate square numbers")
    for n in numbers:
        time.sleep(0.2)
        print("square :", n * n)

def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print("cube :", n * n * n)

if __name__ == "__main__":
    arr = [2, 3, 8, 9]

    t = time.time()

    p1 = Process(target=calc_square, args=(arr,))
    p2 = Process(target=calc_cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("done in :", time.time() - t, "secs")
    print("hah....i am done with my all work")
