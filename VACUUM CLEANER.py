def vacuum_cleaner():
    # Take user input for initial conditions
    location = input("Enter vacuum location (A or B): ").upper()
    status_A = input("Enter status of Room A (Clean or Dirty): ").capitalize()
    status_B = input("Enter status of Room B (Clean or Dirty): ").capitalize()

    print("\nInitial State:")
    print(f"Vacuum is at: {location}")
    print(f"Room A is: {status_A}")
    print(f"Room B is: {status_B}")

    actions = []

    if location == "A":
        if status_A == "Dirty":
            actions.append("Clean Room A")
            status_A = "Clean"
        actions.append("Move to Room B")
        if status_B == "Dirty":
            actions.append("Clean Room B")
            status_B = "Clean"
    elif location == "B":
        if status_B == "Dirty":
            actions.append("Clean Room B")
            status_B = "Clean"
        actions.append("Move to Room A")
        if status_A == "Dirty":
            actions.append("Clean Room A")
            status_A = "Clean"

    print("\nActions:")
    for action in actions:
        print(f"- {action}")

    print("\nFinal State:")
    print(f"Vacuum is at: {'B' if location == 'A' else 'A'}")
    print(f"Room A is: {status_A}")
    print(f"Room B is: {status_B}")

# Run the vacuum cleaner simulation
vacuum_cleaner()
