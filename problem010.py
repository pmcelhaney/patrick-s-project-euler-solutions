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

input ="""
00 01 02 03 04 05 06 07 08 09
10 11 12 13 14 15 16 17 18 19
20 21 22 23 24 25 26 27 28 29
30 31 32 33 34 35 36 37 38 39
40 41 42 43 44 45 46 47 48 49
50 51 52 53 54 55 56 57 58 59
60 61 62 63 64 65 66 67 68 69
70 71 72 73 74 75 76 77 78 79
80 81 82 83 84 85 86 87 88 89
90 91 92 93 94 95 96 97 98 99
"""

data = [map(int, row.split(" ")) for row in input.split('\n') if len(row) > 0]




def find_rows(data):
    height = len(data)
    width = len(data[0])
    for x in xrange(0, height):
        for y in xrange(0, width):
            if y+4 <= height:
                yield [data[x][y+offset] for offset in xrange(0,4)]
            if x+4 <= height:
                yield [data[x+offset][y] for offset in xrange(0,4)]    
            if y+4 <= height and x+4 <= width:    
                yield [data[x+offset][y+offset] for offset in xrange(0,4)]      
            if x >= 3 and y >= 3:
                yield [data[x-offset][y-offset] for offset in xrange(0,4)] 
                
print tuple(find_rows(data))