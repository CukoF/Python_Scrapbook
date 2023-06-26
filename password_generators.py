# -*- coding: utf-8 -*-
import random

lower = "qwertzuiopasdfghjklyxcvbnm"
upper = "QWERTZUIOPASDFGHJKLYXCVBNM"
numbers = "1234567890"
symbols = "[]{}()*;/,_-."

all_items = lower + upper + numbers + symbols


pass_length_choice = random.choice(list(range(8, 17)))
print(pass_length_choice)
print(type(pass_length_choice))


password = "".join(random.sample(all_items, pass_length_choice))
print(password)