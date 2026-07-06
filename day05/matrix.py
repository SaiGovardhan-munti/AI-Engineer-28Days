import numpy as np

arr = np.random.randint(0,100, size=(5,5))
print(arr)
print(arr.shape)

print(f"Mean : {np.mean(arr)}")
print(f"Max : {np.max(arr)}")
print(f"Min : {np.min(arr)}")

print(f"first row: {arr[0, :]}")
print(f"last column: {arr[:, -1]}")

#brodcast
print(arr + 10)

result = np.where(arr > 50, "high", "low" )
print(result)
