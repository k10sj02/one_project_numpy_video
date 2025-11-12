import numpy as np

def file_handling():
  with open('company.txt', 'r') as file:
    for line in file:
      values = line.strip().split(',')
      