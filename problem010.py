input = """
57 12 81 02 54 82 30 22 07 46
77 13 58 37 02 77 17 27 68 71
34 89 42 81 09 80 75 74 11 65
95 60 07 30 43 60 57 28 71 42
05 80 70 39 01 53 92 27 94 77
61 38 62 65 95 18 78 24 92 93
96 69 51 98 81 25 99 88 25 65
18 80 90 91 74 70 84 51 47 72
92 14 39 37 89 90 69 34 38 73
62 42 14 12 86 95 99 10 97 52
"""

data = [map(int, row.split(" ")) for row in input.split('\n') if len(row) > 0]

# print [row for row in data]
print max([max([sum(row[x:x+4]) for x in xrange(0,len(row)-4)]) for row in data])
        