def count_valid_sets(row):
    count = 0
    n = len(row)

    for i in range(n - 2):
        
        if row[i] != row[i + 1] and row[i + 1] != row[i + 2] and row[i] != row[i + 2]:
            count += 1

    return count

def find_winner(ashok_row, anand_row):

    ashok_count = count_valid_sets(ashok_row)
    anand_count = count_valid_sets(anand_row)

   
    if ashok_count > anand_count:
        return "Ashok"
    elif anand_count > ashok_count:
        return "Anand"
    else:
        return "Draw"


ashok_row = input().strip()
anand_row = input().strip()


result = find_winner(ashok_row, anand_row)
print(result)
