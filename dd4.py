def length(path): 
    n = 0 #Creates a counter 
    fin = open(path)
    for line in fin: 
        n += 1 #Adds to the counter for each line
    return n

def count(path):
    counts = []
    fin = open(path)
    for line in fin:
        counts += [len(line)]
    return counts

import random

def random_int(maximum):
    ans = []
    for i in range(maximum): #Loops for each number in the given range 
        n = random.randint(1, 100)
        while len(ans) < 100:
            n = random.randint(1,100) #Gets a random number between 1 and 100 
            ans += [int(n)]
    return ans

def get_lines(path, lst):
    ans = []
    with open(path, "w") as f:
        for i in lst: #Loops for each of the random numbers
            for line in range(i): #Loops for each line corresponding to the random numbers
                a = f.readline() #Reads each line 
                ans += [(a.strip())] #Removes blank space
    return ans 

def count_frequency(lst):
    counts = [0]*26 #Makes 26 spaces in a list for each letter of the alphabet 
    for i in lst: #Loops for each item in the list
        for ch in i: #Loops for each letter in the list 
            if ord(ch) in range(ord("A"), ord("Z")): #Checks if the letter is in uppercase
                counts[(ord(ch) - ord("A"))] += 1 #Adds to its respective column
            elif ord(ch) in range(ord("a"), ord("z")): #Checks if the letter is in lowercase
                counts[(ord(ch) - ord("a"))] += 1 #Adds to its respective column
    return counts

def make_histogram(path, lst):
    i = 0 
    with open(path, "w") as f: #Opens file
        for i in range(26):
            f.write(lst[i]*chr(i + ord("a")) + "\n") #Multiplies the string by number of occurences 
            i += 1 #Moves on to next letter

def random_word_table(path, maximum):
    with open("random_words.txt", "w") as f:
        for i in get_lines(path, random_int(maximum)):
            f.write("{0}{1}{2}".format(" "*(len("Random number") - len(random_int(maximum))), random_int(maximum), i) + "\n") #Writes in format

def count_frequency_table(path, maximum):
    with open("letter_count.txt", "w") as f:
        for i in range(26):
            f.write("{0}{1}{2}".format(i + ord("a"), " "*(len("etter count") - len(count_frequency(get_lines(path, random_int(maximum))))), (count_frequency(get_lines(path, random_int(maximum)))))) #Writes in format 

def main():
    path = raw_input("Please select a file.\n") #File input 
    badFile = True
    while badFile: #Makes sure input is valid
        try: #Tries opening file 
            f = open(path)
            f.close()
            badFile = False
        except IOError:
            print "This file cannot be found. Please try again."
            path = raw_input()
    print "There are {0} lines in your selected file.".format(length(path)) #Finds length of file
    maximum = int(raw_input("What lines would you like to use for your new file?\n")) 
    if maximum <= 0: #Makes sure line is in the file
        print "Please enter a valid input.\n"
        int(raw_input())
    elif maximum > len(path):
        print "Please enter a valid input. \n"
        int(raw_input()) 
    random_word_table(path, maximum) #Writes in format 
    print "Your list of random words has been generated in random_words.txt, sorted by their line number in the input file."
    count_frequency_table(path, maximum) #Writes in format 
    print "The number of occurences of each letter is recorded in letter.count.txt."
    make_histogram("histogram.txt", count_frequency(get_lines(path, random_int(maximum)))) #Makes histogram for letter frequency in random_words.txt
    print "A histogram of the occurences of each letter was made in histogram.txt"

main() 
        
    
