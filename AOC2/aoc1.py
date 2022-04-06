from itertools import combinations
import operator

def create_dictionary(line):
    pwd_dict = {}
    pwd_list = line.split()
    #print('Entry is: ' + str(pwd_list))
    min_max = pwd_list[0].split("-")
    pwd_dict["min"] = int(min_max[0])
    pwd_dict["max"] = int(min_max[1])
    pwd_dict["char"] = pwd_list[1][0]
    pwd_dict["password"] = pwd_list[2]
    print('Dictionary Entry: ' + str(pwd_dict))
    return pwd_dict

def meets_password_policy(password_and_policy):
    char_count_in_password = password_and_policy["password"].count(password_and_policy["char"])
    return password_and_policy["min"] <= char_count_in_password <= password_and_policy["max"]


# Open the file and read in the values as strings
f = open("input.txt", "r")
pwd_input = []

for x in f:
    pwd_input.append(x)
    #create_dictionary(pwd_input[x])

for y in pwd_input:
    #print(y)
    line = ''
    line = str(y)
    passwords_and_policies = [create_dictionary(line) for line in f]
    
#valid_passwords = list(filter(meets_password_policy, password_and_policy))
    

# Close the file
f.close()