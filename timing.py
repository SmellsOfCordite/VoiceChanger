import time

def time_function(func, *args):
  start_time = time.time()
  result = func(*args)
  end_time = time.time()
  execution_time = end_time - start_time
  print(execution_time)
  return result, execution_time