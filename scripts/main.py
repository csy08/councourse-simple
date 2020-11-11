import os, sys

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(sys.path)

print(os.environ)

from helpers.simple import hello_world

hello_world()
