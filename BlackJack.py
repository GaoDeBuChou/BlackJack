import os
import random
NewPoker = range(1,53) #初始牌
chips = 100
win = 0
push = 0
lose = 0
print("您的初始筹码为100，",end = "")
while chips > 0:
    Poker = random.sample(NewPoker,52) #洗牌
    PokerToView = list()
    for i in range(52):
        Poker[i] %= 13
        if Poker[i] == 1:
            PokerToView.append("A")
        elif Poker[i] == 11:
            Poker[i] = 10
            PokerToView.append("J")
        elif Poker[i] == 12:
            Poker[i] = 10
            PokerToView.append("Q")
        elif Poker[i] == 0:
            Poker[i] = 10
            PokerToView.append("K")
        else:
            PokerToView.append(str(Poker[i]))
    while True:
        try:
            bet = int(input("请输入下注数额(输入0退出游戏)，按回车键结束："))
            if bet >= 0:
                if bet <= chips:
                    break
                else:
                    print("下注额不能超过筹码数！")
            else:
                print("请输入有效整数！")
        except:
            print("请输入有效整数！")
    if bet == 0:
        break
    i = os.system("cls")
    chips -= bet
    print("祝您好运，当前剩余筹码：" + str(chips) + "\n")
    print("您的初始牌为" + PokerToView[3] + "、" + PokerToView[4] + "；庄家的明牌为" + PokerToView[1] + "\n") #%庄家明牌为1、暗牌为2，玩家牌为3、4
    if Poker[1] == 1 and chips >= round(bet/2): #%庄家明牌为A
        a = input("请输入买保险(1或a)/不买保险(其它字符)，按回车键结束：")
        if a == "1" or a == "a": #玩家买保险
            chips -= round(bet/2);
            print("当前剩余筹码：" + str(chips) + "\n")
            if Poker[2] == 10: #庄家暗牌为10
                chips += (bet+round(bet/2))
                print("庄家暗牌为" + PokerToView[2] + "，恭喜您赢得保险，剩余筹码：" + str(chips))
                push += 1
                print("当前赢" + str(win) + "局、平" + str(push) + "局、输" + str(lose) + "局\n")
            else: #庄家暗牌非10
                print("庄家暗牌不为10或花牌，很遗憾您输掉保险，游戏继续")
    if not (Poker[1] == 1 and Poker[2] == 10 and a==1): #玩家买保险且赢除外的情况
        if (Poker[3] == 1 and Poker[4] == 10) or (Poker[3] == 10 and Poker[4] == 1): #玩家黑杰克
            if (Poker[1] == 1 and Poker[2] == 10) or (Poker[1] == 10 and Poker[2] == 1): #庄家黑杰克
                chips += bet
                print("庄家暗牌为" + PokerToView[2] + "，您与庄家打平，剩余筹码："+ str(chips))
                push += 1
                print("当前赢" + str(win) + "局、平" + str(push) + "局、输" + str(lose) + "局\n")
            else: #庄家非黑杰克
                chips += round(bet*2.5)
                print("庄家暗牌为" + PokerToView[2] + "，恭喜您获得Blackjack，剩余筹码：" + str(chips))
                win += 1
                print("当前赢" + str(win) + "局、平" + str(push) + "局、输" + str(lose) + "局\n")
        else:
            if Poker[3] == Poker[4] and chips >= bet: #玩家可分牌
                b = input("您的初始牌点数相等，请输入分牌(1或a)/不分牌(其它字符)，按回车键结束：")
                if b == "1" or b == "a": #玩家分牌
                    chips -= bet
                    print("祝您好运，当前剩余筹码：" + str(chips) + "\n")
                    print("您第一组牌的第2张牌为" + PokerToView[5] + "，",end = "")
                    playerSum1 = Poker[3] + Poker[5]
                    n1 = 7
                    while playerSum1 < 21:
                        c1 = input("请输入要牌(1或a)/停牌(其它字符)，按回车键结束：")
                        if c1 == "1" or c1 == "a": #玩家第一组要牌
                            x1 = n1 - 4
                            playerSum1 += Poker[n1]
                            print("您第一组牌的第" + str(x1) + "张牌为" + PokerToView[n1] + "，", end = "")
                            n1 += 1
                        else: #玩家第一组停牌
                            break
                    if playerSum1 > 21: #玩家爆牌
                        print("您第一组牌的点数为" + str(playerSum1) + "，很遗憾您第一组牌爆牌，剩余筹码：" + str(chips))
                        lose += 1
                        print("当前赢" + str(win) + "局、平" + str(push) + "局、输" + str(lose) + "局\n")
                    else: #玩家不爆牌
                        if n1 == 7: #玩家直接停牌
                            if (Poker[3] == 1 or Poker[5] == 1) and playerSum1 + 10 <= 21: #玩家有牌为A且硬牌不爆
                                playerSum1 += 10
                        else: #玩家要牌
                            for m1 in range(7,n1):
                                if (Poker[3] == 1 or Poker[5] == 1 or Poker[m1] == 1) and playerSum1 + 10 <=21: #玩家有牌为A且硬牌不爆
                                    playerSum1 += 10
                        print("您第一组牌的点数为" + str(playerSum1) + "\n")
                    print("您第二组牌的第2张牌为" + PokerToView[6] + "，",end = "")
                    playerSum2 = Poker[4] + Poker[6]
                    n2 = n1
                    while playerSum2 < 21:
                        c2 = input("请输入要牌(1或a)/停牌(其它字符)，按回车键结束：")
                        if c2 == "1" or c2 == "a": #玩家第二组要牌
                            x2 = n2 - n1 + 3
                            playerSum2 += Poker[n2]
                            print("您第二组牌的第" + str(x2) + "张牌为" + PokerToView[n2] + "，",end = "")
                            n2 += 1
                        else: #玩家第二组停牌
                            break
                    if playerSum2 > 21: #玩家爆牌
                        print("您第二组牌的点数为" + str(playerSum2) + "，很遗憾您第二组牌爆牌，剩余筹码：" + str(chips))
                        lose += 1
                        print("当前赢" + str(win) + "局、平" + str(push) + "局、输" + str(lose) + "局\n")
                    else: #玩家不爆牌
                        if n2 == n1: #玩家直接停牌
                            if (Poker[4] == 1 or Poker[6] == 1) and playerSum2 + 10 <= 21: #玩家有牌为A且硬牌不爆
                                playerSum2 += 10
                        else: #玩家要牌
                            for m2 in range(n1,n2):
                                if (Poker[4] == 1 or Poker[6] == 1 or Poker[m2] == 1) and playerSum2 + 10 <=21: #玩家有牌为A且硬牌不爆
                                    playerSum2 += 10
                        print("您第二组牌的点数为" + str(playerSum2) + "\n")
                    if not (playerSum1 > 21 and playerSum2 > 21): #玩家两组全爆牌除外
                        print("庄家暗牌为" + PokerToView[2] + "\n")
                        dealerSum = Poker[1] + Poker[2]
                        nd = n2
                        while dealerSum <= 21:
                            if nd == n2: #庄家要牌前
                                if (Poker[1] == 1 or Poker[2] == 1) and dealerSum + 10 <= 21 and dealerSum + 10 >= 17: #庄家有牌为A且硬牌17不爆
                                    dealerSum += 10
                                    break
                            else: #庄家要牌后
                                for md in range(n2,nd):
                                    if (Poker[1] == 1 or Poker[2] == 1 or Poker[md] == 1) and dealerSum + 10 <= 21 and dealerSum + 10 >= 17: #庄家有牌为A且硬牌17不爆
                                        dealerSum += 10
                                        break
                            if dealerSum < 17: #庄家点数小于17
                                xd = nd - n2 + 3
                                dealerSum += Poker[nd]
                                print("庄家选择要牌，第" + str(xd) + "张牌为" + PokerToView[nd])
                                nd += 1
                            else: #庄家点数大于等于17
                                break
                        if dealerSum > 21: #庄家爆牌
                            if playerSum1 <= 21: #玩家第一组牌不爆
                                chips += bet*2
                                print("庄家点数为" + str(dealerSum) + "，庄家爆牌，恭喜您第一组牌赢了")
                                win += 1
                            if playerSum2 <= 21: #玩家第二组牌不爆
                                chips += bet*2
                                print("庄家点数为" + str(dealerSum) + "，庄家爆牌，恭喜您第二组牌赢了")
                                win += 1
                            print("剩余筹码：" + str(chips))
                            print("当前赢" + str(win) + "局、平" + str(push) + "局、输" + str(lose) + "局\n")
                        else: #庄家不爆牌
                            if playerSum1 < dealerSum: #玩家第一组牌小于庄家
                                print("庄家选择停牌，点数为" + str(dealerSum) + "，很遗憾您第一组牌输了")
                                lose += 1
                            elif playerSum1 == dealerSum: #玩家第一组牌等于庄家
                                print("庄家选择停牌，点数为" + str(dealerSum) + "，您第一组牌与庄家打平")
                                chips += bet
                                push += 1
                            elif playerSum1 > dealerSum and playerSum1 <= 21: #玩家第一组牌大于庄家且不爆
                                print("庄家选择停牌，点数为" + str(dealerSum) + "，恭喜您第一组牌赢了")
                                chips += bet*2
                                win += 1
                            if playerSum2 < dealerSum: #玩家第二组牌小于庄家
                                print("庄家选择停牌，点数为" + str(dealerSum) + "，很遗憾您第二组牌输了")
                                lose += 1
                            elif playerSum2 == dealerSum: #玩家第二组牌等于庄家
                                print("庄家选择停牌，点数为" + str(dealerSum) + "，您第二组牌与庄家打平")
                                chips += bet
                                push += 1
                            elif playerSum2 > dealerSum and playerSum2 <= 21: #玩家第二组牌大于庄家且不爆
                                print("庄家选择停牌，点数为" + str(dealerSum) + "，恭喜您第二组牌赢了")
                                chips += bet*2
                                win += 1
                            print("剩余筹码：" + str(chips))
                            print("当前赢" + str(win) + "局、平" + str(push) + "局、输" + str(lose) + "局\n")
            if Poker[3] != Poker[4] or (Poker[3] == Poker[4] and b != "1"): #玩家不可分牌或玩家不分牌
                playerSum = Poker[3] + Poker[4]
                n = 5
                while playerSum < 21:
                    c = input("请输入要牌(1或a)/停牌(其它字符)，按回车键结束：")
                    if c == "1" or c == "a": #玩家要牌
                        x = n - 2
                        playerSum += Poker[n]
                        print("您的第" + str(x) + "张牌为" + PokerToView[n] + "，",end = "")
                        n += 1
                    else: #玩家停牌
                        break
                if playerSum > 21: #玩家爆牌
                    print("您的点数为" + str(playerSum) + "，很遗憾您爆牌了，剩余筹码：" + str(chips))
                    lose += 1
                    print("当前赢" + str(win) + "局、平" + str(push) + "局、输" + str(lose) + "局\n")
                else: #玩家不爆牌
                    if n == 5: #玩家直接停牌
                        if (Poker[3] == 1 or Poker[4] == 1) and playerSum + 10 <= 21: #玩家有牌为A且硬牌不爆
                            playerSum += 10
                    else: #玩家要牌
                        for m in range(5,n):
                            if (Poker[3] == 1 or Poker[4] == 1 or Poker[m] == 1) and playerSum + 10 <= 21: #玩家有牌为A且硬牌不爆
                                playerSum += 10
                    print("您的点数为" + str(playerSum) + "\n")
                    print("庄家暗牌为" + PokerToView[2] + "\n")
                    dealerSum = Poker[1] + Poker[2]
                    nd = n
                    while dealerSum <= 21:
                        if nd == n: #庄家要牌前
                            if (Poker[1]==1 or Poker[2] == 1) and dealerSum + 10 <= 21 and dealerSum + 10 >= 17: #庄家有牌为A且硬牌17不爆
                                dealerSum += 10
                                break
                        else: #庄家要牌后
                            for md in range(n,nd):
                                if (Poker[1] == 1 or Poker[2] == 1 or Poker[md] == 1) and dealerSum + 10 <= 21 and dealerSum + 10 >= 17: #庄家有牌为A且硬牌17不爆
                                    dealerSum += 10
                                    break
                        if dealerSum < 17: #庄家点数小于17
                            xd = nd - n + 3
                            dealerSum += Poker[nd]
                            print("庄家选择要牌，第" + str(xd) + "张牌为" + PokerToView[nd])
                            nd += 1
                        else: #庄家点数大于等于17
                            break
                    if dealerSum > 21: #庄家爆牌
                        chips += bet*2
                        print("庄家点数为" + str(dealerSum) + "，庄家爆牌，恭喜您赢了，剩余筹码：" + str(chips))
                        win += 1
                        print("当前赢" + str(win) + "局、平" + str(push) + "局、输" + str(lose) + "局\n")
                    else: #庄家不爆牌
                        if playerSum < dealerSum: #玩家小于庄家
                            print("庄家选择停牌，点数为" + str(dealerSum) + "，很遗憾您输了，",end = "")
                            lose += 1
                        elif playerSum == dealerSum: #玩家等于庄家
                            print("庄家选择停牌，点数为" + str(dealerSum) + "，您与庄家打平，",end = "")
                            chips += bet
                            push += 1
                        elif playerSum > dealerSum and playerSum <= 21: #玩家大于庄家且不爆
                            print("庄家选择停牌，点数为" + str(dealerSum) + "，恭喜您赢了，",end = "")
                            chips += bet*2
                            win += 1
                        print("剩余筹码：" + str(chips))
                        print("当前赢" + str(win) + "局、平" + str(push) + "局、输" + str(lose) + "局\n")
else:
    print("剩余筹码不足！")
print("游戏结束，重新开始请重新运行此程序！")
