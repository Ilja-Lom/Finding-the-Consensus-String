'''
Author: Ilja Lom...
GitHub: https://github.com/Ilja-Lom
Publication-Date: 17/09/2021
Description: 
    An algorithm to find the consensus string given two or more homologous DNA sequences. See the included documentation
    in the repository for more detail
'''

'''Initialising the variables'''
nuc_dict = {"adenine": 0, "thymine": 0, "guanine": 0, "cytosine": 0} #nucleotide_dictionary
a_count = [] #counts the number of adenine nucleotides in each position in the sequence
t_count = []
g_count = []
c_count = []
cat_string = [] #short for 'consensus string'
list = [] #list of homologous sequences

repeat = True
while repeat==True:
   seq_input = input("Enter the homologous sequences you wish to analyse. They must be of equal length. Once you are finished, enter 'n':\n")
   if seq_input == "n":
      repeat = False
      break
   list.append(seq_input) #this is here to stop 'n' being appended to the list

'''Analysing the sequences'''
for i in range(len(list[0])): #cycles letters in element
   for element in list: #cycles elements in list
      if element[i] == "A":
         nuc_dict["adenine"] += 1
      if element[i] == "T":
         nuc_dict["thymine"] += 1
      if element[i] == "G":
         nuc_dict["guanine"] += 1
      if element[i] == "C":
         nuc_dict["cytosine"] += 1

   cat_string.append(max(nuc_dict, key=nuc_dict.get)) #finds the largest value within nuc_dict, returns corresponding nucleotide
   a_count.append(nuc_dict["adenine"])
   t_count.append(nuc_dict["thymine"])
   g_count.append(nuc_dict["guanine"])
   c_count.append(nuc_dict["cytosine"])

   nuc_dict = {"adenine": 0, "thymine": 0, "guanine": 0, "cytosine": 0} #reset the values for next repetition

'''Returning output'''
print(f"""
A: {a_count}
T: {t_count}
G: {g_count}
C: {c_count}

Concatenated String: {cat_string}
""")

























