


#红方   帅  仕  相  马  车  炮  兵
#       K   A   B   N   R   C   P 
#黑方   将  士  象  马  车  炮  兵
#       k   a   b   n   r   c   p   
ChessDict_Init = {16:'K', 17:'A', 18:'A', 19:'B', 20:'B', 21:'N', 22:'N', 
    23:'R', 24:'R', 25:'C', 26:'C', 27:'P', 28:'P', 29:'P', 30:'P', 31:'P', 
    32:'k', 33:'a', 34:'a', 35:'b', 36:'b', 37:'n', 38:'n', 
    39:'r', 40:'r', 41:'c', 42:'c', 43:'p', 44:'p', 45:'p', 46:'p', 47:'p'}

DictChess_Init = {}
DictChess_value = {}

for key,value in ChessDict_Init.items():
    if value not in DictChess_Init:
        DictChess_Init.update({value:key})
        DictChess_value.update({value:True})


LegalPosition_Init =[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0],
    [0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0],
    [0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0],
    [0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0],
    [0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0],
    [0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0],
    [0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0],
    [0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0],
    [0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0],
    [0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

Board_Init = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0],
    [0,0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0],
    [0,0,0,39,37,35,33,32,34,36,38,40,0,0,0,0],
    [0,0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0],
    [0,0,0, 0,41, 0, 0, 0, 0, 0,42, 0, 0,0,0,0],
    [0,0,0,43, 0,44, 0,45, 0,46, 0,47, 0,0,0,0],
    [0,0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0],
    [0,0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0],
    [0,0,0,27, 0,28, 0,29, 0,30, 0,31, 0,0,0,0],
    [0,0,0, 0,25, 0, 0, 0, 0, 0,26, 0, 0,0,0,0],
    [0,0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0],
    [0,0,0,23,21,19,17,16,18,20,22,24, 0,0,0,0],
    [0,0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


class ChessBoard:
    def __init__(self):
        self.Board = Board_Init
        self.LegalPosition = LegalPosition_Init
        self.ChessDict = ChessDict_Init
        self.DictChess = DictChess_Init
        self.DictChess_value = DictChess_value
        self.side = 0

    def ArrToFen(self):
        FenStr = ''
        for i in range(3,13):
            cnt = 0
            for j in range(3,12):
                pc = self.Board[i][j]
                if pc == 0:
                    cnt = cnt + 1
                elif cnt != 0:
                    FenStr = FenStr + str(cnt) + self.ChessDict[pc]
                    cnt = 0
                else:
                    FenStr = FenStr + self.ChessDict[pc]
            if cnt > 0:
                FenStr = FenStr + str(cnt)
                cnt = 0
            FenStr = FenStr + '/'
        if self.side == 0:
            turn = 'w'
        else:
            turn = 'b'
        FenStr = FenStr + turn
        return FenStr


        # ??????????????
    def FenToArr(self, FenStr):
        i = 3
        j = 3
        flag = 0
        for index in range(len(FenStr)):
            char = FenStr[index]
            # print(char)
            if char == '/':
                i = i + 1
                j = 3
                continue
            try:
                cnt = int(char)
                j = j + cnt
            except:
                # if  self.DictChess_value[self.DictChess[char]]:
                #     self.Board[i][j] = self.DictChess[char]
                #     self.DictChess_value[self.DictChess[char]] = False
                # else
                if self.DictChess_value[char]:
                    self.Board[i][j] = self.DictChess[char]
                    self.DictChess_value[char] = False
                else:
                    self.Board[i][j] = self.DictChess[char]+1
                    self.DictChess_value[char] = True

                j = j + 1
            if char == 'w':
                self.side = 0
            if char == 'b':
                self.side = 1
            return self.Board




CB = ChessBoard()
print(CB.ArrToFen())
print(CB.FenToArr(CB.ArrToFen()))
            