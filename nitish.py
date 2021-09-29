def next_number(A, position):
    """
    :param A: global
    :param position: true for even
    :return: the perfect number
    """
    if position % 2:  # requirement of an odd number
        for x in A:
            if x % 2:
                return A.pop(A.index(x))
        for x in A:
            if not x % 2:
                return A.pop(A.index(x))
    else:
        for x in A:
            if not x % 2:
                return A.pop(A.index(x))
        for x in A:
            if x % 2:
                return A.pop(A.index(x))


class TC:
    def __init__(self, A):
        self.A = list(map(int, A))

    def perfect_sort(self):
        A = []
        for i in range(len(self.A)):
            A.append(next_number(self.A, i))
        self.A = A

    def do_the_fuckings(self):
        ejaculation, position = 0, 1
        for x in self.A:
            ejaculation += ((x + position) % 2)
            position += 1
        print(ejaculation)


x = int(input())
for i in range(x):
    if i != (x - 1):
        input()
    a = TC(input().split(' '))
    a.perfect_sort()
    a.do_the_fuckings()
