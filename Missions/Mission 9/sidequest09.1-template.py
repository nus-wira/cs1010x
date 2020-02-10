#
# CS1010X --- Programming Methodology
#
# Sidequest 9.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

import json
import time

#####################
# Reading json file #
#####################

def read_json(filename):
    """
    Reads a json file and returns a list of modules
    To find out more about json, please google it :P

    For example, file.txt contains:
    [["CS3216", "SOFTWARE DEVELOPMENT ON EVOLVING PLATFORMS", "TAN KENG YAN, COLIN"], ["CS2010", "DATA STRUCTURES & ALGORITHMS II", "STEVEN HALIM"], ["CS1010S", "PROGRAMMING METHODOLOGY", "LEONG WING LUP, BEN"]]

    Calling read_json('file.txt') will return the following array
    [
        ["CS3216", "SOFTWARE DEVELOPMENT ON EVOLVING PLATFORMS", "TAN KENG YAN, COLIN"],
        ["CS2010", "DATA STRUCTURES & ALGORITHMS II", "STEVEN HALIM"],
        ["CS1010S", "PROGRAMMING METHODOLOGY", "LEONG WING LUP, BEN"]
    ]
    """
    datafile = open(filename, 'r', encoding='utf-8')
    return json.loads(datafile.read())

#############
# Accessors #
#############

def module_code(module):
    return module[0]

def module_name(module):
    return module[1]

def module_prof(module):
    return module[2]


###########
# Task 1a #
###########

def merge_lists(all_lst):
    length = len(all_lst)
    if length == 0:
        return all_lst
    elif length == 1:
        return all_lst[0]

    new_lst = []
    while all_lst[0] and all_lst[1]:
        if all_lst[0][0] <= all_lst[1][0]:
            new_lst += [all_lst[0][0]]
            all_lst[0].pop(0)    
        else:
            new_lst += [all_lst[1][0]]
            all_lst[1].pop(0)
            
    new_lst.extend(all_lst[0])
    new_lst.extend(all_lst[1])
    
    return merge_lists([new_lst] + all_lst[2:])

all_lst = [[2, 7, 10], [0, 4, 6], [3, 11]]
print("## Q1a ##")
print(merge_lists(all_lst)) # [0, 2, 3, 4, 6, 7, 10, 11]


###########
# Task 1b #
###########

def merge(lists, field):
    length = len(lists)
    if length == 0:
        return lists
    elif length == 1:
        return lists[0]

    new_lst = []
    while lists[0] and lists[1]:
        if field(lists[0][0]) <= field(lists[1][0]):
            new_lst += [lists[0][0]]
            lists[0].pop(0)    
        else:
            new_lst += [lists[1][0]]
            lists[1].pop(0)
    new_lst.extend(lists[0])
    new_lst.extend(lists[1])
    
    return merge([new_lst] + lists[2:], field)


list_of_lists = [[["CS1010S", "PROGRAMMING METHODOLOGY", "LEONG WING LUP, BEN"],
                  ["CS3235", "COMPUTER SECURITY", "NORMAN HUGH ANDERSON"]],
                 [["CS4221", "DATABASE DESIGN", "LING TOK WANG"],
                  ["CS2010", "DATA STRUCTURES & ALGORITHMS II", "STEVEN HALIM"]]]
print("## Q1b ##")
print(merge(list_of_lists, module_prof))
# [[’CS1010S’, ’PROGRAMMING METHODOLOGY’, ’LEONG WING LUP, BEN’],
#  [’CS4221’, ’DATABASE DESIGN’, ’LING TOK WANG’],
#  [’CS3235’, ’COMPUTER SECURITY’, ’NORMAN HUGH ANDERSON’],
#  [’CS2010’, ’DATA STRUCTURES & ALGORITHMS II’, ’STEVEN HALIM’]

##########
# Task 2 #
##########

def merge_sort(lst, k, field):
    length = len(lst)
    if length < 2:
        return lst
    elif length <= k or k < 2:
        split_lst = list(map(lambda x: [x], lst))
        
        return merge(split_lst, field)

    #takes length and k, returns tuple of split lengths to add up to k parts
    def split_len(length, k): #length > k
        if k < 2:
            return (length,)
    
        part = length // k   
        return (part,) + split_len(length - part, k-1)

    parts = split_len(length, k)
    split_part_lst = [lst[:parts[0]]]
    for i in range(1,k):
        index = sum(parts[:i])
        split_part_lst += [lst[index:index+parts[i]]]

    
    split_lst = []
    for split_part in split_part_lst:
        split_lst += [merge_sort(split_part, k , field)]
    

    return merge(split_lst, field)

lst = [['CS1010S', 'PROGRAMMING METHODOLOGY', 'LEONG WING LUP, BEN'], ['CS4221', 'DATABASE DESIGN', 'LING TOK WANG'], ['CS3235', 'COMPUTER SECURITY', 'NORMAN HUGH ANDERSON'], ['CS2010', 'DATA STRUCTURES & ALGORITHMS II', 'STEVEN HALIM']]
# For your own debugging
modules = read_json('modules_small.txt')
for module in merge_sort(modules, 5, module_code):
   print(module)


########### DO NOT REMOVE THE TEST BELOW ###########
########### DO NOT REMOVE THE TEST BELOW ###########
########### DO NOT REMOVE THE TEST BELOW ###########
########### DO NOT REMOVE THE TEST BELOW ###########
########### DO NOT REMOVE THE TEST BELOW ###########

def print_list_to_str(list):
    return '\n'.join(str(x) for x in list)

def test(testfile_prefix):
    print("\n*** Testing with ",testfile_prefix,".txt ***")
    modules = read_json(testfile_prefix+'.txt')
    total_time = 0

    # Open correct answers
    modules_sorted_code = open(testfile_prefix+'_sorted_code.txt', 'r', encoding='utf-8').read()
    modules_sorted_name = open(testfile_prefix+'_sorted_name.txt', 'r', encoding='utf-8').read()
    modules_sorted_prof = open(testfile_prefix+'_sorted_prof.txt', 'r', encoding='utf-8').read()

    ks = [2,3,5,8,13,21,34,55,89,144]
    pass_k = 0

    for k in ks:
        start_time = time.time()
        # Execute
        modules_answer_code = merge_sort(modules, k, module_code)
        modules_answer_name = merge_sort(modules, k, module_name)
        modules_answer_prof = merge_sort(modules, k, module_prof)
        end_time = time.time()
        total_time += (end_time - start_time)

        # Check
        code_same = print_list_to_str(modules_answer_code) == modules_sorted_code
        name_same = print_list_to_str(modules_answer_name) == modules_sorted_name
        prof_same = print_list_to_str(modules_answer_prof) == modules_sorted_prof
        if (code_same and name_same and prof_same):
            pass_k += 1
        print("k = ", k, ", code: ",code_same,", name: ", name_same,", prof: ",prof_same)

    print(pass_k,"/", len(ks), " correct! Total time taken: ", total_time, " seconds.")

print("## Q2 ##")
test('modules_small')
test('modules')
test('modules_empty')
