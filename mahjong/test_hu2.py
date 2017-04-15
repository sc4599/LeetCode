# coding=utf-8

LAI_ZI = 1000
CARD_VAL_RANGE = [[17, 25], [33, 41], [49, 51]]  # 饼, 条, 箭


def ke(ls):
    for i in xrange(1, len(ls)):
        if ls[i] != ls[i - 1]:
            return False
    return True


def sun(ls):
    return ls[0] == ls[1] + 1 == ls[2] + 2


def index_ex(ls, item):
    for i in xrange(len(ls)):
        if ls[i] == item:
            return i
    return -1


def drop(ls, n):
    rst = ls[n:]


def delete(ls, itmes):
    rst = ls[:]
    for i in itmes:
        rst.remove(i)
    return rst


cut = 0


def hu(js, ls):
    global cut
    cut += 1
    jlen = len(js)
    llen = len(ls)
    rst = [[] for _ in xrange(6)]
    if llen == 0:
        return [[js]]
    if jlen + llen == 3:
        if jlen >= 2 or \
                (jlen == 1 and (ke(ls) or abs(ls[0] - ls[1]) <= 2)) or \
                (jlen == 0 and (ke(ls) or sun(ls))):
            return [[js + ls]]
        else:
            return []
    elif jlen + llen > 3:
        s1, s2 = index_ex(ls, ls[0] - 1), index_ex(ls, ls[0] - 2)
        if llen >= 3 and ke(ls[:3]):
            rst[0] = map(lambda x: [ls[:3]] + x, hu(js, ls[3:]))
        if s1 != -1 and s2 != -1:
            tmp = [ls[0], ls[s1], ls[s2]]
            rst[1] = map(lambda x: [tmp] + x, hu(js, delete(ls, tmp)))
        if jlen > 0 and llen >= 2 and ke(ls[:2]):
            tmp = [js[0]] + ls[:2]
            rst[2] = map(lambda x: [tmp] + x, hu(js[1:], ls[2:]))
        if jlen > 0 and s1 != -1:
            tmp = [js[0], ls[0], ls[s1]]
            rst[3] = map(lambda x: [tmp] + x, hu(js[1:], delete(ls, [ls[0], ls[s1]])))
        if jlen > 0 and s2 != -1:
            tmp = [js[0], ls[0], ls[s2]]
            rst[4] = map(lambda x: [tmp] + x, hu(js[1:], delete(ls, [ls[0], ls[s2]])))
        if jlen > 1:
            tmp = [js[0], js[1], ls[0]]
            rst[5] = map(lambda x: [tmp] + x, hu(js[2:], ls[1:]))
        return reduce(lambda x, y: x + y, rst)


def huex(ls):
    rst = []
    # if len(ls) == 14:
    num_len = len(ls)
    if num_len % 3 == 2:
        ls.sort(key=lambda x: -x)
        jiang = []
        tmpset = set()
        # for i in xrange(13):
        #     for j in xrange(i + 1, 14):
        for i in xrange(num_len - 1):
            for j in xrange(i + 1, num_len):
                if ls[i] == ls[j] or ls[i] + ls[j] > LAI_ZI:
                    if ls[i] * LAI_ZI + ls[j] not in tmpset:
                        jiang.append([ls[i], ls[j]])
                        tmpset.add(ls[i] * LAI_ZI + ls[j])
        for it in jiang:
            tmp = delete(ls, it)
            jp = filter(lambda x: x >= LAI_ZI, tmp)
            lp = filter(lambda x: x < LAI_ZI, tmp)
            rst += map(lambda x: [it, x], hu(jp, lp))
        return rst


def get_shun_liang_tou_card(card_1, card_2):
    if card_1 != card_2 + 1:
        return []
    ret = []
    for r in CARD_VAL_RANGE:
        if card_1 + 1 <= r[1] and card_1 + 1 >= r[0]:
            ret.append(card_1 + 1)
            break
    for r in CARD_VAL_RANGE:
        if card_2 - 1 <= r[1] and card_2 - 1 >= r[0]:
            ret.append(card_2 - 1)
            break
    return ret


def get_lai_zi_card(card_list):
    '''从胡牌中获取用癞子替代的牌'''
    jiang_cards = card_list[0]
    ting_cards = []
    if LAI_ZI < jiang_cards[0] + jiang_cards[1]:
        ting_cards.append(jiang_cards[0] + jiang_cards[1] - LAI_ZI)
    for cards in card_list[1]:
        if 3 == len(cards) and LAI_ZI == cards[0]:
            if cards[1] == cards[2] + 1:
                ting_cards.extend(get_shun_liang_tou_card(cards[1], cards[2]))
            elif cards[1] == cards[2] + 2:
                ting_cards.append(cards[1] - 1)
            elif cards[1] == cards[2]:
                ting_cards.append(cards[1])
    return list(set(ting_cards))


if __name__ == '__main__':
    print '11111111111111111111111111111111111111111111111111111111111'

    '''
    #tt = profile.runcall("huex([LAI_ZI, 43, 43, 42, 42, 41, 41, 26, 26, 5, 4, 3, 3, 3])", "timeit")

    #pro = cProfile.Profile()
    #tt = pro.runcall(huex, [LAI_ZI, 43, 43, 42, 42, 41, 41, 26, 26, 5, 4, 3, 3, 3], "timeit")
    #print 'cProfile', tt

    p = pstats.Stats('timeit')
    p.sort_stats('time')
    p.print_stats(10)
    '''

    import time

    # t = time.time()
    # for i in range(LAI_ZI):
    #     tmp = huex([LAI_ZI, LAI_ZI, 47, 47, 29, 29, 29, 25, 24, 23, 7, 7, 5, 5])
    # print '%.6f' % ((time.time() - t) / LAI_ZI.0)
    # for x in tmp:
    #     print x
    #
    # t = time.time()
    # for i in range(LAI_ZI):
    #     tmp = huex([LAI_ZI, 43, 43, 42, 42, 41, 41, 26, 26, 5, 4, 3, 3, 3])
    # print '%.6f' % ((time.time() - t) / LAI_ZI.0)
    # for x in tmp:
    #     print x

    t = time.time()
    for i in range(LAI_ZI):
        # tmp = huex([LAI_ZI, LAI_ZI, 81, 81, 47, 46, 26, 25, 7, 6, 5, 4, 4, 4])
        tmp = huex([LAI_ZI, 6, 47, 47, 29, 29, 29, 25, 24, 23, 7, 7, 5, 5])
        # print "tmp=", tmp
    print '%.6f' % ((time.time() - t) / 1000.0)
    for x in tmp:
        print "x=", x, get_lai_zi_card(x)

        # print cut / LAI_ZI
