def mix_colours(primary, secondary):
    primary = primary.upper()
    secondary = secondary.upper()

    combos = [
        (["R", "B"], "P"),
        (["R", "Y"], "O"),
        (["B", "Y"], "G")
    ]

    for colours, result in combos:
        if sorted([primary, secondary]) == sorted(colours):
            print("Your colour is:", result)
            return

    if primary == secondary:
        print(f"You entered the same colour twice: {primary}. It stays the same.")
    else:
        print("Unknown combination. Try R, B, or Y.")

primary = input("Enter your primary colour (R, B, Y): ")
secondary = input("Enter your secondary colour (R, B, Y): ")

mix_colours(primary, secondary)