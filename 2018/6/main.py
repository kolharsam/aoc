inp = open('input', 'r').readlines()

points = []
for i in inp:
    x, y = i.split(", ")
    points.append((int(x), int(y)))

def calc_manhattan_dist(source, dest):
    return abs(source[0] - dest[0]) + abs(source[1] - dest[1])

def find_min_dist_point(dpl, min_dis):
    ul = []
    
    for i in dpl:
        dis = i[0]
        p = i[1]
        if min_dis == dis:
            ul.append(p)

    if len(ul) == 1:
        return ul[0], True
    else:
        return ul[0], False

point_count = {}
for i in points:
    point_count[i] = 0

hit_list = set()
loc_count = 0
for i in range(501):
    for j in range(501):
        current_point = (j, i)
        
        dists = []
        dist_point_list = []
        
        for s in points:
            d = calc_manhattan_dist(s, current_point)
            dists.append(d)
            dist_point_list.append((d, s))

        # this only works because the assumption that the region will exist
        # in only one place in the given grid where this holds true is infact true
        sum_dists = sum(dists)
        if sum_dists < 10000:
            loc_count += 1
        
        min_dist = min(dists)
        min_dist_point, uniq = find_min_dist_point(dist_point_list, min_dist)

        if i == 0 or j == 0 or j == 500 or i == 500 and uniq:
            hit_list.add(min_dist_point)
        
        if uniq:
            point_count[min_dist_point] += 1

for i in hit_list:
    point_count.__delitem__(i)

# part 1
print(max([i for i in point_count.values()]))
# part 2
print(loc_count)
