import statistics

data = list(map(int, input("Enter numbers: ").split()))

print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Mode:", statistics.multimode(data))