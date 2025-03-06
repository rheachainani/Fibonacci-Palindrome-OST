def fibonacci_series(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[i-1] + fib_series[i-2])
    return fib_series[:n]  # Return only 'n' elements

def is_palindrome(number):
    return str(number) == str(number)[::-1]

# Welcome message
print("🔹🔹 Welcome to the Fibonacci and Palindrome Checker 🔹🔹\n")

while True:
    print("\n Choose an option:")
    print("1️⃣ Generate Fibonacci Series")
    print("2️⃣ Check if a number is a Palindrome")
    print("3️⃣ Exit")

    choice = input("\n Enter your choice (1/2/3): ")

    if choice == '1':
        num_terms = int(input("\nEnter the number of terms for Fibonacci series: "))
        fib_series = fibonacci_series(num_terms)
        print(f"📌 Fibonacci Series ({num_terms} terms):", fib_series)

    elif choice == '2':
        num_to_check = input("\nEnter a number to check if it is a palindrome: ")
        if num_to_check.isdigit():  # Ensure input is a number
            if is_palindrome(num_to_check):
                print(f"✅ {num_to_check} is a palindrome!")
            else:
                print(f"❌ {num_to_check} is NOT a palindrome.")
        else:
            print("⚠️ Please enter a valid number.")

    elif choice == '3':
        print("\n🔹 Thank you for using the program! Goodbye! 👋")
        break

    else:
        print("⚠️ Invalid choice! Please enter 1, 2, or 3.")

