def MaxHeapChecker(arr):
    
  # code goes here
  res = [] # array of wrong elements
  n = len(arr)

  for i in range(n//2):
    if arr[i*2+1] > arr[i]:
      res.append(str(arr[i*2+1]))

    if 2*i+2 < n and arr[i*2+2] > arr[i]:
      res.append(str(arr[i*2+2]))
  
  return ",".join(res) if len(res) else 'max'

# keep this function call here 
print(MaxHeapChecker(input()))
