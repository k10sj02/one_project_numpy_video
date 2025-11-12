import numpy as np

class IntArray:
  def __init(self, int_array):
    if not isinstance(int_array, np.ndarray) or int_array.dtype != int: 
      raise ValueError("Input must be a NUMPY array of integers")
    
    self.int_array = int_array
  
  def display(self):
    print(self.int_array)