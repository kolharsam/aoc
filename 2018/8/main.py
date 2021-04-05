inp = [int(i) for i in open('input', 'r').readline().split()]

all_metadata = []
all_child = []

def tree_parse(arr, level, par_id):
    root_child = arr[0]
    rc = arr[0]
    root_metadata_num = arr[1]

    if root_child != 0:
        loop_list = arr[2:]
        ll = level + 1
        i = 1
        while root_child != 0:
            pid = (par_id, i)
            loop_list = tree_parse(loop_list, ll, pid)
            root_child -= 1
            i += 1
        arr = loop_list
    else:
        arr = arr[2:]
    
    level_metadata = []
    for i in range(root_metadata_num):
        all_metadata.append(arr[i])
        level_metadata.append(arr[i])

    all_child.append((level, rc, par_id, level_metadata, sum(level_metadata)))

    return arr[root_metadata_num:]

tree_parse(inp, 0, None)

# part 1
print(sum(all_metadata))

# part 2
sorted_all_child = sorted(all_child, key=(lambda x: x[0]))

# NOTE: node is a tuple
# (level, num. of child, pid(None if root, or tuple otherwise), metadata values, sum(metadata_values))

def calc_val(node, s):
    all_children_direct = []
    for i in sorted_all_child[1:]:
        if i[2][0] == node[2]:
            all_children_direct.append(i)

    for i in node[3]:
        c_val = None
        for j in all_children_direct:
            if j[2][1] == i:
                c_val = j
                break
        
        if c_val != None:
            if c_val[1] == 0:
                s += c_val[4]
            else:
                s += calc_val(c_val, 0)
    
    return s
        

root_value = calc_val(sorted_all_child[0], 0)
print(root_value)
