'''
python Subtractions_Generator.py
'''

################################################################################

import numpy as np # Importing Numpy for arrays, matrices, etc. manipulation 
import pandas as pd # Importing Pandas for dataframes creation and manipulation
from psychopy import gui, core # Importing these two modules for the savefile window

################################################################################

myDlg = gui.Dlg(title = 'Subtractions Generator',) # The dialog window poping out when the script starts
myDlg.addField('Filename for original output:')
myDlg.addField('Filename for sorted output:')
show_dlg = myDlg.show()

if myDlg.OK:
    if len(show_dlg[0]) < 1 or len(show_dlg[1]) < 1:
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
        save_file_name_sort = show_dlg[1] + '.xlsx'
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

subtractions1_1 = []
subtractions1_2 = []
subtractions1_3 = []
subtractions1_4 = []
subtractions2_1 = []
subtractions2_2 = []
subtractions2_3 = []                       # Creating the entire subtractions pool 
subtractions2_4 = []
results_subtractions1_1 = []
results_subtractions1_2 = []
results_subtractions1_3 = []
results_subtractions1_4 = []
results_subtractions2_1 = []
results_subtractions2_2 = []
results_subtractions2_3 = []
results_subtractions2_4 = []

for a in pool:                          # Remember, our subtractions are like '3 + ? = 7'. We have to consider the difference...like '7 - 3'
    for c in pool:
        if c - a in pool and c - a not in trash_pool:  # So, our difference must be included in our pool (0, 10, 11 etc. are not accepted)
            if a != 1 and a != 2: # Our first factor (ex. 3) is set diffeent from 1 and 2 (my decision)
                if c - a != 1 and c - a != 2: # Our differnce too
                    if istwodigits(c)[0] == -1: # Our result (7) is a single digit
                        if istwodigits(a)[0] == -1 and istwodigits(c - a)[0] == -1: # No carry beacuse -> single digit in both factors
                            subtractions1_1.append([a, c]) 
                            results_subtractions1_1.append(c - a)
                        '''
                        elif istwodigits(a)[0] == 0 and istwodigits(c - a)[0] == -1:
                            subtractions1_2.append([a, c])
                            results_subtractions1_2.append(c - a)
                        elif istwodigits(a)[0] == -1 and istwodigits(c - a)[0] == 0: # This snippet is grayed beacuse they are all empty arrays
                            subtractions1_3.append([a, c])
                            results_subtractions1_3.append(c - a)
                        elif istwodigits(a)[0] == 0 and istwodigits(c - a)[0] == 0:
                            subtractions1_4.append([a, c])
                            results_subtractions1_4.append(c - a)
                        '''
                    if istwodigits(c)[0] == 0: # Our result is a double digit (ex. 12)
                        if istwodigits(a)[0] == -1 and istwodigits(c - a)[0] == -1: # First factor is single, second same
                            subtractions2_1.append([a, c]) # Only carry
                            results_subtractions2_1.append(c - a)
                        elif istwodigits(a)[0] == 0 and istwodigits(c - a)[0] == -1: # First factor is double, second single
                            subtractions2_2.append([a, c]) # Mixed
                            results_subtractions2_2.append(c - a)
                        elif istwodigits(a)[0] == -1 and istwodigits(c - a)[0] == 0:  # First factor is single, second double
                            subtractions2_3.append([a, c]) # Mixed
                            results_subtractions2_3.append(c - a)
                        elif istwodigits(a)[0] == 0 and istwodigits(c - a)[0] == 0:  # First factor is double, second same
                            subtractions2_4.append([a, c]) # Mixed
                            results_subtractions2_4.append(c - a)

#subtractions1_2, subtractions1_3, subtractions1_4 = subtractions1_2[: len(subtractions1_1)], subtractions1_3[: len(subtractions1_1)], subtractions1_4[: len(subtractions1_1)]
#subtractions2_2, subtractions2_3, subtractions2_4 = subtractions2_2[: len(subtractions2_1)], subtractions2_3[: len(subtractions2_1)], subtractions2_4[: len(subtractions2_1)]
#results_subtractions2_2, results_subtractions2_3, results_subtractions2_4 = results_subtractions2_2[: len(subtractions2_1)], results_subtractions2_3[: len(subtractions2_1)], results_subtractions2_4[: len(subtractions2_1)]

subtractions1_1 = [(sub[1], sub[0]) for sub in subtractions1_1]
subtractions2_1 = [(sub[1], sub[0]) for sub in subtractions2_1]
subtractions2_2 = [(sub[1], sub[0]) for sub in subtractions2_2]
subtractions2_3 = [(sub[1], sub[0]) for sub in subtractions2_3]
subtractions2_4 = [(sub[1], sub[0]) for sub in subtractions2_4]

################################################################################

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

################################################################################

subtractions1_1 = iscarry(subtractions1_1)[0] # Assigning manually each possible combination (double/single digit numbers are considered for each factor and result, carry/no-carry is considered too)
subtractions2_1 = iscarry(subtractions2_1)[2]
subtractions2_2 = (iscarry(subtractions2_2)[1], iscarry(subtractions2_2)[2])
subtractions2_3 = (iscarry(subtractions2_3)[1], iscarry(subtractions2_3)[2])
subtractions2_4 = (iscarry(subtractions2_4)[1], iscarry(subtractions2_4)[2])

'''
subtractions1_1 = [(sub[1], sub[0]) for sub in subtractions1_1]
subtractions2_1 = [(sub[1], sub[0]) for sub in subtractions2_1]
subtractions2_2 = [(sub[1], sub[0]) for sub in subtractions2_2]
subtractions2_3 = [(sub[1], sub[0]) for sub in subtractions2_3]
subtractions2_4 = [(sub[1], sub[0]) for sub in subtractions2_4]
'''

def dict(array): # This function creates the 'string' part
    dictionary = []
    for i in range(len(array)):
        dictionary.append('%d - ? = %d' %(array[i][0], array[i][1]))
        #dictionary.append('? + %d = %d' %(array[i][0], array[i][1]))
    return dictionary

def res(array): # Creating results arrays
    results = []
    for i in range(len(array)):
        results.append(array[i][0] - array[i][1])
        #results.append(array[i][0] - array[i][1])
    return results

dictionary1_1 = dict(subtractions1_1) # Creating our 'graphic' part with two possible switches of '?'
dictionary2_1 = dict(subtractions2_1)
dictionary2_2_1 = dict(subtractions2_2[0])
dictionary2_2_2 = dict(subtractions2_2[1])
dictionary2_3_1 = dict(subtractions2_3[0])
dictionary2_3_2 = dict(subtractions2_3[1])
dictionary2_4_1 = dict(subtractions2_4[0])
dictionary2_4_2 = dict(subtractions2_4[1])

results1_1 = res(subtractions1_1)
results2_1 = res(subtractions2_1)
results2_2_1 = res(subtractions2_2[0])
results2_2_2 = res(subtractions2_2[1])
results2_3_1 = res(subtractions2_3[0])
results2_3_2 = res(subtractions2_3[1])
results2_4_1 = res(subtractions2_4[0])
results2_4_2 = res(subtractions2_4[1])

'''
df1 = pd.DataFrame({'1-1-1-n': dictionary1_1[:len(dictionary1_1): 2], # Join everything in dataframes
                    '1-1-1-r': dictionary1_1[1:len(dictionary1_1): 2],
                    '<- RESULTS1': results1_1[:len(results1_1): 2]})
                    
df2 = pd.DataFrame({'1-1-2-n-ca': dictionary2_1[:len(dictionary2_1): 2],
                    '1-1-2-r-ca': dictionary2_1[1:len(dictionary2_1): 2],
                    '<- RESULTS2': results2_1[:len(results2_1): 2]})

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

df1 = pd.DataFrame({'1-1-1-n': dictionary1_1, # Join everything in dataframes
                    '<- RESULTS1': results1_1})

'''
df2 = pd.DataFrame({'1-1-2-n-ca': dictionary2_1,
                    '<- RESULTS2': results2_1})
'''

df3 = pd.DataFrame({'2-1-2-ca': dictionary2_2_1,
             
                    '<- RESULTS3': results2_2_1})

df4 = pd.DataFrame({'2-1-2-n': dictionary2_2_2,
    
                    '<- RESULTS4': results2_2_2})

'''
df5 = pd.DataFrame({'1-2-2-n': dictionary2_3_1,
    
                    '<- RESULTS5': results2_3_1})

df6 = pd.DataFrame({'1-2-2-ca': dictionary2_3_2,
              
                    '<- RESULTS6': results2_3_2})
'''

df7 = pd.DataFrame({'2-2-2-ca': dictionary2_4_1,
            
                    '<- RESULTS7': results2_4_1})

df8 = pd.DataFrame({'2-2-2-n': dictionary2_4_2,

                    '<- RESULTS8': results2_4_2})
                    
Subtractions = pd.concat([df1, df3, df4, df7, df8], axis = 1) # Joining everything in one single excel file and saving it
Subtractions.to_excel(save_file_name, index = False)
print('%s saved. Program closed' %(save_file_name))

def distro(results_array, dictionary):
    distribution = np.unique(results_array)
    indexes = []
    sub_dictionary = []
    frequencies = []
    results = []
    for i in range(len(distribution)):
        indexes.append([y for y, x in enumerate(results_array) if x == distribution[i]])
        frequencies.append(['%d' %(distribution[i]), len(indexes[i])])
        sub_dictionary.append([dictionary[index] for index in indexes[i]])
        results.append([results_array[index] for index in indexes[i]])
    
    '''
    for i in range(len(distribution)):
        sub_dictionary.append([dictionary_reversed[index] for index in indexes[i]])
        results.append([results_array[index] for index in indexes[i]])
    '''
    
    sub_dictionary = [item for sublist in sub_dictionary for item in sublist]
    results = [item for sublist in results for item in sublist]
    return frequencies, sub_dictionary, results

sub_df1 = distro(df1.iloc[:, 1], df1.iloc[:, 0])
df1n = pd.DataFrame({#'Frequecies': sub_df1[0], 
                        '1-1-1-n': sub_df1[1],
                        '<- RESULTS1': sub_df1[2]})
#df1n.to_excel('ab.xlsx', index = False)

'''
sub_df2 = distro(df2.iloc[:, 2], df2.iloc[:, 0], df2.iloc[:, 1])
df2n = pd.DataFrame({#'Frequecies': sub_df2[0], 
                        '1-1-2-ca': sub_df2[1],
                        '<- RESULTS2': sub_df2[2]})
#df2n.to_excel('ac.xlsx', index = False)
'''

sub_df3 = distro(df3.iloc[:, 1], df3.iloc[:, 0])
df3n = pd.DataFrame({#'Frequecies': sub_df3[0], 
                        '2-1-2-ca': sub_df3[1],
                        '<- RESULTS3': sub_df3[2]})
#df3n.to_excel('ab.xlsx', index = False)

sub_df4 = distro(df4.iloc[:, 1], df4.iloc[:, 0])
df4n = pd.DataFrame({#'Frequecies': sub_df4[0], 
                        '2-1-2-n': sub_df4[1],
                        '<- RESULTS4': sub_df4[2]})
#df4n.to_excel('ac.xlsx', index = False)

'''
sub_df5 = distro(df5.iloc[:, 2], df5.iloc[:, 0], df5.iloc[:, 1])
df5n = pd.DataFrame({#'Frequecies': sub_df5[0], 
                        '1-1-2-n': sub_df5[1],
                        '<- RESULTS5': sub_df5[2]})
#df5n.to_excel('ab.xlsx', index = False)

sub_df6 = distro(df6.iloc[:, 2], df6.iloc[:, 0], df6.iloc[:, 1])
df6n = pd.DataFrame({#'Frequecies': sub_df6[0], 
                        '1-1-2-ca': sub_df6[1],
                        '<- RESULTS6': sub_df6[2]})
#df6n.to_excel('ac.xlsx', index = False)
'''

sub_df7 = distro(df7.iloc[:, 1], df7.iloc[:, 0])
df7n = pd.DataFrame({#'Frequecies': sub_df7[0], 
                        '2-2-2-ca': sub_df7[1],
                        '<- RESULTS7': sub_df7[2]})
#df7n.to_excel('ab.xlsx', index = False)

sub_df8 = distro(df8.iloc[:, 1], df8.iloc[:, 0])
df8n = pd.DataFrame({#'Frequecies': sub_df8[0], 
                        '2-2-2-n': sub_df8[1],
                        '<- RESULTS8': sub_df8[2]})
#df8n.to_excel('ac.xlsx', index = False)

Subtractions = pd.concat([df1n, df3n, df4n, df7n, df8n], axis = 1) # Joining everything in one single excel file and saving it
Subtractions.to_excel(save_file_name_sort, index = False)
print('%s saved. Program closed' %(save_file_name_sort))

################################################################################