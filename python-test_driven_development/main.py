#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

# Tests
say_my_name("John", "Smith")   # My name is John Smith
say_my_name("Walter", "White") # My name is Walter White
say_my_name("Bob")             # My name is Bob