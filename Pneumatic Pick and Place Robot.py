# Pneumatic-Pick-and-Place-Robot
# Pneumatic Pick and Place Robot

while True:
    print("\n--- PNEUMATIC PICK AND PLACE ROBOT ---")
    print("1. Start Robot")
    print("2. Stop Robot")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("\nRobot started!")

        print("1. Moving to object...")
        print("2. Gripper closing...")
        print("3. Object picked!")
        print("4. Moving to destination...")
        print("5. Gripper opening...")
        print("6. Object placed!")

        print("\nPick and Place operation completed.")

    elif choice == "2":
        print("Robot stopped.")

    elif choice == "3":
        print("Program ended.")
        break

    else:
        print("Invalid choice!")
