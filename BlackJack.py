import os
import random
import time


def shuffle(new_poker):
    poker = random.sample(new_poker, 52)
    poker_to_view = list()
    for card in range(52):
        poker[card] %= 13
        if poker[card] == 1:
            poker_to_view.append("A")
        elif poker[card] == 11:
            poker[card] = 10
            poker_to_view.append("J")
        elif poker[card] == 12:
            poker[card] = 10
            poker_to_view.append("Q")
        elif poker[card] == 0:
            poker[card] = 10
            poker_to_view.append("K")
        else:
            poker_to_view.append(str(poker[card]))
    return poker, poker_to_view


def deal(poker, poker_to_view, i, x, person):
    if x < len(person):
        person[x] = poker[i]
    else:
        person.append(poker[i])
    if person[0] == "庄家":
        print("庄家选择要牌，第" + str(x) + "张牌为" + poker_to_view[i])
    else:
        print(person[0] + "的第" + str(x) + "张牌为" + poker_to_view[i] + "，", end="")


def calc(person):
    points = 0
    for i in range(1, len(person)):
        points += person[i]
    if 1 in person and points <= 11:
        points += 10
    return points


def play(poker, poker_to_view, i, person):
    x = 3
    while calc(person) < 21:
        c = input("请输入要牌(1或a)/停牌(其它字符)，按回车键结束：")
        if c == "1" or c == "a":  # 要牌
            deal(poker, poker_to_view, i, x, person)
            i += 1
            x += 1
        else:
            break
    return calc(person), i


def dealer(poker, poker_to_view, i, person):
    x = 3
    while calc(person) < 17:
        now = time.time()
        while time.time() < now + 1:
            pass
        deal(poker, poker_to_view, i, x, person)
        i += 1
        x += 1
    return calc(person)


def compare(player, player_sum, dealer_sum, wpl, cps, bt):
    if player_sum <= 21 < dealer_sum:  # 玩家不爆庄家爆
        cps += bt * 2
        print("庄家点数为" + str(dealer_sum) + "，庄家爆牌，恭喜" + player + "赢了")
        wpl[0] += 1
    elif player_sum < dealer_sum <= 21:  # 玩家小于庄家
        print("庄家选择停牌，点数为" + str(dealer_sum) + "，很遗憾" + player + "输了")
        wpl[2] += 1
    elif player_sum == dealer_sum <= 21:  # 玩家等于庄家
        cps += bt
        print("庄家选择停牌，点数为" + str(dealer_sum) + "，" + player + "与庄家打平")
        wpl[1] += 1
    elif dealer_sum < player_sum <= 21:  # 玩家大于庄家且不爆
        cps += bt * 2
        print("庄家选择停牌，点数为" + str(dealerSum) + "，恭喜" + player + "赢了")
        wpl[0] += 1
    return cps


def print_wpl(wpl, n):
    if n > -1:
        wpl[n] += 1
    print("当前赢" + str(wpl[0]) + "局、平" + str(wpl[1]) + "局、输" + str(wpl[2]) + "局\n")


NewPoker = range(1, 53)  # 初始牌
chips = 100
WPL = [0, 0, 0]
print("您的初始筹码为100，", end="")
while chips > 0:
    Poker, PokerToView = shuffle(NewPoker)  # 洗牌
    while True:
        try:
            bet = int(input("请输入下注数额(输入0退出游戏)，按回车键结束："))
            if bet >= 0:
                if bet <= chips:
                    break
                else:
                    print("下注额不能超过筹码数！")
            else:
                print("请输入有效正整数！")
        except ValueError:
            print("请输入有效正整数！")
    if bet == 0:
        break
    clear = os.system("cls")
    chips -= bet
    print("祝您好运，当前剩余筹码：" + str(chips) + "\n")
    person1 = ["庄家", Poker[0], Poker[1]]
    person2 = ["您", Poker[2], Poker[3]]
    print("您的初始牌为" + PokerToView[2] + "、" + PokerToView[3] + "；庄家的明牌为" + PokerToView[0] + "\n")  # 庄家明牌为0、暗牌为1，玩家牌为2、3
    if (person2[1] == 1 and person2[2] == 10) or (person2[1] == 10 and person2[2] == 1):  # 玩家黑杰克
        if (person1[1] == 1 and person1[2] == 10) or (person1[1] == 10 and person1[2] == 1):  # 庄家黑杰克
            chips += bet
            print("庄家暗牌为" + PokerToView[1] + "，您与庄家打平，剩余筹码：" + str(chips))
            print_wpl(WPL, 1)
        else:  # 庄家非黑杰克
            chips += round(bet * 2.5)
            print("庄家暗牌为" + PokerToView[1] + "，恭喜您获得Blackjack，剩余筹码：" + str(chips))
            print_wpl(WPL, 0)
    else:
        a = 0
        if person1[1] == 1 and chips >= round(bet / 2):  # 庄家明牌为A
            a = input("请输入买保险(1或a)/不买保险(其它字符)，按回车键结束：")
            if a == "1" or a == "a":  # 玩家买保险
                chips -= round(bet / 2)
                print("当前剩余筹码：" + str(chips) + "\n")
                if person1[2] == 10:  # 庄家暗牌为10
                    chips += (bet + round(bet / 2))
                    print("庄家暗牌为" + PokerToView[1] + "，恭喜您赢得保险，剩余筹码：" + str(chips))
                    print_wpl(WPL, 1)
                else:  # 庄家暗牌非10
                    print("庄家暗牌不为10或JQK，很遗憾您输掉保险，游戏继续")
        if not (person1[1] == 1 and person1[2] == 10 and (a == "1" or a == "a")):  # 玩家买保险且赢除外的情况
            index = 4
            b = 0
            if person2[1] == person2[2] and chips >= bet:  # 玩家可分牌
                b = input("您的初始牌点数相等，请输入分牌(1或a)/不分牌(其它字符)，按回车键结束：")
                if b == "1" or b == "a":  # 玩家分牌
                    chips -= bet
                    print("祝您好运，当前剩余筹码：" + str(chips) + "\n")
                    person2[0] = "您第一组牌"
                    person3 = ["您第二组牌", Poker[3], Poker[5]]
                    deal(Poker, PokerToView, index, 2, person2)
                    index += 2
                    playerSum1, index = play(Poker, PokerToView, index, person2)
                    if playerSum1 > 21:  # 玩家爆牌
                        print("您第一组牌的点数为" + str(playerSum1) + "，很遗憾您第一组牌爆牌，剩余筹码：" + str(chips))
                        print_wpl(WPL, 2)
                    else:  # 玩家不爆牌
                        print("您第一组牌的点数为" + str(playerSum1) + "\n")
                    print("您第二组牌的第2张牌为" + PokerToView[5] + "，", end="")
                    playerSum2, index = play(Poker, PokerToView, index, person3)
                    if playerSum2 > 21:  # 玩家爆牌
                        print("您第二组牌的点数为" + str(playerSum2) + "，很遗憾您第二组牌爆牌，剩余筹码：" + str(chips))
                        print_wpl(WPL, 2)
                    else:  # 玩家不爆牌
                        print("您第二组牌的点数为" + str(playerSum2) + "\n")
                    if playerSum1 <= 21 or playerSum2 <= 21:  # 玩家至少一组不爆牌
                        print("庄家暗牌为" + PokerToView[1] + "\n")
                        dealerSum = dealer(Poker, PokerToView, index, person1)
                        chips = compare(person2[0], playerSum1, dealerSum, WPL, chips, bet)
                        chips = compare(person3[0], playerSum2, dealerSum, WPL, chips, bet)
                        print("剩余筹码：" + str(chips))
                        print_wpl(WPL, -1)
            if Poker[2] != Poker[3] or (b != "1" and b != "a"):  # 玩家不可分牌或玩家不分牌
                playerSum, index = play(Poker, PokerToView, index, person2)
                if playerSum > 21:  # 玩家爆牌
                    print("您的点数为" + str(playerSum) + "，很遗憾您爆牌了，剩余筹码：" + str(chips))
                    print_wpl(WPL, 2)
                else:
                    print("您的点数为" + str(playerSum) + "\n")
                    print("庄家暗牌为" + PokerToView[1] + "\n")
                    dealerSum = dealer(Poker, PokerToView, index, person1)
                    chips = compare(person2[0], playerSum, dealerSum, WPL, chips, bet)
                    print("剩余筹码：" + str(chips))
                    print_wpl(WPL, -1)
else:
    print("剩余筹码不足！")
print("游戏结束，重新开始请重新运行此程序！")
