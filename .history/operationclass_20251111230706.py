import numpy as np

class IntArray:
  def __init(self, int_array):
    if not isinstance(int_array, np.ndarray) or int_array.dtype != int: 
      raise ValueError("Input must be a NUMPY array of integers")
    
    self.int_array = int_array
  
  def display(self):
    print(self.int_array)
  
  def salary(self):
    array_shape = self.int_array.shape
    money_for_product = np.full(array_shape,7)
    salaries = self.int_array * money_for_product


    print(f"People made {self.int_array} and these are their salaries: {salaries}")