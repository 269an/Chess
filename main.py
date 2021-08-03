import os

def printBoard():
    print("/"," "*5,end="")
    for letter in alphabets :
        print(letter," "*(13-len(letter)),end="")
    print("\n")
    
    for key in Board:
        print(key," "*5,end="")
        for moreKey in Board[key] :
            print(Board[key][moreKey]," "*(13-len(Board[key][moreKey])),end="")
        print("\n")
    print("\n")
    
def printValidBoard(valid):
    print("/"," "*5,end="")
    for letter in alphabets :
        print(letter," "*(13-len(letter)),end="")
    print("\n")
    
    for key in Board:
        print(key," "*5,end="")
        for moreKey in Board[key] :
            if (moreKey+key in valid):
                idk = "("+Board[key][moreKey]+")"
                print(idk," "*(13-len(idk)),end="")
            else:
                print(Board[key][moreKey]," "*(13-len(Board[key][moreKey])),end="")
        print("\n")
    print("\n")
    
def move(start, end,BlackTurn):
    valid = showValid(start,BlackTurn)
    if (len(valid)==0) : return False
    if (end[::-1] in valid) :
        piece = Board[end[0]][end[1]]
        Board[end[0]][end[1]]=Board[start[0]][start[1]]
        Board[start[0]][start[1]]="."
        os.system("clear")
        printBoard()
        return True
    else:
        return False
        
        
def showValid(start,BlackTurn):

    valid = []
    invalid = []

    piece = Board[start[0]][start[1]]

    if BlackTurn :
        if piece[0]=="B" : pass
        else : return valid
    else :
        if piece[0]=="W" : pass
        else : return valid
    
    if piece[2:]=="Pawn" :
        if piece[0]=="W" :
            #WE CHECK IF IT CAN ATTACK DIAGONALLY
            DfrontCol = start[1]
            DfrontRow = str(int(start[0])+1)
            Dfront = Board[DfrontRow][DfrontCol]
            DfrontIndex = DfrontCol+DfrontRow
            
            DleftCol = alphabets[alphabets.index(start[1])-1]
            DleftRow = str(int(start[0])+1)
            Dleft = Board[DleftRow][DleftCol]
            DleftIndex = DleftCol+DleftRow
            
            DrightCol = alphabets[alphabets.index(start[1])+1]
            DrightRow = str(int(start[0])+1)
            Dright = Board[DrightRow][DrightCol]
            DrightIndex = DrightCol+DrightRow
            
            if Dleft ==".": #EITHER DLEFT IS EMPTY
                invalid.append(DleftIndex)
            else: #OR NOT
                if Dleft[0]=="W" : invalid.append(DleftIndex) #IF NOT EMPTY, THEN EITHER WHITE
                else : valid.append(DleftIndex) # OR NOT
            if Dright ==".": #EITHER DLEFT IS EMPTY
                invalid.append(DrightIndex)
            else: #OR NOT
                if Dright[0]=="W" : invalid.append(DrightIndex) #IF NOT EMPTY, THEN EITHER WHITE
                else : valid.append(DrightIndex) # OR NOT
            #WE CHECK IF IT CAN GO FRONT OR NOT
            if Dfront!="." :
                invalid.append(DfrontIndex)
            else :
                valid.append(DfrontIndex)
                
            if start[0]=="2" :
                    
                DTwoFrontCol = start[1]
                DTwoFrontRow = str(int(start[0])+2)
                DTwoFront = Board[DTwoFrontRow][DTwoFrontCol]
                DTwoFrontIndex = DTwoFrontCol+DTwoFrontRow
                if Dfront!=".":
                    invalid.append(DTwoFrontIndex)
                elif DTwoFront==".":
                    valid.append(DTwoFrontIndex)
                else :
                    invalid.append(DTwoFrontIndex)
        else :
            #WE CHECK IF IT CAN ATTACK DIAGONALLY
            DfrontCol = start[1]
            DfrontRow = str(int(start[0])-1)
            Dfront = Board[DfrontRow][DfrontCol]
            DfrontIndex = DfrontCol+DfrontRow
            
            DleftCol = alphabets[alphabets.index(start[1])-1]
            DleftRow = str(int(start[0])-1)
            Dleft = Board[DleftRow][DleftCol]
            DleftIndex = DleftCol+DleftRow
            
            DrightCol = alphabets[alphabets.index(start[1])+1]
            DrightRow = str(int(start[0])-1)
            Dright = Board[DrightRow][DrightCol]
            DrightIndex = DrightCol+DrightRow
            
            if Dleft ==".": #EITHER DLEFT IS EMPTY
                invalid.append(DleftIndex)
            else: #OR NOT
                if Dleft[0]=="B" : invalid.append(DleftIndex) #IF NOT EMPTY, THEN EITHER WHITE
                else : valid.append(DleftIndex) # OR NOT
            if Dright ==".": #EITHER DLEFT IS EMPTY
                invalid.append(DrightIndex)
            else: #OR NOT
                if Dright[0]=="B" : invalid.append(DrightIndex) #IF NOT EMPTY, THEN EITHER WHITE
                else : valid.append(DrightIndex) # OR NOT
            #WE CHECK IF IT CAN GO FRONT OR NOT
            if Dfront!="." :
                invalid.append(DfrontIndex)
            else :
                valid.append(DfrontIndex)
                
            if start[0]=="7" :
                DTwoFrontCol = start[1]
                DTwoFrontRow = str(int(start[0])-2)
                DTwoFront = Board[DTwoFrontRow][DTwoFrontCol]
                DTwoFrontIndex = DTwoFrontCol+DTwoFrontRow
                if Dfront!=".":
                    invalid.append(DTwoFrontIndex)
                elif DTwoFront==".":
                    valid.append(DTwoFrontIndex)
                else :
                    invalid.append(DTwoFrontIndex)
    elif piece[2:]=="Rook" :
        FrontCol = start[1]
        FrontRow = str(int(start[0])+1)
        Front = Board[FrontRow][FrontCol]
        FrontIndex = FrontCol+FrontRow
        while(Front[0]!="W"):
            if (Front[0]=="B"):
                valid.append(FrontIndex)
                break
            valid.append(FrontIndex)
            FrontRow = str(int(FrontRow)+1)
            if (FrontRow=="9"):
                break
            Front = Board[FrontRow][FrontCol]
            FrontIndex = FrontCol+FrontRow
            
            
        BehindCol = start[1]
        BehindRow = str(int(start[0])-1)
        Behind = Board[BehindRow][BehindCol]
        BehindIndex = BehindCol+BehindRow
        while(Behind[0]!="W"):
            if (Behind[0]=="B"):
                valid.append(BehindIndex)
                break
            valid.append(BehindIndex)
            BehindRow = str(int(BehindRow)-1)
            if (BehindRow=="0"):
                break
            Behind = Board[BehindRow][BehindCol]
            BehindIndex = BehindCol+BehindRow
            
            
        LeftCol = alphabets[alphabets.index(start[1])-1]
        LeftRow = start[0]
        Left = Board[LeftRow][LeftCol]
        LeftIndex = LeftCol+LeftRow
        while(Left[0]!="W"):
            if (Left[0]=="B"):
                valid.append(LeftIndex)
                break
            valid.append(LeftIndex)
            if LeftCol=="a":
                break
            LeftCol = alphabets[alphabets.index(LeftCol)-1]
            Left = Board[LeftRow][LeftCol]
            LeftIndex = LeftCol+LeftRow
            
            
        RightCol = alphabets[alphabets.index(start[1])+1]
        RightRow = start[0]
        Right = Board[RightRow][RightCol]
        RightIndex = RightCol+RightRow
        while(Right[0]!="W"):
            if (Right[0]=="B"):
                valid.append(RightIndex)
                break
            valid.append(RightIndex)
            if RightCol=="h":
                break
            RightCol = alphabets[alphabets.index(RightCol)+1]
            Right = Board[RightRow][RightCol]
            RightIndex = RightCol+RightRow
    elif piece[2:]=="Horse" :
        One = alphabets[alphabets.index(start[1])-1]+str(int(start[0])-2)
        if (alphabets.index(start[1])-1<0 or int(start[0])-2<1 or int(start[0])-2>8): pass
        else: valid.append(One)
        
        Five = alphabets[alphabets.index(start[1])-1]+str(int(start[0])+2)
        if (alphabets.index(start[1])-1<0 or int(start[0])-2<1 or int(start[0])+2>8): pass
        else: valid.append(Five)
        
        Three = alphabets[alphabets.index(start[1])+1]+str(int(start[0])+2)
        
        if (alphabets.index(start[1])+1<0 or int(start[0])-2<1 or int(start[0])+2>8):
            pass
        else:
            valid.append(Three)
            
        Seven = alphabets[alphabets.index(start[1])+1]+str(int(start[0])-2)
        
        if (alphabets.index(start[1])+1<0 or int(start[0])-2<1 or int(start[0])-2>8):
            pass
        else:
            valid.append(Seven)

        Six = alphabets[alphabets.index(start[1])-2]+str(int(start[0])+1)
        
        if (alphabets.index(start[1])-2<0 or int(start[0])+1<1 or int(start[0])-2>8):
            pass
        else:
            valid.append(Six)
            
        Two = alphabets[alphabets.index(start[1])-2]+str(int(start[0])-1)
        if (alphabets.index(start[1])-2<0 or int(start[0])-1<1 or int(start[0])-2>8):
            pass
        else:
            valid.append(Two)
        
        Four = alphabets[alphabets.index(start[1])+2]+str(int(start[0])+1)
        
        if (alphabets.index(start[1])+2<0 or int(start[0])+1<1 or int(start[0])-2>8):
            pass
        else:
            valid.append(Four)
            
        Eight = alphabets[alphabets.index(start[1])+2]+str(int(start[0])-1)
        
        if (alphabets.index(start[1])+2<0 or int(start[0])-1<1 or int(start[0])-2>8):
            pass
        else:
            valid.append(Eight)

        for block in valid :
            if Board[block[1]][block[0]][0]=="W":
                valid.remove(block)
    elif piece[2:]=="Bishop" :
        #FOR FRONT RIGHT
        
        FrontCol = alphabets[alphabets.index(start[1])+1]
        FrontRow = str(int(start[0])+1)
        Front = Board[FrontRow][FrontCol]
        FrontIndex = FrontCol+FrontRow
        while(Front[0]!="W"):
            if (Front[0]=="B"):
                valid.append(FrontIndex)
                break
            if (FrontCol=="h"):
                break
            valid.append(FrontIndex)
            FrontCol = alphabets[alphabets.index(FrontCol)+1]
            FrontRow = str(int(FrontRow)+1)
            if (FrontRow=="9"):
                break
            Front = Board[FrontRow][FrontCol]
            FrontIndex = FrontCol+FrontRow
        
        #FOR FRONT LEFT
        
        FrontCol = alphabets[alphabets.index(start[1])-1]
        FrontRow = str(int(start[0])+1)
        Front = Board[FrontRow][FrontCol]
        FrontIndex = FrontCol+FrontRow
        while(Front[0]!="W"):
            if (Front[0]=="B"):
                valid.append(FrontIndex)
                break
            if (FrontCol=="h"):
                break
            valid.append(FrontIndex)
            FrontCol = alphabets[alphabets.index(FrontCol)-1]
            FrontRow = str(int(FrontRow)+1)
            if (FrontRow=="9"):
                break
            Front = Board[FrontRow][FrontCol]
            FrontIndex = FrontCol+FrontRow
        
        #FOR BEHIND RIGHT
        
        BehindCol = alphabets[alphabets.index(start[1])+1]
        BehindRow = str(int(start[0])-1)
        Behind = Board[BehindRow][BehindCol]
        BehindIndex = BehindCol+BehindRow
        while(Behind[0]!="W"):
            if (Behind[0]=="B"):
                valid.append(BehindIndex)
                break
            valid.append(BehindIndex)
            BehindCol = alphabets[alphabets.index(BehindCol)+1]
            BehindRow = str(int(BehindRow)-1)
            if (BehindRow=="0"):
                break
            Behind = Board[BehindRow][BehindCol]
            BehindIndex = BehindCol+BehindRow
        
        #FOR BEHIND LEFT
        
        BehindCol = alphabets[alphabets.index(start[1])-1]
        BehindRow = str(int(start[0])-1)
        Behind = Board[BehindRow][BehindCol]
        BehindIndex = BehindCol+BehindRow
        while(Behind[0]!="W"):
            if (Behind[0]=="B"):
                valid.append(BehindIndex)
                break
            valid.append(BehindIndex)
            BehindCol = alphabets[alphabets.index(BehindCol)-1]
            BehindRow = str(int(BehindRow)-1)
            if (BehindRow=="0"):
                break
            Behind = Board[BehindRow][BehindCol]
            BehindIndex = BehindCol+BehindRow
    elif piece[2:]=="King" :
        #FOR FRONT RIGHT
        
        FrontCol = alphabets[alphabets.index(start[1])+1]
        FrontRow = str(int(start[0])+1)
        Front = Board[FrontRow][FrontCol]
        FrontIndex = FrontCol+FrontRow
        count=0
        while(Front[0]!="W"):
            if (count==1) : break
            if (Front[0]=="B"):
                valid.append(FrontIndex)
                break
            if (FrontCol=="h"):
                break
            valid.append(FrontIndex)
            FrontCol = alphabets[alphabets.index(FrontCol)+1]
            FrontRow = str(int(FrontRow)+1)
            if (FrontRow=="9"):
                break
            Front = Board[FrontRow][FrontCol]
            FrontIndex = FrontCol+FrontRow
            count+=1
        
        #FOR FRONT LEFT
        
        FrontCol = alphabets[alphabets.index(start[1])-1]
        FrontRow = str(int(start[0])+1)
        Front = Board[FrontRow][FrontCol]
        FrontIndex = FrontCol+FrontRow
        count=0

        while(Front[0]!="W"):
            if (count==1) : break
            if (Front[0]=="B"):
                valid.append(FrontIndex)
                break
            if (FrontCol=="h"):
                break
            valid.append(FrontIndex)
            FrontCol = alphabets[alphabets.index(FrontCol)-1]
            FrontRow = str(int(FrontRow)+1)
            if (FrontRow=="9"):
                break
            Front = Board[FrontRow][FrontCol]
            FrontIndex = FrontCol+FrontRow
            count+=1
        
        #FOR BEHIND RIGHT
        
        BehindCol = alphabets[alphabets.index(start[1])+1]
        BehindRow = str(int(start[0])-1)
        Behind = Board[BehindRow][BehindCol]
        BehindIndex = BehindCol+BehindRow
        count=0

        while(Behind[0]!="W"):
            if (count==1) : break
            if (Behind[0]=="B"):
                valid.append(BehindIndex)
                break
            valid.append(BehindIndex)
            BehindCol = alphabets[alphabets.index(BehindCol)+1]
            BehindRow = str(int(BehindRow)-1)
            if (BehindRow=="0"):
                break
            Behind = Board[BehindRow][BehindCol]
            BehindIndex = BehindCol+BehindRow
            count+=1
        
        #FOR BEHIND LEFT
        
        BehindCol = alphabets[alphabets.index(start[1])-1]
        BehindRow = str(int(start[0])-1)
        Behind = Board[BehindRow][BehindCol]
        BehindIndex = BehindCol+BehindRow
        count=0

        while(Behind[0]!="W"):
            if (count==1) : break
            if (Behind[0]=="B"):
                valid.append(BehindIndex)
                break
            valid.append(BehindIndex)
            BehindCol = alphabets[alphabets.index(BehindCol)-1]
            BehindRow = str(int(BehindRow)-1)
            if (BehindRow=="0"):
                break
            Behind = Board[BehindRow][BehindCol]
            BehindIndex = BehindCol+BehindRow
            count+=1
        
        FrontCol = start[1]
        FrontRow = str(int(start[0])+1)
        Front = Board[FrontRow][FrontCol]
        FrontIndex = FrontCol+FrontRow
        count=0

        while(Front[0]!="W"):
            if (count==1) : break
            if (Front[0]=="B"):
                valid.append(FrontIndex)
                break
            valid.append(FrontIndex)
            FrontRow = str(int(FrontRow)+1)
            if (FrontRow=="9"):
                break
            Front = Board[FrontRow][FrontCol]
            FrontIndex = FrontCol+FrontRow
            count+=1
            
            
        BehindCol = start[1]
        BehindRow = str(int(start[0])-1)
        Behind = Board[BehindRow][BehindCol]
        BehindIndex = BehindCol+BehindRow
        count=0

        while(Behind[0]!="W"):
            if (count==1) : break
            if (Behind[0]=="B"):
                valid.append(BehindIndex)
                break
            valid.append(BehindIndex)
            BehindRow = str(int(BehindRow)-1)
            if (BehindRow=="0"):
                break
            Behind = Board[BehindRow][BehindCol]
            BehindIndex = BehindCol+BehindRow
            count+=1
            
            
        LeftCol = alphabets[alphabets.index(start[1])-1]
        LeftRow = start[0]
        Left = Board[LeftRow][LeftCol]
        LeftIndex = LeftCol+LeftRow
        count=0

        while(Left[0]!="W"):
            if (count==1) : break
            if (Left[0]=="B"):
                valid.append(LeftIndex)
                break
            valid.append(LeftIndex)
            if LeftCol=="a":
                break
            LeftCol = alphabets[alphabets.index(LeftCol)-1]
            Left = Board[LeftRow][LeftCol]
            LeftIndex = LeftCol+LeftRow
            count+=1
            
            
        RightCol = alphabets[alphabets.index(start[1])+1]
        RightRow = start[0]
        Right = Board[RightRow][RightCol]
        RightIndex = RightCol+RightRow
        count=0

        while(Right[0]!="W"):
            if (count==1) : break
            if (Right[0]=="B"):
                valid.append(RightIndex)
                break
            valid.append(RightIndex)
            if RightCol=="h":
                break
            RightCol = alphabets[alphabets.index(RightCol)+1]
            Right = Board[RightRow][RightCol]
            RightIndex = RightCol+RightRow
            count+=1
    elif piece[2:]=="Queen" :
        #FOR FRONT RIGHT
        
        FrontCol = alphabets[alphabets.index(start[1])+1]
        FrontRow = str(int(start[0])+1)
        Front = Board[FrontRow][FrontCol]
        FrontIndex = FrontCol+FrontRow
        while(Front[0]!="W"):
            if (Front[0]=="B"):
                valid.append(FrontIndex)
                break
            if (FrontCol=="h"):
                break
            valid.append(FrontIndex)
            FrontCol = alphabets[alphabets.index(FrontCol)+1]
            FrontRow = str(int(FrontRow)+1)
            if (FrontRow=="9"):
                break
            Front = Board[FrontRow][FrontCol]
            FrontIndex = FrontCol+FrontRow
        
        #FOR FRONT LEFT
        
        FrontCol = alphabets[alphabets.index(start[1])-1]
        FrontRow = str(int(start[0])+1)
        Front = Board[FrontRow][FrontCol]
        FrontIndex = FrontCol+FrontRow
        while(Front[0]!="W"):
            if (Front[0]=="B"):
                valid.append(FrontIndex)
                break
            if (FrontCol=="h"):
                break
            valid.append(FrontIndex)
            FrontCol = alphabets[alphabets.index(FrontCol)-1]
            FrontRow = str(int(FrontRow)+1)
            if (FrontRow=="9"):
                break
            Front = Board[FrontRow][FrontCol]
            FrontIndex = FrontCol+FrontRow
        
        #FOR BEHIND RIGHT
        
        BehindCol = alphabets[alphabets.index(start[1])+1]
        BehindRow = str(int(start[0])-1)
        Behind = Board[BehindRow][BehindCol]
        BehindIndex = BehindCol+BehindRow
        while(Behind[0]!="W"):
            if (Behind[0]=="B"):
                valid.append(BehindIndex)
                break
            valid.append(BehindIndex)
            BehindCol = alphabets[alphabets.index(BehindCol)+1]
            BehindRow = str(int(BehindRow)-1)
            if (BehindRow=="0"):
                break
            Behind = Board[BehindRow][BehindCol]
            BehindIndex = BehindCol+BehindRow
        
        #FOR BEHIND LEFT
        
        BehindCol = alphabets[alphabets.index(start[1])-1]
        BehindRow = str(int(start[0])-1)
        Behind = Board[BehindRow][BehindCol]
        BehindIndex = BehindCol+BehindRow
        while(Behind[0]!="W"):
            if (Behind[0]=="B"):
                valid.append(BehindIndex)
                break
            valid.append(BehindIndex)
            BehindCol = alphabets[alphabets.index(BehindCol)-1]
            BehindRow = str(int(BehindRow)-1)
            if (BehindRow=="0"):
                break
            Behind = Board[BehindRow][BehindCol]
            BehindIndex = BehindCol+BehindRow
        
        FrontCol = start[1]
        FrontRow = str(int(start[0])+1)
        Front = Board[FrontRow][FrontCol]
        FrontIndex = FrontCol+FrontRow
        while(Front[0]!="W"):
            if (Front[0]=="B"):
                valid.append(FrontIndex)
                break
            valid.append(FrontIndex)
            FrontRow = str(int(FrontRow)+1)
            if (FrontRow=="9"):
                break
            Front = Board[FrontRow][FrontCol]
            FrontIndex = FrontCol+FrontRow
            
            
        BehindCol = start[1]
        BehindRow = str(int(start[0])-1)
        Behind = Board[BehindRow][BehindCol]
        BehindIndex = BehindCol+BehindRow
        while(Behind[0]!="W"):
            if (Behind[0]=="B"):
                valid.append(BehindIndex)
                break
            valid.append(BehindIndex)
            BehindRow = str(int(BehindRow)-1)
            if (BehindRow=="0"):
                break
            Behind = Board[BehindRow][BehindCol]
            BehindIndex = BehindCol+BehindRow
            
            
        LeftCol = alphabets[alphabets.index(start[1])-1]
        LeftRow = start[0]
        Left = Board[LeftRow][LeftCol]
        LeftIndex = LeftCol+LeftRow
        while(Left[0]!="W"):
            if (Left[0]=="B"):
                valid.append(LeftIndex)
                break
            valid.append(LeftIndex)
            if LeftCol=="a":
                break
            LeftCol = alphabets[alphabets.index(LeftCol)-1]
            Left = Board[LeftRow][LeftCol]
            LeftIndex = LeftCol+LeftRow
            
            
        RightCol = alphabets[alphabets.index(start[1])+1]
        RightRow = start[0]
        Right = Board[RightRow][RightCol]
        RightIndex = RightCol+RightRow
        while(Right[0]!="W"):
            if (Right[0]=="B"):
                valid.append(RightIndex)
                break
            valid.append(RightIndex)
            if RightCol=="h":
                break
            RightCol = alphabets[alphabets.index(RightCol)+1]
            Right = Board[RightRow][RightCol]
            RightIndex = RightCol+RightRow
    os.system('clear')
    printValidBoard(valid)
    return valid

os.system("clear")
print("\n")
Board = {}

alphabets = ['a','b','c','d','e','f','g','h']
numbers = ['1','2','3','4','5','6','7','8']

for i in range(8):
    row = {}
    for j in range(8):
        if (i==1):
            row[alphabets[j]]="W-Pawn"
        elif (i==6):
            row[alphabets[j]]="B-Pawn"
        elif(i==0):
            if(j==0 or j==7):
                row[alphabets[j]]="W-Rook"
            elif(j==1 or j==6):
                row[alphabets[j]]="W-Horse"
            elif(j==2 or j==5):
                row[alphabets[j]]="W-Bishop"
            elif(j==3):
                row[alphabets[j]]="W-Queen"
            else:
                row[alphabets[j]]="W-King"
        elif(i==7):
            if(j==0 or j==7):
                row[alphabets[j]]="B-Rook"
            elif(j==1 or j==6):
                row[alphabets[j]]="B-Horse"
            elif(j==2 or j==5):
                row[alphabets[j]]="B-Bishop"
            elif(j==3):
                row[alphabets[j]]="B-Queen"
            else:
                row[alphabets[j]]="B-King"
        else:
            row[alphabets[j]]="."
    Board[numbers[i]] = row

printBoard()

toPlay=["Random"]
BlackTurn = False
while(toPlay[0]!="bas"):
    toPlay=[]
    if BlackTurn : print("Turn of Black, ",end="")
    else : print("Turn of White, ",end="")
    toPlay = input("What to do ? : ").split(" ")
    #print(toPlay)
    try :
        if toPlay[0]=="show":
            showValid(toPlay[2],BlackTurn)
            continue
        os.system("clear")
        while(not move(toPlay[0],toPlay[1],BlackTurn)):
            printBoard()
            print("Invalid Move pls don't waste our time")
            toPlay = input("What to do ? : ").split(" ")
            os.system("clear")
        BlackTurn = not BlackTurn
    except :
        os.system("clear")
        printBoard()
        print("Invalid Move pls don't waste our time")
