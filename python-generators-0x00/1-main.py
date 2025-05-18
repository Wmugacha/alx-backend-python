#!/usr/bin/python3
from itertools import islice
import sys

# Import the module
stream_users_module = __import__('0-stream_users')

# Get the generator function from the module
stream_users = stream_users_module.stream_users

# Use islice to fetch first 6 rows
for user in islice(stream_users(), 6):
    print(user)