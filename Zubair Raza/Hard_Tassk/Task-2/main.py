import numpy as np

def convert_to_2d_array(arr, rows, cols):
    
 # Converts a 1D array into a 2D array with the specified number of rows and columns using NumPy.
    
    # Check if the input array can be evenly divided into the specified number of rows and columns
    if len(arr) != rows * cols:
        return None
    
    # Reshape the input array into a 2D array with the specified number of rows and columns
    arr_2d = np.reshape(arr, (rows, cols))
    
    # Return the new 2D array
    return arr_2d
convert_to_2d_array([1, 2, 3, 4, 5, 6], 2, 3)
convert_to_2d_array([1, 2, 3, 4, 5, 6], 3, 2)
convert_to_2d_array([1, 2, 3, 4, 5, 6], 3, 3)
convert_to_2d_array([], 2, 2)


