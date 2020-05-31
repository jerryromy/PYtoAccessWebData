import re
hand = open('regex_sum_358097.txt')
numlist = list()
for line in hand :
    line = line.rstrip()
    nums = re.findall('[0-9]+', line)
    # this findall() will return an array, or a list of lists, so I must identify the lists with just one element first and append the to the numlist
    if len(nums) ==1 :
        for item in nums :
            intnums = int(item)
            numlist.append(intnums)
    # Now I'm attempting to ignore the lists with a single element so I can proceed to iterate through the lists with multiple elements, convert them to int(), and append them to numlist
    if len(nums) >1 :
        for group in nums :
            for num in group :
            # iterating through the arrays in findall() and converting the strings within the arrays into integers and appending to numlist
                addnum = int(num)
                numlist.append(addnum)
print(sum(numlist))
# printing sum of all integers in list
