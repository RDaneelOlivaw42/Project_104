import csv
from collections import Counter

with open('/Users/drpoojayadav/Downloads/Project 104/data.csv', newline = "") as f:
    file = csv.reader(f)
    all_data = list(file)
    
all_data.pop(0)

data = []

for singular_data in all_data:
    data.append(singular_data[2])


def arithmetic_mean(data):
    # getting sum
    total_sum = 0

    for singular_data in data:
        total_sum += float(singular_data)
    
    # getting number to divide sum by
    denominator = len(data)

    # applying mean formula
    mean = total_sum/denominator
    print("Arithemtic mean weight is", str(mean), "pounds")


def median(data):
    # getting total number of data 
    n = len(data)

    # checking which formula to apply
    if n%2 == 0:

        m1 = float(data[n//2])
        m2 = float(data[n//2 - 1])
        median = (m1 + m2)/2
    
    else:
        median = float(data[n//2])

    print("Median weight is", str(median), "pounds")


def mode(data):
    mode_data = Counter(data)

    # finding maximum weight and minimum weight from data
    max_weight = 0
    min_weight = 1000

    for weight in data:
        if float(weight) > max_weight:
            max_weight = float(weight)
        if float(weight) < min_weight:
            min_weight = float(weight)

    # finding upper_limit and lower_limit of data
    max_weight_list = list(str(int(max_weight)))
    max_weight_to_be_subtracted = max_weight_list[len(max_weight_list)-1]
    upper_limit = (int(max_weight) - int(max_weight_to_be_subtracted)) + 10
    
    min_weight_list = list(str(int(min_weight)))
    min_weight_to_be_subtracted = min_weight_list[len(min_weight_list)-1]
    lower_limit = int(min_weight) - int(min_weight_to_be_subtracted)

    # defining ranges/classes of data [Eg. 10-20, 20-30]
    num_of_ranges = (upper_limit - lower_limit)
    x = 0
    ranges = {}

    while(x < num_of_ranges):
        first_term = upper_limit - x - 10
        second_term = upper_limit - x
        expression = f"{first_term} - {second_term}"
        ranges.update({expression: 0})
        x += 10
        continue

    # defining frequency of each range in ranges(dictionary object)
    for range in ranges:
        num = str(range)
        num_components = num.split(" ")
        
        for weight,occurence in mode_data.items():
            if num_components[0] < weight < num_components[2]:
                ranges[range] += occurence

    
    #finding modal range and occurence
    mode_range, mode_occurence = 0, 0

    for range in ranges:
        if occurence > mode_occurence:
            mode_occurence = occurence
            num = str(range).split(" ")
            mode_range = [int(num[0]), int(num[2])]
    
    mode = float((mode_range[0] + mode_range[1])/2)
    print("Mode is", str(mode), "pounds")
        

arithmetic_mean(data)
median(data)
mode(data)