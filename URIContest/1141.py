history = """
6
plant
ant
cant
decant
deca
an
2
supercalifragilisticexpialidocious
rag
0
"""

def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def pic_array(*args):
    return args[0].split("\n")

def divide_groups(array):
    groups = []
    temp = []
    for line in array:
        if isInt(line):
            groups.append(temp[1:])
            if line == "0":
                break;
            del temp[:]

        temp.append(line)
    return groups[1:]

def sort_array(array):
    for vector in array:
        vector.sort(key = lambda s: len(s))
    return array

def go_groups(lists):
    for arr in lists:
        print(run_compare(arr))

def run_compare(array):
    count = 0
    for i, val in enumerate(array):
        temp = count_substrings(val, array[i:])
        if temp > count:
            count = temp
    return count

def count_substrings(comp, array):
    count = 0
    for value in array:
        if value.find(comp) >= 0:
            count += 1
            comp = value
    return count
        

pics = pic_array(history)
groups = divide_groups(pics)
groups = sort_array(groups)
go_groups(groups)
