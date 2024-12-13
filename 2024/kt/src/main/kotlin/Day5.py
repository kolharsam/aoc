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


def find_valid_permutation(order, orders):
    """Find the first valid permutation of 'order' that satisfies 'orders'."""

    def backtrack(path, remaining):
        if not remaining:
            # Check if the constructed path is valid
            if all(
                all((path[i], path[j]) in orders for j in range(i + 1, len(path)))
                for i in range(len(path))
            ):
                return path
            return None

        for i, item in enumerate(remaining):
            result = backtrack(path + [item], remaining[:i] + remaining[i + 1 :])
            if result:
                return result

        return None

    return backtrack([], order)


def day5():
    file_path = "./../../../inputs/input5"
    orders, pages = parse_input(file_path)

    right_orders = []
    wrong_orders = []

    # Classify pages as right or wrong
    for page in pages:
        if all(
            all((page[i], page[j]) in orders for j in range(i + 1, len(page)))
            for i in range(len(page))
        ):
            right_orders.append(page)
        else:
            wrong_orders.append(page)

    # Part 1: Middle element sum of right orders
    mids = [middle(page) for page in right_orders if middle(page) is not None]
    print(sum_list(mids))

    # Part 2: Fix wrong orders
    new_right_orders = []

    for ord in wrong_orders:
        valid_perm = find_valid_permutation(ord, orders)
        if valid_perm:
            new_right_orders.append(valid_perm)

    mids2 = [middle(page) for page in new_right_orders if middle(page) is not None]
    print(sum_list(mids2))


if __name__ == "__main__":
    day5()
