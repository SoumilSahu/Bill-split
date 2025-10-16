'''
Soumil Sahu @ 2025

Code to split bill among a group of people. The paid and owed values for 
each type of transaction is to be specified in the 'values.dat' file.
The format of specifiying the transactions is specified in the readme 
file. 
'''

'''
Importing necessary stuff
'''
import numpy as np

'''
Defining functions
'''
def sort_dict(dic): #sort a dictionary by values
    keys = list(dic.keys())
    vals = np.array(list(dic.values()),dtype=float)
    sort_val_idx = np.argsort(vals)
    sorted_dic = {keys[i]:vals[i] for i in sort_val_idx}
    return sorted_dic

# This split function can be imported and then used on any local .dat file
def split(file_path = 'values.dat'):
    '''
    Reading file
    '''
    file = open(file_path,'r')
    line = []
    for i in file:
        line.append(i.split(' ')[:-1]) #don't include '\n'

    '''
    Make dictionary with keys being each person and values their owed amount.
    Positive amount implies they are owed, negative means they owe.
    To start 0.0 is assigned to each person
    '''
    All = {} 
    for i in range(len(line[0])-3):
        All[line[0][i+3]]=0.0

    '''
    Update the 'paid' value from each transaction
    '''
    for i in range(1,len(line)):
        payer = line[i][1] #payer name
        amt = line[i][2] #paid amount
        if payer in All.keys():
            All[payer] = float(amt)
        else:
            raise ValueError(f'Payer \'{payer}\' not found list of people, please check spelling (case sensitive).')

    '''
    Update owed values
    '''
    for j in range(1,len(line)):
        if 'e' in line[j]:
            num_e = line[j].count('e') #number of time 'e' occurs
            eq_amt = float(line[j][2])/num_e #the equal split amount
            for i in range(3,len(line[0])):
                pers = line[0][i]
                if line[j][i] == 'e':
                    All[pers] -= eq_amt
                else:
                    All[pers] -= float(line[j][i])
        else:
            for i in range(3,len(line[0])):
                pers = line[0][i]
                All[pers] -= float(line[j][i])

    '''
    Separate into givers and takers
    '''
    persons = list(All.keys())
    Givers = {}
    Takers = {}
    for i in range(len(persons)):
        if All[persons[i]] > 0:
            Takers[persons[i]] = All[persons[i]]
        elif All[persons[i]] < 0:
            Givers[persons[i]] = abs(All[persons[i]])
        else:
            continue

    '''
    Sort the dictionaries 
    '''
    Givers_ = sort_dict(Givers)
    Takers_ = sort_dict(Takers)

    '''
    Consistency check
    '''
    give_tot = sum(list(Givers_.values()))
    take_tot = sum(list(Takers_.values()))
    if give_tot != take_tot:
        raise ValueError('There is a mismatch in give and take balance, please check enteries.')

    '''
    Iterate through each 'giver' and note transactions.
    The smallest giver starts by giving to takers in increasing order of
    amount.
    Then we go to the next smallest giver and so on.
    '''
    Trans = {}
    Giv_names = list(Givers_.keys())
    Tak_names = list(Takers_.keys())

    for i in range(len(Giv_names)):
        debt = Givers_[Giv_names[i]]
        # print(debt)
        taker_idx = 0
        while debt != 0.0:
            if Takers_[Tak_names[taker_idx]] == 0.0:
                taker_idx += 1
            else:
                val = min(debt,Takers_[Tak_names[taker_idx]])
                Trans[f'{Giv_names[i]} -> {Tak_names[taker_idx]}'] = val
                Givers_[Giv_names[i]] -= val
                Takers_[Tak_names[taker_idx]] -= val
                debt = Givers_[Giv_names[i]]
                taker_idx += 1

    '''
    Print the final transactions
    '''
    for i in list(Trans.keys()):
        print(f'{i} : {Trans[i]}\n')