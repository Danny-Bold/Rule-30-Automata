import json
import numpy as np
import matplotlib.pyplot as plt

"""

Key in RULES dict logic:

The binary equivalent of the key is the sequence.

E.g. 4 = 0b100, so 4: 1 means [1, 0, 0] gives a value of 1 on the next row.

"""

RULES = {
    7: 0,
    6: 0,
    5: 0,
    4: 1,
    3: 1,
    2: 1,
    1: 1,
    0: 0
}

COLOURS = {
    0: (0, 0, 0),
    1: (1, 1, 1)
}


def main():
    # saved = open('aut.txt', 'wt')
    #
    # saved.write(json.dumps([[1]]))
    #
    # saved.close()

    iterations = 2500

    array = [[1], [1, 1, 1]]

    for row in range(iterations):

        newLine = []

        currentRow = array[-1]

        newLine.append(RULES[currentRow[0]])

        newLine.append(RULES[2 * currentRow[0] + currentRow[1]])

        for x in range(1, len(currentRow) - 1):
            newLine.append(RULES[4 * currentRow[x - 1] + 2 * currentRow[x] + currentRow[x + 1]])

        newLine.append(RULES[4 * currentRow[-2] + 2 * currentRow[-1]])
        newLine.append(RULES[4 * currentRow[-1]])

        array.append(newLine)

    genImage(array)


def genImage(array):
    height = len(array)
    img = np.zeros((height, 2 * height - 1, 3))

    for x in range(len(array)):
        row = array[x]

        coords = [y - x + height - 1 for y in range(len(row))]

        for y in range(len(coords)):
            img[x, coords[y]] = COLOURS[row[y]]


    plt.imsave('aut.png', img)


if __name__ == '__main__':
    main()
