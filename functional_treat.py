data = []
data_type = ""
summary_count = 0


def get_numbers():
    """Convert space-separated values into a list of integers."""
    return [int(x) for x in input("Enter values separated by spaces: ").split()]


def input_data():
    """Take 1D or 2D list input from the user."""
    global data, data_type

    print("\nChoose data type:")
    print("1. 1D List")
    print("2. 2D List")

    choice = input("Enter your choice: ")
    print("You selected:", choice)

    if choice == "1":
        data = get_numbers()
        data_type = "1D"

    elif choice == "2":
        rows = int(input("Enter number of rows: "))
        data = []

        for i in range(rows):
            print(f"Enter values for row {i + 1}:")
            data.append(get_numbers())

        data_type = "2D"

    else:
        print("Invalid choice!")
        return

    print("Data stored successfully!")


def flatten(values):
    """Return a 1D list from either a 1D or 2D list."""
    if not values:
        return []

    if isinstance(values[0], list):
        return [item for row in values for item in row]

    return values.copy()


def display_data():
    """Display the current dataset in a readable format."""
    if not data:
        print("No data available. Please input data first.")
        return

    print("\nCurrent Dataset:")

    if data_type == "1D":
        print(data)

    else:
        for row in data:
            print("  ", row)


def data_summary():
    """Use built-in functions to display basic dataset statistics."""
    global summary_count

    values = flatten(data)

    if not values:
        print("No data available.")
        return

    summary_count += 1

    print("\nData Summary (Built-in Functions)")
    print("Total elements :", len(values))
    print("Minimum value  :", min(values))
    print("Maximum value  :", max(values))
    print("Sum of values  :", sum(values))
    print("Average value  :", round(sum(values) / len(values), 2))


def analyze_args(*numbers):
    """Analyze any number of values using *args."""
    return len(numbers), sum(numbers), max(numbers), min(numbers)


def show_kwargs(**details):
    """Display dataset information supplied through **kwargs."""
    print("\nDataset Information (**kwargs)")

    for key, value in details.items():
        print(f"{key.title():<15}: {value}")


def function_demo():
    """Demonstrate UDF, *args, **kwargs and __doc__."""
    values = flatten(data)

    if not values:
        print("No data available. Please input data first.")
        return

    count, total, highest, lowest = analyze_args(*values)

    print("\nUser-Defined Function Demo")
    print("Count  :", count)
    print("Sum    :", total)
    print("Highest:", highest)
    print("Lowest :", lowest)

    show_kwargs(
        data_type=data_type,
        elements=count,
        average=round(total / count, 2)
    )

    print("\nFunction Documentation (__doc__):")
    print(analyze_args.__doc__)


def factorial(n):
    """Calculate factorial using recursion."""
    if n <= 1:
        return 1

    return n * factorial(n - 1)


def recursion_demo():
    """Demonstrate recursive factorial calculation."""
    n = int(input("\nEnter a number for factorial: "))

    print("You entered:", n)

    if n < 0:
        print("Factorial is not defined for negative numbers.")

    else:
        print(f"Factorial of {n} is {factorial(n)}")


def lambda_demo():
    """Filter values using lambda with map() and filter()."""
    values = flatten(data)

    if not values:
        print("No data available. Please input data first.")
        return

    threshold = int(input("\nEnter threshold: "))

    print("You entered:", threshold)

    filtered = list(filter(lambda x: x >= threshold, values))

    doubled = list(map(lambda x: x * 2, filtered))

    print(f"Values >= {threshold} :", filtered)
    print("Doubled values       :", doubled)


def global_demo():
    """Show a global variable used across function calls."""
    print("\nGlobal Variable Demo")
    print("Summary function was used",
          summary_count,
          "time(s).")


def get_statistics(values):
    """Return minimum, maximum, sum and average as multiple values."""
    return (
        min(values),
        max(values),
        sum(values),
        round(sum(values) / len(values), 2)
    )


def multiple_return_demo():
    """Demonstrate a function returning multiple values."""
    values = flatten(data)

    if not values:
        print("No data available. Please input data first.")
        return

    minimum, maximum, total, average = get_statistics(values)

    print("\nDataset Statistics (Multiple Return Values)")
    print("Minimum :", minimum)
    print("Maximum :", maximum)
    print("Sum     :", total)
    print("Average :", average)


def sorting_demo():
    """Demonstrate sort() and sorted() for 1D and 2D lists."""
    global data

    if not data:
        print("No data available. Please input data first.")
        return

    print("\nSorting Options")
    print("1. Ascending")
    print("2. Descending")

    choice = input("Enter your choice: ")

    # Keep the entered choice visible
    print("You selected:", choice)

    reverse = choice == "2"

    if data_type == "1D":

        original = data.copy()

        # sort() changes the original list
        data.sort(reverse=reverse)

        # sorted() returns a new list
        new_sorted = sorted(original, reverse=reverse)

        print("\nOriginal copy :", original)
        print("After sort()  :", data)
        print("sorted() copy :", new_sorted)

    else:

        print("\nOriginal 2D List:")

        for row in data:
            print(" ", row)

        # sort() changes every row in-place
        for row in data:
            row.sort(reverse=reverse)

        # sorted() creates a new 2D list
        sorted_2d = [
            sorted(row, reverse=reverse)
            for row in data
        ]

        print("\nAfter sort() on each row:")

        for row in data:
            print(" ", row)

        print("\nNew list using sorted():")

        for row in sorted_2d:
            print(" ", row)


def main():
    """Main menu for the Data Analyzer and Transformer."""

    print("==============================================")
    print(" Welcome to the Data Analyzer and Transformer")
    print("==============================================")

    while True:

        print("\nMain Menu")
        print("1. Input Data (1D / 2D)")
        print("2. Display Data")
        print("3. Data Summary (Built-in Functions)")
        print("4. UDF + *args + **kwargs + __doc__")
        print("5. Factorial (Recursion)")
        print("6. Filter Data (Lambda + map + filter)")
        print("7. Global Variable Demo")
        print("8. Statistics (Return Multiple Values)")
        print("9. Sort Data (sort / sorted)")
        print("10. Exit")

        choice = input("Please enter your choice: ")

        # Keep the entered menu choice visible
        print("You selected:", choice)

        if choice == "1":
            input_data()

        elif choice == "2":
            display_data()

        elif choice == "3":
            data_summary()

        elif choice == "4":
            function_demo()

        elif choice == "5":
            recursion_demo()

        elif choice == "6":
            lambda_demo()

        elif choice == "7":
            global_demo()

        elif choice == "8":
            multiple_return_demo()

        elif choice == "9":
            sorting_demo()

        elif choice == "10":
            print("\nThank you for using the Data Analyzer and Transformer!")
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()