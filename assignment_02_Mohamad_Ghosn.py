def Menu():
    print("Welcome to my small program :)")
    print("In this program, I will give you 4 options for you and I to play together:")

    print("Select one:")
    print("1. Count Digits")
    print("2. Find Max")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        num = int(input("Enter an integer: "))
        result = count_digits(num)
        print("Number of digits:", result)
    elif choice == "2":
        numbers = input("Enter a list of integers (space-separated): ")
        num_list = [int(n) for n in numbers.split()]
        result = find_max(num_list)
        print("Maximum value:", result)
    elif choice == "3":
        print("Exiting the program. Goodbye!")
        return
    else:
        print("Invalid choice. Please try again.")
        Menu()


def count_digits(num):
    count = 0
    if num < 0:
        num = abs(num)
    if num == 0:
        return 1
    count = 1 + count_digits(num // 10)
    return count


def find_max(lst):
    if not lst:
        return 0
    elif len(lst) == 1:
        return lst[0]
    else:
        max_value = find_max(lst[1:])

        if lst[0] > max_value:
            return lst[0]
        else:
            return max_value


Menu()