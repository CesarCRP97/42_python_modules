def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        print(seed_type.capitalize(), "seeds: ", quantity,
              " packets available")
    elif unit == "grams":
        print(seed_type.capitalize(), "seeds: ", quantity,
              " grams total")
    elif unit == "area":
        print(seed_type.capitalize(), "seeds: covers ", quantity,
              " square meters")
    else:
        print("Unknown unit type")


ft_seed_inventory("Aubergene", 42, "area")
ft_seed_inventory("Pumpkin", 42, "packets")
ft_seed_inventory("Strawberry", 42, "grams")
