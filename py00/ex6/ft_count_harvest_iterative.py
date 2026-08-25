#!/usr/bin/python3

def ft_count_harvest_iterative() -> None:
    total_days:  int = int(input("Days until harvest: "))
    for i in range(1, total_days + 1):
        print("Day ", i)
    print("Harvest time!")
