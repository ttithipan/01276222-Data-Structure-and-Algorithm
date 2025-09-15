def print_rods(rods, n):
    print("|  |  |")  # rod caps with spaces between

    for level in range(n, 0, -1):
        row_parts = []

        # Rod A
        if len(rods['A']) >= level:
            disk = rods['A'][level - 1]
            row_parts.append(f"{disk}")
        else:
            row_parts.append("|")

        # Rod B
        if len(rods['B']) >= level:
            disk = rods['B'][level - 1]
            row_parts.append(f"{disk:>3}")
        else:
            row_parts.append("  |")

        # Rod C
        if len(rods['C']) >= level:
            disk = rods['C'][level - 1]
            row_parts.append(f"{disk:>3}")
        else:
            row_parts.append("  |")

        print(''.join(row_parts))



def TowerOfHanoi(n, from_rod, to_rod, aux_rod, rods):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod, rods)
    
    disk = rods[from_rod].pop()
    rods[to_rod].append(disk)
    print(f"move {disk} from  {from_rod} to {to_rod}")
    print_rods(rods, N)
    
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod, rods)


N = int(input("Enter Input : "))

rods = {
    'A': list(range(N, 0, -1)),
    'B': [],
    'C': []
}

print_rods(rods, N)
TowerOfHanoi(N, 'A', 'C', 'B', rods)
