
def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    print("get_user_input")
    userInput = input()
    userInput = userInput.split(", ")

    for i in range(len(userInput)):
        userInput[i]=float(userInput[i])

    print(userInput)
    return userInput


def calc_average_temperature(inputTemp):
    print("calc_average_temperature")
    sum = 0
    for i in range(len(inputTemp)):
        sum += inputTemp[i]

    avg = sum/len(inputTemp)
    return avg
    

def find_min_max(inputTemp):
    print("find_min_max")
    minMax = [inputTemp[0], inputTemp[0]]
    for i in range(len(inputTemp)):
        if inputTemp[i] <= minMax[0]:
            minMax[0] = inputTemp[i]
        
        if inputTemp[i] >= minMax[1]:
            minMax[1] = inputTemp[i]
    return minMax

    
def sort_temperature(inputTemp):
    print("sort_temperature")
    inputTemp.sort()
    return inputTemp


def calc_median_temperature(inputSorted):
    print("calc_median_temperature")
    length = len(inputSorted)
    if length % 2 == 1:
        median = inputSorted[int((length-1)/2)]
    else:
        median = inputSorted[int((length)/2)] + inputSorted[int((length)/2)-1]
        median /= 2

    return median


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

    display_main_menu()
    inputList = get_user_input()
    print(calc_average_temperature(inputList))
    print(find_min_max(inputList))
    sortedList = sort_temperature(inputList)
    print(sortedList)
    print(calc_median_temperature(sortedList))


if __name__ == "__main__":
    main()

