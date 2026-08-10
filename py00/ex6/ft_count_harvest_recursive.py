def ft_count_harvest_recursive():
    total_days = int(input("Days until harvest: "))

    def count_day(day):
        if day > total_days:
            print("Harvest time!")
        else:
            print("Day ", day)
            count_day(day + 1)

    count_day(1)
