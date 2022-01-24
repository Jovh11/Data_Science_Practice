#!/usr/bin/env python
# coding: utf-8

# ## Import Statements and Json Interpretation

# In[1]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import os
import json


# In[2]:


from sqlalchemy import create_engine


# In[3]:


path_to_json = 'filepath here'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]


# In[4]:


def extract_neow(all_text):
    victory = None
    neow_bonus = None
    character = None
    dict_list = []
    for key in all_text:
        val = key
        event = val['event']
        victory = event.get('victory', 'NONE')
        neow_bonus = event.get('neow_bonus', 'NONE')
        character = event.get('character_chosen', 'NONE')
        neow_dict = {'character': character, 'victory': victory, 'neow_boon':neow_bonus}
        dict_list.append(neow_dict)
    i = 0
    return dict_list


# In[ ]:


i = 0
engine = create_engine('postgresql://postgres:password@localhost:5432/database name')
for index, js in enumerate(json_files):
    with open(os.path.join(path_to_json, js)) as json_file:
        json_text = json.load(json_file)
        length = len(json_text)
        dict_info = (extract_neow(json_text))
        test = dict_info
        neow_info = pd.DataFrame(test)    
        neow_info.to_sql('table name', engine, if_exists='append')
        i += 1
        print(i)


# ## Processing Data Collected From Database For all Runs

# In[ ]:


total_count = 68693221
win_count = 5999021
lose_count = 62694200


# In[ ]:


all_dict = {'Boss Relic': 6354652, '100 Gold': 2968019, 'One Rare Card': 3294992, 'One Rare Relic': 4172699, 'Random Uncommon Colorless Card': 1907016, 'Random Rare Colorless Card': 1402416, 'Random Common Relic': 5835906, 'Remove One Card': 1176368, 'Remove Two Cards': 1172289, 'Ten Percent HP Bonus': 5846402, 'Three Cards': 2174342, 'Next 3 Enemies have 1 HP': 19495582, 'Three Rare Cards': 2710034, 'Obtain 3 Potions': 893076, 'Transform a Card': 1485163, 'Transform Two Cards': 1488704, 'Twenty Percent HP Bonus': 974500, '250 Gold': 2002021, 'Upgrade a Card': 1980401, 'None': 1358639}


# In[ ]:


all_adjusted = {}
keys = all_dict.keys()
for x in keys:
    new = all_dict[x]
    val = (new/total_count) * 100
    all_adjusted[x] = val


# In[ ]:


winner_vals = [555564, 287542, 274803, 444214, 134641, 101482, 632240, 130275, 139109, 500029, 170226, 1450125, 220269, 76814, 143973, 153316, 104090, 223212, 202914, 54183]
winner_dict = {}
i = 0
for x in keys:
    num = winner_vals[i]
    i += 1
    val = (num/win_count) * 100
    winner_dict[x] = val


# In[ ]:


loser_vals = [5799088, 2680477, 3020189, 3728485, 1772375, 1300934, 5203666, 1046093, 1033180, 5346373, 2004116, 18045457, 2489765, 816262, 1341190, 1335388, 870410, 1778809, 1777487, 1304456]
loser_dict = {}
i = 0
for x in keys:
    num = loser_vals[i]
    i += 1
    val = (num/lose_count) * 100
    loser_dict[x] = val


# In[ ]:


all_vals = all_adjusted.values()
win_vals = winner_dict.values()
lose_vals = loser_dict.values()
win_diff_vals = []
lose_diff_vals = []
for x in keys:
    num = all_adjusted[x]
    win = winner_dict[x]
    lose = loser_dict[x]
    win_pct = win - num
    lose_pct = lose - num
    win_diff_vals.append(win_pct)
    lose_diff_vals.append(lose_pct)


# In[ ]:


colors = ['b', 'g', 'r', 'm']


# In[ ]:


fig, ax= plt.subplots(figsize = [12,12])
plt.bar(keys, all_vals, color = colors)
ax.figure.autofmt_xdate()
plt.ylabel('Pct Boon Chosen', fontsize = 15)
plt.xlabel('Chosen Boon', fontsize = 15)
plt.title('Percentage a Neow Boon is Chosen')
plt.show()


# In[ ]:


fig, ax= plt.subplots(figsize = [12,12])
plt.bar(keys, win_diff_vals, color = colors)
ax.figure.autofmt_xdate()
plt.ylabel('Pct Boon Chosen', fontsize = 15)
plt.xlabel('Chosen Boon', fontsize = 15)
plt.title('Pct Diff a Winner Chooses a Boon')
plt.show()


# In[ ]:


fig, ax= plt.subplots(figsize = [12,12])
plt.bar(keys, lose_diff_vals, color = colors)
ax.figure.autofmt_xdate()
plt.ylabel('Pct Boon Chosen', fontsize = 15)
plt.xlabel('Chosen Boon', fontsize = 15)
plt.title('Pct Diff a Loser Chooses a Boon')
plt.show()


# ## Processing Ironclad Data

# In[ ]:


ic_total = 26212859
ic_win_total = 2327590
ic_lose_total = 23885269


# In[ ]:


ic_vals = [1646703, 1205614, 1342417, 1741499, 790239, 608196, 2343597, 515346, 529947, 2073732, 898361, 6824737, 1172115, 365728, 622154, 646457, 471982, 853872, 714650, 845513]
ic_dict = {}
i = 0
for x in keys:
    num = ic_vals[i]
    i += 1
    val = (num/ic_total) * 100
    ic_dict[x] = val


# In[ ]:


ic_win_vals = [138979, 117570, 116339, 195477, 56769, 44422, 260097, 56150, 62992, 183518, 69190, 505274, 103315, 31978, 58870, 65599, 52671, 95498, 69007, 43875]
ic_win_dict = {}
i = 0
for x in keys:
    num = ic_win_vals[i]
    i += 1
    val = (num/ic_win_total) * 100
    ic_win_dict[x] = val


# In[ ]:


ic_lose_vals = [1507724, 1088044, 1226078, 1546022, 733470, 563774, 2083500, 459196, 466955, 1890214, 829171, 6319463, 1068800, 333750, 563284, 580858, 419311, 758374, 645643, 801638]
ic_lose_dict = {}
i = 0
for x in keys:
    num = ic_lose_vals[i]
    i += 1
    val = (num/ic_lose_total) * 100
    ic_lose_dict[x] = val


# In[ ]:


ic_all_vals = ic_dict.values()
ic_win_vals = ic_win_dict.values()
ic_lose_vals = ic_lose_dict.values()
ic_win_diff_vals = []
ic_lose_diff_vals = []
for x in keys:
    num = ic_dict[x]
    win = ic_win_dict[x]
    lose = ic_lose_dict[x]
    win_pct = win - num
    lose_pct = lose - num
    ic_win_diff_vals.append(win_pct)
    ic_lose_diff_vals.append(lose_pct)


# In[ ]:


fig, ax= plt.subplots(figsize = [12,12])
plt.bar(keys, all_vals, color = 'red')
ax.figure.autofmt_xdate()
plt.ylabel('Pct Boon Chosen', fontsize = 15)
plt.xlabel('Chosen Boon', fontsize = 15)
plt.title('Percentage a Neow Boon is Chosen For Ironclad')
plt.show()


# In[ ]:


fig, ax= plt.subplots(figsize = [12,12])
plt.bar(keys, win_diff_vals, color = 'red')
ax.figure.autofmt_xdate()
plt.ylabel('Pct Boon Chosen', fontsize = 15)
plt.xlabel('Chosen Boon', fontsize = 15)
plt.title('Pct Diff a Winning Ironclad Chooses a Boon')
plt.show()


# In[ ]:


fig, ax= plt.subplots(figsize = [12,12])
plt.bar(keys, lose_diff_vals, color = 'red')
ax.figure.autofmt_xdate()
plt.ylabel('Pct Boon Chosen', fontsize = 15)
plt.xlabel('Chosen Boon', fontsize = 15)
plt.title('Pct Diff a Losing Ironclad Chooses a Boon')
plt.show()


# ## Processing Silent Data

# In[ ]:


si_total = 20712606
si_win_total = 1784480
si_lose_total = 18928126


# In[ ]:


si_vals = [2814065, 823097, 881533, 1130195, 518539, 357947, 1655120, 292401, 284819, 1835016, 582441, 6331697, 682053, 250002, 380906, 368968, 227556, 524379, 509266, 262606]
si_dict = {}
i = 0
for x in keys:
    num = si_vals[i]
    i += 1
    val = (num/si_total) * 100
    si_dict[x] = val


# In[ ]:


si_win_vals = [243879, 80561, 70496, 116707, 36189, 26581, 178855, 33807, 35618, 150827, 44610, 472774, 51117, 21313, 37717, 38961, 22931, 59872, 56167, 5498]
si_win_dict = {}
i = 0
for x in keys:
    num = si_win_vals[i]
    i += 1
    val = (num/si_win_total) * 100
    si_win_dict[x] = val


# In[ ]:


si_lose_vals = [2570186, 742536, 811037, 1013488, 482350, 331366, 1476265, 258594, 249201, 1684189, 537831, 5858923, 630936, 228689, 343189, 330007, 204625, 464507, 453099, 257108]
si_lose_dict = {}
i = 0
for x in keys:
    num = si_lose_vals[i]
    i += 1
    val = (num/si_lose_total) * 100
    si_lose_dict[x] = val


# In[ ]:


si_all_vals = si_dict.values()
si_win_vals = si_win_dict.values()
si_lose_vals = si_lose_dict.values()
si_win_diff_vals = []
si_lose_diff_vals = []
for x in keys:
    num = si_dict[x]
    win = si_win_dict[x]
    lose = si_lose_dict[x]
    win_pct = win - num
    lose_pct = lose - num
    si_win_diff_vals.append(win_pct)
    si_lose_diff_vals.append(lose_pct)


# In[ ]:


fig, ax= plt.subplots(figsize = [12,12])
plt.bar(keys, all_vals, color = 'green')
ax.figure.autofmt_xdate()
plt.ylabel('Pct Boon Chosen', fontsize = 15)
plt.xlabel('Chosen Boon', fontsize = 15)
plt.title('Percentage a Neow Boon is Chosen For The Silent')
plt.show()


# In[ ]:


fig, ax= plt.subplots(figsize = [12,12])
plt.bar(keys, win_diff_vals, color = 'green')
ax.figure.autofmt_xdate()
plt.ylabel('Pct Boon Chosen', fontsize = 15)
plt.xlabel('Chosen Boon', fontsize = 15)
plt.title('Pct Diff a Winning Silent Chooses a Boon')
plt.show()


# In[ ]:


fig, ax= plt.subplots(figsize = [12,12])
plt.bar(keys, lose_diff_vals, color = 'green')
ax.figure.autofmt_xdate()
plt.ylabel('Pct Boon Chosen', fontsize = 15)
plt.xlabel('Chosen Boon', fontsize = 15)
plt.title('Pct Diff a Losing Silent Chooses a Boon')
plt.show()


# ## Processing Defect Data

# In[ ]:


de_total = 19812913
de_win_total = 1702447
de_lose_total = 18110466


# In[ ]:


de_vals = [1644157, 870459, 984166, 1204844, 556540, 391141, 1702021, 341075, 329371, 1721335, 640489, 5750191, 788627, 251657, 446380, 437129, 252316, 578242, 694059, 228714]
de_dict = {}
i = 0
for x in keys:
    num = de_vals[i]
    i += 1
    val = (num/de_total) * 100
    de_dict[x] = val


# In[ ]:


de_win_vals = [139567, 83020, 80421, 121448, 38740, 26193, 179026, 36853, 35998, 149974, 52346, 425626, 59639, 21428, 43811, 44162, 26225, 62376, 70838, 4756]
de_win_dict = {}
i = 0
for x in keys:
    num = de_win_vals[i]
    i += 1
    val = (num/de_win_total) * 100
    de_win_dict[x] = val


# In[ ]:


de_lose_vals = [1504590, 787439, 903745, 1083396, 517800, 364948, 1522995, 304222, 293373, 1571361, 588143, 5324565, 728988, 230229, 402569, 392967, 226091, 515866, 623221, 223958]
de_lose_dict = {}
i = 0
for x in keys:
    num = de_lose_vals[i]
    i += 1
    val = (num/de_lose_total) * 100
    de_lose_dict[x] = val


# In[ ]:


de_all_vals = de_dict.values()
de_win_vals = de_win_dict.values()
de_lose_vals = de_lose_dict.values()
de_win_diff_vals = []
de_lose_diff_vals = []
for x in keys:
    num = de_dict[x]
    win = de_win_dict[x]
    lose = de_lose_dict[x]
    win_pct = win - num
    lose_pct = lose - num
    de_win_diff_vals.append(win_pct)
    de_lose_diff_vals.append(lose_pct)


# In[ ]:


fig, ax= plt.subplots(figsize = [12,12])
plt.bar(keys, all_vals, color = 'blue')
ax.figure.autofmt_xdate()
plt.ylabel('Pct Boon Chosen', fontsize = 15)
plt.xlabel('Chosen Boon', fontsize = 15)
plt.title('Percentage a Neow Boon is Chosen For Defect')
plt.show()


# In[ ]:


fig, ax= plt.subplots(figsize = [12,12])
plt.bar(keys, win_diff_vals, color = 'blue')
ax.figure.autofmt_xdate()
plt.ylabel('Pct Boon Chosen', fontsize = 15)
plt.xlabel('Chosen Boon', fontsize = 15)
plt.title('Pct Diff a Winning Defect Chooses a Boon')
plt.show()


# In[ ]:


fig, ax= plt.subplots(figsize = [12,12])
plt.bar(keys, lose_diff_vals, color = 'blue')
ax.figure.autofmt_xdate()
plt.ylabel('Pct Boon Chosen', fontsize = 15)
plt.xlabel('Chosen Boon', fontsize = 15)
plt.title('Pct Diff a Losing Defect Chooses a Boon')
plt.show()


# ## Processing Watcher Data

# In[ ]:


wa_total = 1954837
wa_win_total = 184504
wa_lose_total = 1770333


# In[ ]:


wa_vals = [249727, 68849, 86876, 96161, 41698, 45132, 135168, 27546, 28152, 216319, 53051, 588957, 67239, 25689, 35723, 36150, 22646, 45528, 62426, 21800]
wa_dict = {}
i = 0
for x in keys:
    num = wa_vals[i]
    i += 1
    val = (num/wa_total) * 100
    wa_dict[x] = val


# In[ ]:


wa_win_vals = [33139, 6391, 7547, 10582, 2943, 4286,14262, 3465, 4501, 15710, 4080, 46451, 6198, 2095, 3575, 4594, 2263, 5466, 6902, 54]
wa_win_dict = {}
i = 0
for x in keys:
    num = wa_win_vals[i]
    i += 1
    val = (num/wa_win_total) * 100
    wa_win_dict[x] = val


# In[ ]:


wa_lose_vals = [216588, 62458, 79329, 85579, 38755, 40846, 120906, 24081, 23651, 200609, 48971, 542506, 61041, 23594, 32148, 31556, 20383, 40062, 55524, 21746]
wa_lose_dict = {}
i = 0
for x in keys:
    num = wa_lose_vals[i]
    i += 1
    val = (num/wa_lose_total) * 100
    wa_lose_dict[x] = val


# In[ ]:


wa_all_vals = wa_dict.values()
wa_win_vals = wa_win_dict.values()
wa_lose_vals = wa_lose_dict.values()
wa_win_diff_vals = []
wa_lose_diff_vals = []
for x in keys:
    num = wa_dict[x]
    win = wa_win_dict[x]
    lose = wa_lose_dict[x]
    win_pct = win - num
    lose_pct = lose - num
    wa_win_diff_vals.append(win_pct)
    wa_lose_diff_vals.append(lose_pct)


# In[ ]:


fig, ax= plt.subplots(figsize = [12,12])
plt.bar(keys, all_vals, color = 'magenta')
ax.figure.autofmt_xdate()
plt.ylabel('Pct Boon Chosen', fontsize = 15)
plt.xlabel('Chosen Boon', fontsize = 15)
plt.title('Percentage a Neow Boon is Chosen For Watcher')
plt.show()


# In[ ]:


fig, ax= plt.subplots(figsize = [12,12])
plt.bar(keys, win_diff_vals, color = 'magenta')
ax.figure.autofmt_xdate()
plt.ylabel('Pct Boon Chosen', fontsize = 15)
plt.xlabel('Chosen Boon', fontsize = 15)
plt.title('Pct Diff a Winning Watcher Chooses a Boon')
plt.show()


# In[ ]:


fig, ax= plt.subplots(figsize = [12,12])
plt.bar(keys, lose_diff_vals, color = 'magenta')
ax.figure.autofmt_xdate()
plt.ylabel('Pct Boon Chosen', fontsize = 15)
plt.xlabel('Chosen Boon', fontsize = 15)
plt.title('Pct Diff a Losing Watcher Chooses a Boon')
plt.show()

