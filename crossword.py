import math
import string
import re
import copy
def generateGameBoard(nRows, nCols)
'.' for i in range(nCols) for j in range(nRows)
    return arr


def loadWord(boardData, nRows, nCols, coord, word, dir):
    if coord[0].isalpha():  # checking coord whether it's number or alphabet
        rows = (ord(coord[0]) - 55) - 1
    else:
        rows = (int(coord[0])) - 1
    if coord[1].isalpha():
        cols = (ord(coord[1]) - 55) - 1
    else:
        cols = (int(coord[1])) - 1

    if dir == "H":  # place the word left to right
        for i in range(0, len(word)):
            boardData[rows + 0 * i][cols + 1 * i] = word[i]
    if dir == "V":  # place top to bottom
        for i in range(0, len(word)):
            boardData[rows + 1 * i][cols + 0 * i] = word[i]

    return boardData


def checkCoord(nRows, nCols, coord):
    rows = chr(nRows + 55)
    cols = chr(nCols + 55)

    regex1 = [r'^(?!\s*$)^[A-Z1-9]{2}$']  # checking coord whether it's valid or not
    rowcheck = r"^[A-%s1-9]" % rows
    colcheck = r".*[A-%s1-9]$" % cols
    for pattern in regex1:
        match = re.match(pattern, coord)
        match1 = re.match(rowcheck, coord)
        match2 = re.match(colcheck, coord)
        if match and match1 and match2:
            return True
        else:
            return False


def updateGameBoard(boardData, boardMask, nRows, nCols, coord, score, lastMove):
    strng = ""
    if checkCoord(nRows, nCols, coord):  # if coord is valid
        if coord[0].isalpha():
            rows = (ord(coord[0]) - 55) - 1
        else:
            rows = (int(coord[0])) - 1
        if coord[1].isalpha():
            cols = (ord(coord[1]) - 55) - 1
        else:
            cols = (int(coord[1])) - 1
        checkword = boardData[rows][cols]
        if checkword != "." and checkword != "~":  # checking whether if it's not dot or tilda
            lastMove = coord
            xright = nCols - cols
            xleft = nCols - xright
            ytop = nRows - rows
            ybottom = nRows - ytop
            strng = " FOUND " + "'" + boardData[rows][cols] + "'" + " at "
            for i in range(xright):            # checking all directions for alphabet
                tmp = boardData[rows + 0 * i][cols + 1 * i]
                if tmp != "." and tmp != "~" and tmp != " " and tmp != boardMask[rows + 1 * i][cols + 0 * i]:
                    boardMask[rows + 0 * i][cols + 1 * i] = tmp
                    score = score + 5

                elif tmp == "." or tmp == "~" or tmp == " " or tmp == boardMask[rows + 1 * i][cols + 0 * i]:
                    break
            for j in range(1, xleft):
                tmp = boardData[rows + 0 * j][cols - 1 * j]
                if tmp != "." and tmp != "~" and tmp != " " and tmp != boardMask[rows + 1 * j][cols + 0 * j]:
                    boardMask[rows + 0 * j][cols - 1 * j] = tmp
                    score = score + 5
                elif tmp == "." or tmp == "~" or tmp == " " or tmp == boardMask[rows + 1 * j][cols + 0 * j]:
                    break

            for k in range(1, ytop):
                tmp = boardData[rows + 1 * k][cols + 0 * k]
                if tmp != "." and tmp != "~" and tmp != " " and tmp != boardMask[rows + 1 * k][cols + 0 * k]:
                    boardMask[rows + 1 * k][cols + 0 * k] = tmp
                    score = score + 5
                elif tmp == "." or tmp == "~" or tmp == " " or tmp == boardMask[rows + 1 * k][cols + 0 * k]:
                    break

            for n in range(1, ybottom):
                tmp = boardData[rows - 1 * n][cols + 0 * n]
                if tmp != "." and tmp != "~" and tmp != " " and tmp != boardMask[rows - 1 * n][cols + 0 * n]:
                    boardMask[rows - 1 * n][cols + 0 * n] = tmp
                    score = score + 5
                elif tmp == "." or tmp == "~" or tmp == " " or tmp == boardMask[rows - 1 * n][cols + 0 * n]:
                    break
        elif checkword == "." or checkword == "~":
            boardMask[rows][cols] = "~"
            strng = " NO letter FOUND at "

        finalboard = (
                ' ' * (2) + "Python Crossword Puzzle..." + '\n' + ' ' * (2)
                + ''.join(str(i) if i < 10 else chr(i + 55) for i in range(1, nCols + 1)) + '\n'
                + '' * 1)
        for i, row in enumerate(boardMask):
            finalboard += (
                    (str(i + 1) if i < 9 else chr(i + 56)).zfill(1) + '|'
                    + ''.join(str(elem) for elem in row) + '|' + '\n')
        finalboard += (
                "Current Score:" + str(score).zfill(4) + "  " + "Last Move:" + strng + "[" + coord[0] + "," + coord[
            1] + "]")
        print(finalboard)
        return boardData, boardMask, score, lastMove
    else:
        strng = " [" + coord[0] + "," + coord[1] + "] " + "is an INVALID COORDINATE"
           #  printing values of board mask
        finalboard = (
                ' ' * (2) + "Python Crossword Puzzle..." + '\n' + ' ' * (2)
                + ''.join(str(i) if i < 10 else chr(i + 55) for i in range(1, nCols + 1)) + '\n'
                + '' * 1)
        for i, row in enumerate(boardMask):
            finalboard += (
                    (str(i + 1) if i < 9 else chr(i + 56)).zfill(1) + '|'
                    + ''.join(str(elem) for elem in row) + '|' + '\n')
        finalboard += ("Current Score:" + str(score).zfill(4) + "  " + "Last Move:" + strng)
        print(finalboard)
        return boardData, boardMask, score, lastMove
def main( ) :
    score = 0
    coords = [ "25", "2A", "XL", "9Q", "1D", "6J", "93", "B4", "AF" ]
    lastMove = ""
    board = generateGameBoard(20, 26)
    mask = generateGameBoard(20, 26)
    board = loadWord(board, 20, 26, "29", "HELLO", "H") # loading words onto game

    board = loadWord(board, 20, 26, "1D", "NO", "V")
    board = loadWord(board, 20, 26, "2A", "EXAMINE", "V")
    board = loadWord(board, 20, 26, "5J", "AREA", "V")

    board = loadWord(board, 20, 26, "6H", "NORTH", "H")
    board = loadWord(board, 20, 26, "93", "PYTHON", "H")
    board = loadWord(board, 20, 26, "AD", "PUZZLE", "H")
    board = loadWord(board, 20, 26, "B4", "7-SEAS", "H")
    board = loadWord(board, 20, 26, "AF", "ZOO", "V")
    for coord in coords :
    (board, mask, score, lastMove) = updateGameBoard(board, mask, 20,26, coord, score, lastMove)
     print( )