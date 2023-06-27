import concurrent.futures

def sum_array(numbers):
  return sum(numbers)

my_array = [1, 2, 3, 4, 5, 6]

with concurrent.futures.ThreadPoolExecutor() as executor:
  future = executor.submit(sum_array, my_array) #-> does the sum_array function with the array as parameter
  result = future.result() #-> we gave the result of the future variable to result variable..
  print("Sum:", result) #-> finally prints it. 
