import nltk
from nltk.corpus import brown
from nltk.tokenize import word_tokenize
import sys
import pandas as pd
from matplotlib import pyplot as plt


'''
Pre: Takes in a filename.
Post: Checks and returns string component.
'''
def get_data(file_name):
    try:
        f = open(file_name,'r')
    except: 
        print('could not find file')
    return f.read()


'''
Pre: Takes in a string.
Post: Returns list tokenized by nltk.
'''
def nltk_tokenizer(text):
    return word_tokenize(text)


'''
Pre: Takes in a list.
Post: Returns dictionary of words:frequency.
'''
def get_frequencies(tab):
    dct = {}
    for word in tab:
        if word in dct:
            dct[word]=dct[word]+1
        else:
            dct[word]= 1
    return dct


'''
Pre: Takes in a dictionary.
Post: Creates and prints to a .csv file using '~' as separator.
'''
def make_file(dct,filename):
    f = open(filename+'.csv','w+' )
    for word in dct: f.write(word+ ' '+ str(dct[word])+'\n')


'''
Pre: Takes in a .csv file.
Post: Dislpays the log-log plot associated with .csv file.
'''     
def display(file_name):
    fil = pd.read_csv(file_name,sep=' ',names=['words','frequencies'], engine='python')
    fil.sort_values(by='frequencies',ascending=False, inplace=True)
    fil.reset_index(inplace=True)
    fil.index += 1
    plt.loglog(fil.index,fil['frequencies'])
    plt.title(file_name + ' Graph')
    plt.xlabel('Rank')
    plt.ylabel('Frequency')
    plt.show()


'''
Pre: NLTK is downloaded.
Post: Brown corpus is returned as a string.
'''
def get_brown():
    nltk.download('brown')
    lst = brown.words()
    return lst[:10000]



def example():
    lst = get_brown()
    dct = get_frequencies(lst)
    make_file(dct,'brown_example')
    display('brown_example.csv')



def create_display():
    filename = input('File name: ')
    display(filename)



def make_csv_only():
    filename = input('File name: ')
    text = get_data(filename)
    lst = nltk_tokenizer(text)
    dct = get_frequencies(lst)
    make_file(dct,filename)



def main():
    command = sys.argv[1]
    if command == 'example':
        example()
    elif command == 'create':
        create_display()
    elif command == 'csv':
        make_csv_only()


main()
