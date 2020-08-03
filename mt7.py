from threading import *
print(current_thread().getName())
current_thread().setName("Zeeshan")
print(current_thread().getName())
print(current_thread().name)