HARD_AILMENTS = [
    'poison',
    'burn',
    'freeze',
    'sleep',
    'paralysis'
]

SOFT_AILMENTS = [
    'nightmare',
    'trap',
    'infatuation',
    'confusion',
    'torment',
    'disable',
    'yawn',
    'heal-block',
    'no-type-immunity',
    'leech-seed',
    'embargo',
    'perish-song',
    'ingrain'
]

STAGE_MODS = {
    -6: 2/8,
    -5: 2/7,
    -4: 2/6,
    -3: 2/5,
    -2: 2/4,
    -1: 2/3,
    0: 2/2,
    1: 3/2,
    2: 4/2,
    3: 5/2,
    4: 6/2,
    5: 7/2,
    6: 8/2
}

CRIT_RATES = {
    0: 1/16,
    1: 1/8,
    2: 1/2,
    3: 1
}

#               N  Ft  Fl  Po  Gd  Rk  Bg  Gh  St  Fr  W   Gs  E   Ps  I   Dr  Da  Fa
TYPE_CHART =  [[1, 1 , 1 , 1 , 1 ,0.5, 1 , 0 ,0.5, 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ],
               [2, 1 ,0.5,0.5, 1 , 2 ,0.5, 0 , 2 , 1 , 1 , 1 , 1 ,0.5, 2 , 1 , 2 ,0.5],
               [1, 2 , 1 , 1 , 1 ,0.5, 2 , 1 ,0.5, 1 , 1 , 2 ,0.5, 1 , 1 , 1 , 1 , 1 ],
               [1, 1 , 1 ,0.5,0.5,0.5, 1 ,0.5, 0 , 1 , 1 , 2 , 1 , 1 , 1 , 1 , 1 , 2 ],
               [1, 1 , 0 , 2 , 1 , 2 ,0.5, 1 , 2 , 2 , 1 ,0.5, 2 , 1 , 1 , 1 , 1 , 1 ],
               [1,0.5, 2 , 1 ,0.5, 1 , 2 , 1 ,0.5, 2 , 1 , 1 , 1 , 1 , 2 , 1 , 1 , 1 ],
               [1,0.5,0.5,0.5, 1 , 1 , 1 ,0.5,0.5,0.5, 1 , 2 , 1 , 2 , 1 , 1 , 2 ,0.5],
               [0, 1 , 1 , 1 , 1 , 1 , 1 , 2 , 1 , 1 , 1 , 1 , 1 , 2 , 1 , 1 ,0.5, 1 ],
               [1, 1 , 1 , 1 , 1 , 2 , 1 , 1 ,0.5,0.5,0.5, 1 ,0.5, 1 , 2 , 1 , 1 , 2 ],
               [1, 1 , 1 , 1 , 1 ,0.5, 2 , 1 , 2 ,0.5,0.5, 2 , 1 , 1 , 2 ,0.5, 1 , 1 ],
               [1, 1 , 1 , 1 , 2 , 2 , 1 , 1 , 1 , 2 ,0.5,0.5, 1 , 1 , 1 ,0.5, 1 , 1 ],
               [1, 1 ,0.5,0.5, 2 , 2 ,0.5, 1 ,0.5,0.5, 2 ,0.5, 1 , 1 , 1 ,0.5, 1 , 1 ],
               [1, 1 , 2 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 2 ,0.5,0.5, 1 , 1 ,0.5, 1 , 1 ],
               [1, 2 , 1 , 2 , 1 , 1 , 1 , 1 ,0.5, 1 , 1 , 1 , 1 ,0.5, 1 , 1 , 0 , 1 ],
               [1, 1 , 2 , 1 , 2 , 1 , 1 , 1 ,0.5,0.5,0.5, 2 , 1 , 1 ,0.5, 2 , 1 , 1 ],
               [1, 1 , 1 , 1 , 1 , 1 , 1 , 1 ,0.5, 1 , 1 , 1 , 1 , 1 , 1 , 2 , 1 , 0 ],
               [1,0.5, 1 , 1 , 1 , 1 , 1 , 2 , 1 , 1 , 1 , 1 , 1 , 2 , 1 , 1 ,0.5,0.5],
               [1, 2 , 1 ,0.5, 1 , 1 , 1 , 1 ,0.5,0.5, 1 , 1 , 1 , 1 , 1 , 2 , 2 , 1 ]]
