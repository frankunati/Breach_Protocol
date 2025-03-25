import random
import os

# Color codes for terminal (Optional)
class Colors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ASCII Cyberpunk-Style Logo
def show_logo():
    clear_screen()
    logo = f"""{Colors.CYAN}
    ____                            __       ____                __                       __
   / __ ) _____ ___   ____ _ _____ / /_     / __ \ _____ ____   / /_ ____   _____ ____   / /
  / __  |/ ___// _ \ / __ `// ___// __ \   / /_/ // ___// __ \ / __// __ \ / ___// __ \ / / 
 / /_/ // /   /  __// /_/ // /__ / / / /  / ____// /   / /_/ // /_ / /_/ // /__ / /_/ // /  
/_____//_/    \___/ \__,_/ \___//_/ /_/  /_/    /_/    \____/ \__/ \____/ \___/ \____//_/   
                                                            
    {Colors.YELLOW}Cyberpunk 2077 - Terminal Breach Protocol{Colors.RESET}
    """
    print(logo)

def generate_grid(rows=4, cols=4):
    elements = [hex(random.randint(0, 255))[2:].upper().zfill(2) for _ in range(rows * cols)]
    return [elements[i * cols:(i + 1) * cols] for i in range(rows)]

def generate_buffer_sequence(grid, length=3):
    flat_grid = [item for sublist in grid for item in sublist]
    return random.sample(flat_grid, length)

def display_grid(grid, selected=None):
    clear_screen()
    show_logo()
    print(Colors.YELLOW + "Breach Protocol Grid:\n" + Colors.RESET)

    print("   " + "   ".join([f"{i}" for i in range(len(grid[0]))]))  # Column index
    print("  +" + "---+" * len(grid[0]))  # Top border
    
    for r_idx, row in enumerate(grid):
        row_str = f"{r_idx} |"  # Row index
        for c_idx, val in enumerate(row):
            if selected and selected == (r_idx, c_idx):
                row_str += f"{Colors.GREEN}[{val}]{Colors.RESET} | "
            else:
                row_str += f" {val}  | "
        print(row_str)
        print("  +" + "---+" * len(row))  # Row separator
    print()

def play_game():
    rows, cols = 4, 4
    grid = generate_grid(rows, cols)
    buffer_sequence = generate_buffer_sequence(grid)
    
    show_logo()
    print(Colors.YELLOW + "Buffer sequence to match:" + Colors.RESET, " -> ".join(buffer_sequence))
    input("Press Enter to start...")

    selected_cells = []
    row, col = 0, 0  # Start position
    moves = len(buffer_sequence)  # Limited moves

    for move in range(moves):
        display_grid(grid, (row, col))
        print(Colors.CYAN + "Buffer sequence:" + Colors.RESET, " -> ".join(buffer_sequence))
        print(Colors.GREEN + "Selected so far:" + Colors.RESET, " -> ".join([grid[r][c] for r, c in selected_cells]))
        print(f"Move {move+1}/{moves}. You can move:")
        print("1. Pick from current row")
        print("2. Pick from current column")
        choice = input("Enter choice (1/2): ")

        if choice == "1":
            new_col = int(input(f"Pick column (0-{cols-1}): "))
            selected_cells.append((row, new_col))
            col = new_col
        elif choice == "2":
            new_row = int(input(f"Pick row (0-{rows-1}): "))
            selected_cells.append((new_row, col))
            row = new_row
        else:
            print(Colors.RED + "Invalid choice. Try again." + Colors.RESET)
            continue

    selected_values = [grid[r][c] for r, c in selected_cells]
    if selected_values == buffer_sequence:
        print(Colors.GREEN + "Success! Breach completed." + Colors.RESET)
    else:
        print(Colors.RED + "Failure. Sequence mismatch." + Colors.RESET)

if __name__ == "__main__":
    play_game()
