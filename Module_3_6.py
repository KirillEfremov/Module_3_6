from itertools import count

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
def summ():
    s = 0
    counter_hello = 0
    counter_ab = 0
    counter_drum_cube = 0
    counter_urban = 0
    counter_urban_2 = 0
    for i in data_structure:
        if isinstance(i, list):
            for j in i:
                s += j
        if isinstance(i, tuple):
            for t in i:
                if isinstance(t, dict):
                    for tt in t.items():
                        for ttt in tt:
                            if isinstance(ttt, str):
                                for dr in ttt:
                                    counter_drum_cube += 1
                            else:
                                s += ttt
                    s += counter_drum_cube
                elif isinstance(t, list):
                    for tl in t:
                        if isinstance(tl, set):
                            for tr in tl:
                                if isinstance(tr, tuple):
                                    for ti in tl:
                                        if isinstance(ti, int):
                                            s += ti
                                        if isinstance(ti, tuple):
                                            for to in ti:
                                                if isinstance(to, int):
                                                    s += to + 1
                                                if isinstance(to, str):
                                                    for u in to:
                                                        counter_urban += 1
                                                if isinstance(to, tuple):
                                                    for p in to:
                                                        if isinstance(p, str):
                                                            for co in p:
                                                                counter_urban_2 += 1
                                                        if isinstance(p, int):
                                                            s += p
                                                    s += counter_urban_2
                                                s += counter_urban
        if isinstance(i, dict):
            for d in i.items():
                for dd in d:
                    if isinstance(dd, str):
                        counter_ab += 1
                    else:
                        s += dd
            s += counter_ab
        if isinstance(i, str):
            for st in i:
                counter_hello += 1
            s += counter_hello
    return s
print(summ())