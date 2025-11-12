import numpy as np
from operationclass import IntArray

def productivity_of_company(order, data_frame):
  """
  num_products = 0
  for element in data_frame[order]:
    num_products += element
  
  return num_products
  """
  return np.sum()

def max_productivity(data_frame):
  i = 0 
  best_company = 1 + 1
  num_products = 0

  for i in range(len(data_frame)):
    result = productivity_of_company(i, data_frame)
    if result > num_of_products:
      num_of_products = result
      best_company = i + 1

  print(f"The best company is the {best_company}")

def file_handling():
  with open('company.txt', 'r') as file:
    lines = []

    for line in file:
      values = line.strip().split(',')
      int_values = [int(val) for val in values]
      lines.append(int_values)
    
    data_frame = np.array([np.array(row) for row in lines], dtype='object')
    
    for row in data_frame:
      for i in row:
        print(type(i))
    
    return data_frame
  

def main():
  data_frame = file_handling()
  print(data_frame)

  first_branch = IntArray(data_frame[0])
  first_branch.display()
  first_branch.salary()
  first_branch.show_data()


main()