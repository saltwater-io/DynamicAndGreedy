
#      This program implements a regular and dynamic solution to the rod cutting problem;
#      as well as an implementation of a greedy algorithm to solve a scheduling problem.
#
#           Written by: Dakota McGuire - 4/2/19
#               For Algorithms - USM

# rod_prices = {1: 1, 2: 5, 3: 8, 4: 9, 5: 10, 6: 17, 7: 17, 8: 20, 9: 24, 10: 30}

# Price of each length of section of rod
rod_price = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

# Start times for activities - index matches end times
# 0 is used as placeholder
start_times = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
# End times for activities - index matches start times
finish_times = [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]


# Returns max value from two numbers
def get_max(a, b):
    if a > b:
        return a
    else:
        return b


# Cuts rod recursively w/ repetition - not dynamic
def cut_rod(price, n):
    # If n = 0 or less return 0
    if not n > 0:
        return 0
    max_value = 0
    # Cuts rod into different pieces to find the best choice for maximum profit
    for i in range(0, n):
        max_value = get_max(max_value, price[i] + cut_rod(price, n - i - 1))
    return max_value


# Cuts rod dynamically by building an array of values bottom-up
# Returns the maximum value sotred at index n in stored_prices
def cut_bottom_up(price, n):
    # Stored prices hold the max possible value of a rod of a certain length
    stored_prices = []
    # From to 0 the the len(n) store '0' to hold the index
    for i in range(0, n + 1):
        stored_prices.append(0)
    max_value = 0
    # Inserts maximum value of rod cuts into stored prices -
    # using this method it checks previously stored values and compares
    for j in range(0, n + 1):
        for k in range(j):
            max_value = get_max(max_value, price[k] + stored_prices[j - k - 1])
        stored_prices[j] = max_value
    return stored_prices[n]


# Helper function to run rod cutting algorithm
def rod_cutting():
    print("")
    # For lengths 1-10: Print max value
    for i in range(1, 11):
        print("Maximum value at length " + str(i) + ": ", cut_rod(rod_price, i))
    test_value = 8
    print("")
    # Max value at length of test-value: 8
    print("Maximum bottom-up at length " + str(test_value) + ": ", cut_bottom_up(rod_price, test_value))


# Greedy Algorithm implemented to solve scheduling tasks
# start = start times, finish = finish times
def get_greedy(start, finish):
    # Length of acitivities - Start times must be same length as finish times
    n = len(start)
    # a = Activities chosen
    a = []
    # k = index
    k = 1
    for m in range(2, n):
        # If start times after finish times add to activities selected
        if start[m] >= finish[k]:
            a.append(m)
            k = m
    return a


# Runs program
def main():
    rod_cutting()
    # gets activities selected using a greedy algorithm
    activities = get_greedy(start_times, finish_times)
    output = "The greedy scheduling algorithm chooses activities: "
    print("")
    # Format's output
    for activity in activities:
        output = output + str(activity) + " "
    print(output)


if __name__ == "__main__":
    main()
