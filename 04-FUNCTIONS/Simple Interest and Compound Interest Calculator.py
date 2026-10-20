def calculate_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    compound_interest = principal * (1 + rate / 100) ** time - principal
    return simple_interest, compound_interest


# Example usage
p = float(input("Enter principal amount: "))
r = float(input("Enter annual interest rate (%): "))
t = float(input("Enter time (years): "))

si, ci = calculate_interest(p, r, t)
print(f"Simple Interest: {si:.2f}")
print(f"Compound Interest: {ci:.2f}")
