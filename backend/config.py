import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.path.join(BASE_DIR, 'instance', 'occupancy.db')
OCCUPANCY_THRSHOLD = 5 # Number of people in a room to be considered occupied