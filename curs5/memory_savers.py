import copy

print("Memory Savers!!!")

my_lambda = lambda x, y: x + y
my_sum = my_lambda(2, 3)
print(my_sum)

print(id(my_lambda))
print(id(lambda: 1))
print(id(my_lambda))
print(id(lambda: 3))

players = [
    {
        "first_name": "Sebastian",
        "last_name": "Mocanu",
        "rank": 3
    },
    {
        "first_name": "Ana-Maria Luisa",
        "last_name": "Mocanu",
        "rank": 1
    },
    {
        "first_name": "Medi",
        "last_name": "Mogoase",
        "rank": 2
    },
]

print(f"Unordered list --> {players}")
sorted_players = sorted(players, key=lambda player: player['rank'])
print(f"Sorted list    --> {sorted_players}")
reversed_players = sorted(players, key=lambda player: player['rank'], reverse=True)
print(f"Reversed list  --> {reversed_players}")


def check_top_3_player(player):
    updated_player = copy.deepcopy(player)
    updated_player['is_top_3'] = True if player["rank"] < 4 else False

    return updated_player


top_players = list(map(check_top_3_player, players))
print(top_players)


def filter_all_mcdonalds(player):
    if player["last_name"] == "Mocanu":
        return True

    return False


all_mcdonalds = list(filter(filter_all_mcdonalds, players))
print(all_mcdonalds)

all_mcdonalds = list(filter(lambda player: player["last_name"] == "Mocanu", players))
print(all_mcdonalds)

letters = ['a', 'b', 'c', "z"]
numbers = [1, 2, 3]

for l, n in zip(letters, numbers):
    print(f"{l} - {n}")


my_numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for nr in my_numbers:
    squared_numbers.append(nr ** 2)

print(squared_numbers)

squared_numbers = [nr ** 2 for nr in my_numbers]
print(squared_numbers)
squared_even_numbers = [nr ** 2 for nr in my_numbers if nr % 2 == 0]
print(squared_even_numbers)





