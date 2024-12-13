def parse_input(file_path):
    orders = set()
    pages = []

    with open(file_path, "r") as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if "|" in line:
            a, b = map(int, line.split("|"))
            orders.add((a, b))
        elif "," in line:
            pages.append(list(map(int, line.split(","))))

    return orders, pages


def middle(lst):
    """Return the middle element of a list."""
    return lst[len(lst) // 2] if lst else None


def sum_list(lst):
    """Sum elements of a list."""
    return sum(lst)


def reorder_list(page, orders):
    """
    Reorder a page to satisfy the order constraints in the 'orders' set.
    If it's impossible to reorder the page, return None.
    """
    # Construct a directed graph from the orders
    graph = {num: [] for num in page}
    for a, b in orders:
        if a in graph and b in graph:
            graph[a].append(b)

    # Perform topological sort to find a valid order
    visited = {}
    result = []

    def dfs(node):
        if node in visited:
            return visited[node]  # Return False if there's a cycle
        visited[node] = False
        for neighbor in graph[node]:
            if neighbor not in visited or not visited[neighbor]:
                if not dfs(neighbor):
                    return False
        visited[node] = True
        result.append(node)
        return True

    for num in page:
        if num not in visited:
            if not dfs(num):
                return None  # Cycle detected, no valid order

    result.reverse()  # Reverse the result of topological sort
    return result if set(result) == set(page) else None


def is_valid_page(page, orders):
    """Check if a page satisfies the order rules."""
    return all(
        all((page[i], page[j]) in orders for j in range(i + 1, len(page)))
        for i in range(len(page))
    )


def day5():
    file_path = "./../../../inputs/input5"
    orders, pages = parse_input(file_path)

    right_orders = []
    wrong_orders = []

    # Classify pages into right and wrong orders
    for page in pages:
        if is_valid_page(page, orders):
            right_orders.append(page)
        else:
            wrong_orders.append(page)

    # Part 1: Middle element sum of right orders
    mids = [middle(page) for page in right_orders if middle(page) is not None]
    print(sum_list(mids))

    # Part 2: Fix wrong orders
    new_right_orders = []
    for ord in wrong_orders:
        reordered = reorder_list(ord, orders)
        if reordered:
            new_right_orders.append(reordered)

    mids2 = [middle(page) for page in new_right_orders if middle(page) is not None]
    print(sum_list(mids2))


if __name__ == "__main__":
    day5()
