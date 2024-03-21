# 9-bo'lim
def josephus_problem(n, k):
    people = list(range(1, n + 1))
    index = 0
    print(f"Boshlang'ich odamlar ro'yxati: {people}")
    while len(people) > 1:
        index = (index + k - 1) % len(people)
        print(f"{people[index]}-sonli odam chiqarib tashlandi.")
        people.pop(index)
    print(f"Omon qolgan odam: {people[0]}")
    return people[0]


josephus_problem(7, 3)
