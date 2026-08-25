#!/usr/bin/python3

def ft_harvest_total() -> None:
    total_harvest: int = 0
    total_harvest += int(input("Day 1 harvest: "))
    total_harvest += int(input("Day 2 harvest: "))
    total_harvest += int(input("Day 3 harvest: "))
    print("Total harvest: ", total_harvest)
