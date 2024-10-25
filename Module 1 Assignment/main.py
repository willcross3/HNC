import time
import pandas as pd
import bucket
import merge
import linear
import binary
import dijkstra
import bellman_ford


df = pd.read_csv("data.csv")
nums = df['No.'].to_numpy()

""" # Merge Sort
start_time = time.process_time()
merge.merge_sort(nums, 0, len(nums) - 1)
end_time = time.process_time()

print("Sorted array is:", df['No.'])
print("Time taken to sort the array:", end_time - start_time, "seconds.") """


""" # Bucket Sort
nums = []
start_time = time.perf_counter()
bucket.insertion(nums)
bucket.bucket(nums)
end_time = time.perf_counter()
time_taken = end_time - start_time
print(f"Time taken to find the desired output is: {time_taken:.8f} seconds.")
 """

""" #Linear Search
start_time = time.perf_counter()
linear.linear(nums, len(nums), 610) #610 is the number to search for
end_time = time.perf_counter()
time_taken = end_time - start_time
print(f"Time taken to find the desired output is: {time_taken:.8f} seconds.") """


""" #Binary Search
start_time = time.perf_counter()
binary.binary(nums, 0, len(nums), 610) #610 is the number to search for
end_time = time.perf_counter()
time_taken = end_time - start_time
print(f"Time taken to find the desired output is: {time_taken:.8f} seconds.") """


#Dijkstra's Algorithm

dijkstra.dijkstra('a')


#Bellman-Ford Algorithm
