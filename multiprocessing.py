import multiprocessing

def sum_array(arr):
    return sum(arr)

if __name__ == "__main__":
    # Sample array
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    num_processes = multiprocessing.cpu_count() # Number of processes to use

    chunk_size = len(array) // num_processes # divides the length of the array by the number of processes 
    #-> Basically, chunk size represents the approximate number of elements
    chunks = [array[i:i + chunk_size] for i in range(0, len(array), chunk_size)] 
    #-> divides the array into smaller chunks, generates a sequence of indices, starting from 0 
    # and incrementing by chunk_size at each step. Also, creates a new sublist for each iteration


    pool = multiprocessing.Pool(processes=num_processes) #-> pool of worker processes
    results = pool.map(sum_array, chunks) #-> sum_array function to each chunk in parallel
    total_sum = sum(results) #-> Combine the results from all the worker processes

    print("Sum:", total_sum)
