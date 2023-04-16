'''
python Multiplications_Generator.py
'''

import numpy as np # Importing Numpy for arrays, matrices, etc. manipulation 
import pandas as pd # Importing Pandas for dataframes creation and manipulation
from psychopy import gui, core # Importing these two modules for the savefile window

################################################################################

myDlg = gui.Dlg(title = 'Multiplications Generator',) # The dialog window poping out when the script starts
myDlg.addField('Filename for original output:')
#myDlg.addField('Filename for sorted output:')
show_dlg = myDlg.show()

if myDlg.OK:
    if len(show_dlg[0]) < 1:# or len(show_dlg[1]) < 1:
        print('Filename cannot be empty. Run again')
        myDlgerror = gui.Dlg(title = 'Error', labelButtonCancel='OK',)
        myDlgerror.addText('Filename cannot be empty. Run again')
        show_dlg = myDlgerror.show()
        if myDlgerror.OK:
            core.quit()
        else:
            core.quit()
    else:
        save_file_name = show_dlg[0] + '.xlsx' # It will saved in the same folder ot the script file
        #save_file_name_sort = show_dlg[1] + '.xlsx'
else:
    print('Cancelled: Program closed')
    myDlgcanc = gui.Dlg(title = 'OK. Done.', labelButtonCancel='OK')
    myDlgcanc.addText('Cancelled: Program closed.')
    show_dlg = myDlgcanc.show()
    if myDlgcanc.OK:
        core.quit()
    else:
        core.quit()

################################################################################

init_pool = list(range(0, 100)) # Setting our initial pool
#print(init_pool)

################################################################################

no_zero = []
bin_array_zero = []
for i in range(len(init_pool)): 
    if not (init_pool[i])%10 == 0:
        no_zero.append(init_pool[i]) # All numbers without zero at the end are stored
    elif (init_pool[i])%10 == 0:
        bin_array_zero.append(init_pool[i]) # All numbers with a zero at the end are stored
pool = no_zero # Assign our transformed pool to 'pool'

################################################################################

def istwodigits(n): # This function take an integer as argument
    n = [int(n) for n in str(n)]
    if len(n) > 1: # It returns whether the number is formed by two digits and the digits theirselves
        if n[0] != n[1]:
            n1, n2 = n[0], n[1] 
            return 0, n1, n2 # And if the two digits are different
        elif n[0] == n[1]:
            n1, n2 = n[0], n[1]
            return 1, n1, n2 # Or not
    else:
        return -1, n # Single digit

################################################################################

no_double = []
bin_array_double = []
for i in pool:
    if istwodigits(i)[0] == 0:
        no_double.append(i)
    elif istwodigits(i)[0] == 1:
        bin_array_double.append(i)
    elif istwodigits(i)[0] == -1:
        no_double.append(i)
pool = no_double # Our pool is furtherly cleared and re-assigned to 'pool'
trash_pool = np.concatenate([bin_array_zero, bin_array_double]) # Numbers like: 0, 10, 11, 20, 22... are thrown in the trash

################################################################################

multiplications1_1 = []
multiplications1_2 = []
multiplications1_3 = []
multiplications1_4 = []
multiplications2_1 = []
multiplications2_2 = []
multiplications2_3 = []                       # Creating the entire multiplications pool 
multiplications2_4 = []
results_multiplications1_1 = []
results_multiplications1_2 = []
results_multiplications1_3 = []
results_multiplications1_4 = []
results_multiplications2_1 = []
results_multiplications2_2 = []
results_multiplications2_3 = []
results_multiplications2_4 = []
for a in pool:                          # Remember, our additions are like '3 + ? = 7'. We have to consider the difference...like '7 - 3'
    for c in pool:
        if int(c/a) in pool and int(c/a) not in trash_pool: 
             if a != 1 and a != 2: # Our first factor (ex. 3) is set diffeent from 1 and 2 (my decision)
                if int(c/a) != 1 and int(c/a) != 2: # Our differnce too
                    if c%a == 0:
                        if istwodigits(c)[0] == -1: # Our result (7) is a single digit
                            if istwodigits(a)[0] == -1 and istwodigits(int(c/a))[0] == -1: # No carry beacuse -> single digit in both factors
                                multiplications1_1.append([a, c]) 
                                results_multiplications1_1.append(int(c/a))
                            '''
                            elif istwodigits(a)[0] == 0 and istwodigits(c - a)[0] == -1:
                                multiplications1_2.append([a, c])
                                results_multiplications1_2.append(c - a)
                            elif istwodigits(a)[0] == -1 and istwodigits(c - a)[0] == 0: # This snippet is grayed beacuse they are all empty arrays
                                multiplications1_3.append([a, c])
                                results_multiplications1_3.append(c - a)
                            elif istwodigits(a)[0] == 0 and istwodigits(c - a)[0] == 0:
                                multiplications1_4.append([a, c])
                                results_multiplications1_4.append(c - a)
                            '''
                        if istwodigits(c)[0] == 0: # Our result is a double digit (ex. 12)
                            if istwodigits(a)[0] == -1 and istwodigits(int(c/a))[0] == -1: # First factor is single, second same
                                multiplications2_1.append([a, c]) # Only carry
                                results_multiplications2_1.append(int(c/a))
                            elif istwodigits(a)[0] == 0 and istwodigits(int(c/a))[0] == -1: # First factor is double, second single
                                multiplications2_2.append([a, c]) # Mixed
                                results_multiplications2_2.append(int(c/a))
                            elif istwodigits(a)[0] == -1 and istwodigits(int(c/a))[0] == 0:  # First factor is single, second double
                                multiplications2_3.append([a, c]) # Mixed
                                results_multiplications2_3.append(int(c/a))
                            
                            '''
                            elif istwodigits(a)[0] == 0 and istwodigits(int(c/a))[0] == 0:  # First factor is double, second same
                                multiplications2_4.append([a, c]) # Mixed
                                results_multiplications2_4.append(int(c/a))
                            '''
                        
#multiplications1_2, multiplications1_3, multiplications1_4 = multiplications1_2[: len(multiplications1_1)], multiplications1_3[: len(multiplications1_1)], multiplications1_4[: len(multiplications1_1)]
#multiplications2_2, multiplications2_3, multiplications2_4 = multiplications2_2[: len(multiplications2_1)], multiplications2_3[: len(multiplications2_1)], multiplications2_4[: len(multiplications2_1)]
#results_multiplications2_2, results_multiplications2_3, results_multiplications2_4 = results_multiplications2_2[: len(multiplications2_1)], results_multiplications2_3[: len(multiplications2_1)], results_multiplications2_4[: len(multiplications2_1)]

'''
def iscarry(array): # This function unentangle previous sets and splits them in carry/no-carry sets
    empty_1 = []
    empty_2 = []
    empty_3 = []
    for i in range(len(array)):
        a = array[i][0]
        c = array[i][1]
        if istwodigits(a)[0] == -1 and istwodigits(c)[0] == -1:
            empty_1.append([a, c]) # No carry of course
        if istwodigits(c)[0] == 0:
            n2c = istwodigits(c)[2]
            if istwodigits(a)[0] == 0:
                n2a = istwodigits(a)[2]
                if n2c >= n2a:
                    empty_2.append([a, c]) # No carry
                if n2c < n2a:
                    empty_3.append([a, c]) # Carry
            if istwodigits(a)[0] == -1:
                n2a = a
                if n2c >= a:
                    empty_2.append([a, c]) # No carry
                if n2c < a:
                    empty_3.append([a, c]) # Carry
                    
    array1 = empty_1
    array2 = empty_2
    array3 = empty_3
    return array1, array2, array3
'''

################################################################################

'''
multiplications1_1 = iscarry(multiplications1_1)[0] # Assigning manually each possible combination (double/single digit numbers are considered for each factor and result, carry/no-carry is considered too)
multiplications2_1 = iscarry(multiplications2_1)[2]
multiplications2_2 = (iscarry(multiplications2_2)[1], iscarry(multiplications2_2)[2])
multiplications2_3 = (iscarry(multiplications2_3)[1], iscarry(multiplications2_3)[2])
multiplications2_4 = (iscarry(multiplications2_4)[1], iscarry(multiplications2_4)[2])
'''

def dict(array): # This function creates the 'string' part
    dictionary = []
    for i in range(len(array)):
        dictionary.append('%d x ? = %d' %(array[i][0], array[i][1]))
        dictionary.append('? x %d = %d' %(array[i][0], array[i][1]))
    return dictionary

def res(array): # Creating results arrays
    results = []
    for i in range(len(array)):
        results.append(int(array[i][1] / array[i][0]))
        results.append(int(array[i][1] / array[i][0]))
    return results

dictionary1_1 = dict(multiplications1_1) # Creating our 'graphic' part with two possible switches of '?'
dictionary2_1 = dict(multiplications2_1)
dictionary2_2 = dict(multiplications2_2)
dictionary2_3 = dict(multiplications2_3)

'''
dictionary2_4 = dict(multiplications2_4)
#print(dictionary2_4)
#print(len(dictionary2_4))
'''

'''
dictionary2_2_1 = dict(multiplications2_2[0])
dictionary2_2_2 = dict(multiplications2_2[1])
dictionary2_3_1 = dict(multiplications2_3[0])
dictionary2_3_2 = dict(multiplications2_3[1])
dictionary2_4_1 = dict(multiplications2_4[0])
dictionary2_4_2 = dict(multiplications2_4[1])
'''

results1_1 = res(multiplications1_1)
results2_1 = res(multiplications2_1)
results2_2 = res(multiplications2_2)
results2_3 = res(multiplications2_3)

'''
results2_4 = res(multiplications2_4)
'''

'''
results2_2_1 = res(multiplications2_2[0])
results2_2_2 = res(multiplications2_2[1])
results2_3_1 = res(multiplications2_3[0])
results2_3_2 = res(multiplications2_3[1])
results2_4_1 = res(multiplications2_4[0])
results2_4_2 = res(multiplications2_4[1])
'''
################################################################################

df1 = pd.DataFrame({'1-1-1-n': dictionary1_1[:len(dictionary1_1): 2], # Join everything in dataframes
                    '1-1-1-r': dictionary1_1[1:len(dictionary1_1): 2],
                    '<- RESULTS1': results1_1[:len(results1_1): 2]})
                    
df2 = pd.DataFrame({'1-1-2-ca': dictionary2_1[:len(dictionary2_1): 2],
                    '1-1-2-r-ca': dictionary2_1[1:len(dictionary2_1): 2],
                    '<- RESULTS2': results2_1[:len(results2_1): 2]})

df3 = pd.DataFrame({'2-1-2-ca': dictionary2_2[:len(dictionary2_2): 2],
                    '2-1-2-r-ca': dictionary2_2[1:len(dictionary2_2): 2],
                    '<- RESULTS3': results2_2[:len(results2_2): 2]})
                    
df4 = pd.DataFrame({'1-2-2-ca': dictionary2_3[:len(dictionary2_3): 2],
                    '1-2-2-r-ca': dictionary2_3[1:len(dictionary2_3): 2],
                    '<- RESULTS4': results2_3[:len(results2_3): 2]})

'''
df5 = pd.DataFrame({'1-1-2-n-ca': dictionary2_4[:len(dictionary2_4): 2],
                    '1-1-2-r-ca': dictionary2_4[1:len(dictionary2_4): 2],
                    '<- RESULTS5': results2_4[:len(results2_4): 2]})

df3 = pd.DataFrame({'2-1-2-n': dictionary2_2_1[:len(dictionary2_2_1): 2],
                    '2-1-2-r': dictionary2_2_1[1:len(dictionary2_2_1): 2],
                    '<- RESULTS3': results2_2_1[:len(results2_2_1): 2]})

df4 = pd.DataFrame({'2-1-2-ca': dictionary2_2_2[:len(dictionary2_2_2): 2],
                    '2-1-2-r-ca': dictionary2_2_2[1:len(dictionary2_2_2): 2],
                    '<- RESULTS4': results2_2_2[:len(results2_2_2): 2]})

df5 = pd.DataFrame({'1-2-2-n': dictionary2_3_1[:len(dictionary2_3_1): 2],
                    '1-2-2-r': dictionary2_3_1[1:len(dictionary2_3_1): 2],
                    '<- RESULTS5': results2_3_1[:len(results2_3_1): 2]})

df6 = pd.DataFrame({'1-2-2-ca': dictionary2_3_2[:len(dictionary2_3_2): 2],
                    '1-2-2-r-ca': dictionary2_3_2[1:len(dictionary2_3_2): 2],
                    '<- RESULTS6': results2_3_2[:len(results2_3_2): 2]})

df7 = pd.DataFrame({'2-2-2-n': dictionary2_4_1[:len(dictionary2_4_1): 2],
                    '2-2-2-r': dictionary2_4_1[1:len(dictionary2_4_1): 2],
                    '<- RESULTS7': results2_4_1[:len(results2_4_1): 2]})

df8 = pd.DataFrame({'2-2-2-ca': dictionary2_4_2[:len(dictionary2_4_2): 2],
                    '2-2-2-r-ca': dictionary2_4_2[1:len(dictionary2_4_2): 2],
                    '<- RESULTS8': results2_4_2[:len(results2_4_2): 2]})
'''

Multiplications = pd.concat([df1, df2, df3, df4], axis = 1) # Joining everything in one single excel file and saving it
Multiplications.to_excel(save_file_name, index = False)
print('%s saved. Program closed' %(save_file_name))

################################################################################
