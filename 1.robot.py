# Create room using user input
def create_room():
    room = []
    print("Enter the room (4x4 grid):")
    print("Enter 1 for Dirty and 0 for Clean")

    for i in range(4):
        row = list(map(int, input(f"Enter row {i+1} (4 values separated by space): ").split()))
        room.append(row)
    
    return room

# Display the grid
def display_room(room):
    for row in room:
        print(" ".join(['D' if cell == 1 else 'C' for cell in row]))
    print()

# Clean the room
def clean_room(room):
    cleaned_positions = []
    total_dirty = 0

    # Count dirty cells
    for i in range(4):
        for j in range(4):
            if room[i][j] == 1:
                total_dirty += 1

    # Cleaning
    cleaned_count = 0
    for i in range(4):
        for j in range(4):
            if room[i][j] == 1:
                room[i][j] = 0
                cleaned_positions.append((i, j))
                cleaned_count += 1

    # Performance
    performance = (cleaned_count / total_dirty * 100) if total_dirty > 0 else 100

    return cleaned_positions, performance


# Main program
room = create_room()

print("\nRoom before cleaning:")
display_room(room)

cleaned_positions, performance = clean_room(room)

print("Room after cleaning:")
display_room(room)

print("Cleaned positions (row, column):")
for pos in cleaned_positions:
    print(pos)

print(f"\nPerformance: {performance:.2f}%")