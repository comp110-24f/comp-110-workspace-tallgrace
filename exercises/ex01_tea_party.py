__author__ = "730649724"

"""tea party numbers"""


def main_planner(guest: int) -> None:
    """bringing everything together for how much of each"""
    return None
    print(tea_bags)
    print(round(treats))
    print(cost)


def tea_bags(people: int) -> int:
    """number of people impacts number of tea bags"""
    return people * 2


def treats(people: int) -> float:
    """for each tea a guest drinks, they will, on average, want 1.5 treats with it"""
    return tea_bags(people) * 1.5


def cost(tea_count: int, treat_count: int) -> float:
    "each bag of tea caost 0.50 and each treat cost 0.75"
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("how many guests are attending your tea party?")))
