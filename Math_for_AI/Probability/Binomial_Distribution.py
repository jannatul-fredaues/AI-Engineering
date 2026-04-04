from scipy.stats import binom

try:
    # 1. Get user inputs
    n = int(input("Enter the number of trials (n): "))
    p = float(input("Enter the probability of success (p) [0 to 1]: "))
    k = int(input("Enter the number of successes you want to check (k): "))

    # Simple validation for probability
    if not (0 <= p <= 1):
        print("Error: Probability (p) must be between 0 and 1.")
    elif k > n:
        print(f"Error: Successes (k={k}) cannot be greater than trials (n={n}).")
    else:
        # 2. Calculate results
        pmf_val = binom.pmf(k, n, p)
        cdf_val = binom.cdf(k, n, p)

        # 3. Output results
        print("-" * 30)
        print(f"Results for n={n}, p={p}, k={k}:")
        print(f"Probability of exactly {k} successes: {pmf_val:.6f}")
        print(f"Probability of {k} or fewer successes: {cdf_val:.6f}")

except ValueError:
    print("Invalid input! Please enter numbers only.")