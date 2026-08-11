def ft_count_harvest_recursive() -> None:
    total_days:  int = int(input("Days until harvest: "))

    def count_day(day: int):
        if day > total_days:
            print("Harvest time!")
        else:
            print("Day ", day)
            count_day(day + 1)
