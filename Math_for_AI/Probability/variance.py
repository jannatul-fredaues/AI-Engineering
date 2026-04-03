import statistics

data = list(map(int, input("Enter numbers: ").split()))

print("Variance:", statistics.variance(data))