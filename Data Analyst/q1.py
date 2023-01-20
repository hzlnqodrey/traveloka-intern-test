# MEDIAN OF LENGTH STRING AND GIVING ITS INDEX
# example:
# input 1:
# str_list = ['a', 'aa'] , then 
# output 1:
# (string= 'aa', index=2)

# input 2:
# str_list = ['a', 'aa', 'aaaa', 'aaaaaaaa']
# output 2:
# (string= 'aaaa', index=3)

# input 3:
# str_list = ['a', 'aaa', 'aa']
# output 3:
# (string= 'aa', index=2)

# if median is not exact like len string, chose the closest number [https://stackoverflow.com/questions/12141150/from-list-of-integers-get-number-closest-to-a-given-value



# ======================================================================================================================


def find_closest_number(arr, target): # target is median of string len

    # buntu haha
    n = len(arr)
    
    # check if the target greater than all
    if ( target >= arr[-1] ):
        # then it's the closest number
        return arr[-1]

    # check if the target smallest than all
    if ( target <= arr[0] ):
        return arr[0]

    # check if the target between them [Traverse the middle list]  # BINARY SEARCH
    low = 0
    high = n;
    mid = 0

    while ( low < high ):

        mid = int(( high + low ) / 2)

        if ( arr[mid] == target ):
            return target

        if ( target < arr[mid] ):
            # FIND CLOSEST
            if ( mid > 0 and target > arr[mid-1] ):
                return get_closest_number(arr[mid-1], arr[mid], target)
        
            high = mid

        elif ( target > arr[mid] ):
            # FIND CLOSEST
            if ( mid < n - 1  and target < arr[mid+1] ):
                return get_closest_number(arr[mid], arr[mid+1], target)

            low = mid + 1
        
        
    return arr[mid]

# Method to compare which one is the more close.
# We find the closest by taking the difference
# between the target and both values. It assumes
# that val2 is greater than val1 and target lies
# between these two.
def get_closest_number(v1, v2, target):

    if ( target - v1 >= v2 - target ):
        return v2
    else:
        return v1

def med_string(list_string):

    string = ""
    index = 0

    # med_odd = ((n+1)/2)
    # med_even = ((n/2)+((n/2)+1))/2

    # Testing
    kumpul_len_string = []
    kumpul_len_string_even = []
    kumpul_string_index = []
    kumpul_string_index_even = []

    if (len(list_string) >= 0):
        for i in list_string:
            # even
            if (len(list_string) % 2 == 0):
                kumpul_len_string_even.append(len(i))
                kumpul_string_index_even.append(list_string.index(i))

            kumpul_len_string.append(len(i))
            kumpul_string_index.append(list_string.index(i))

    if (len(list_string) % 2 == 0):
        print("string len    :", kumpul_len_string_even)
        print("string index  :",kumpul_string_index_even)
    else:
        print("string len    :", kumpul_len_string)
        print("string index  :", kumpul_string_index)

    # FIND THE MAXIMUM NUMBER to be compared with median
    max_number = 0
    max_number_arr = sorted(kumpul_len_string)
    print(max_number_arr)
    max_number = max_number_arr[-1]
    print("max number: ",max_number)

    # Check whether list is not 0 size
    if (len(list_string) >= 0):
        med_odd = ((max_number+1)/2)
        med_even = ((max_number/2)+((max_number/2)+1))/2
        for i in list_string:
            # even
            if (len(list_string) % 2 == 0):
                if ( med_even == len(i) ):
                    string = i
                    index = list_string.index(i)
                else:
                    index = find_closest_number(max_number_arr, med_even)

            if ( med_odd == len(i) ):
                string = i
                index = list_string.index(i)
            else:
                index = find_closest_number(max_number_arr, med_odd)

    return string, index





string, index = med_string(['a'])
print("\n")
print("My Output")
print(string)
print(index)
print("====================== TEST CASE #1")
print("\n")
string, index = med_string(['a', 'aa'])
print("\n")
print("My Output")
print(string)
print(index)
print("====================== TEST CASE #2")
print("\n")
string, index = med_string(['a', 'aaa', 'aa'])
print("\n")
print("My Output")
print(string)
print(index)
print("====================== TEST CASE #3")
print("\n")
string, index = med_string(['aaaaaaaaaaaaaaa', 'a', 'aaa', 'aaaaa', 'aaaaaaaa']) # CASE WHEN THE EXACT CANT BE FOUND, FIND THE CLOSEST NUMBER
print("\n")
print("My Output")
print(string)
print(index)
print("====================== TEST CASE #4")
print("\n")
string, index = med_string(['aaaaaaaaaaaaaaa', 'aaaaaaaa', 'a', 'aaa',  'aaaaa', 'aaaaaaa']) # CASE WHEN THE EXACT CANT BE FOUND, FIND THE CLOSEST NUMBER
print("\n")
print("My Output")
print(string)
print(index)
print("====================== TEST CASE #5")
print("\n")
string, index = med_string(['aaaaaaaaaaaaaaa', 'a', 'aaa', 'aaaaaa', 'aaaaa', 'aaaaaaa']) # CASE WHEN THE EXACT CANT BE FOUND, FIND THE CLOSEST NUMBER
print("\n")
print("My Output")
print(string)
print(index)
print("====================== TEST CASE #6")
print("\n")

