class Computer:  # 問題を出すコンピュータのクラス（設計図）
    def randomNumber(self):
        print("----------\nWelcome to Hit and Blow game.")
        print("You will guess 3 secret numbers generated randomly by computer.")
        print("There are many chances until you made a guess.")
        print("The rule is described as below:")
        print("1. When the both numbers match at the same digit, count and show as Blow:'n'.")
        print("2. When the both numbers match but not at the same digit, cound and show as Hit:'n'.")
        print("3. You can exit this game by entering 'END()'.")
        print("The game will start soon... Relax and enjoy it!!\n----------\n")

        import random
        ranNum = []
        for i in range(0, 3):
            ranNum.append(random.randint(0, 9))
        return ranNum

class User:  # 問題を解答するユーザーのクラス（設計図）
    def answer(self):
        import sys
        while True:
            userNum = []
            userIn = input("Enter 3 numbers: ")
            if userIn == 'END()':
                print("You have entered 'END()' Exiting the game...\n")
                sys.exit()
            userNum = list(map(int, userIn))
            if len(userNum) == 3:
                return userNum
                break
            print("IndexError：Please enter only 3 index of numbers\n")

class Result:  # 結果を表示するクラス（設計図）
    def __init__(self, ranNum, userNum):
        self.ranNum = ranNum
        self.userNum = userNum

    def compare(self):
        hit = 0
        blow = 0
        for i in range(3):
            if ranNum[i] == userNum[i]:
                hit += 1
                continue
            for j in range(3):
                if ranNum[i] == userNum[j]:
                        blow += 1             

        print('-----\nHit:', hit)
        print('Blow:', blow, '\n')
        return hit

# インスタンス生成（クラスの実体を生成）
computer = Computer()
ranNum = computer.randomNumber()

# 本文
while True:
    try:
        user = User()
        userNum = user.answer()

        result = Result(ranNum, userNum)
        hit = result.compare()

        if hit == 3:
            print('Congrats!! You got 3 hits as: ', ranNum)
            break

    except ValueError:
        print("ValueError：Please enter only numbers as integer\n")
    except IndexError:
        print("IndexError：Please enter only 3 index of numbers\n")
