from collections import deque
import time

# This function will read the words file and store all of the words into a set to scan through later on
def readFile(file_name):
    word_list = set()
    with open(file_name) as word_file:
        for line in word_file:
            word_list.add(line.strip())
    return word_list

# This function finds a list of adjacent word to the current word that is poped out of the queue
def findAdjacent(current_word, word_list):
    adjacent_list = set()
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # We replace one word within the string with all of the alphabet character
    # Check new word (word after one character replacement) to see if it is in the words list
    # If it is, add it into the adjacent list
    for slice in range(len(current_word)):
        for replacement in alphabet:
            possible_adjacent = current_word[:slice] + replacement + current_word[slice+1:]
            if possible_adjacent in word_list and possible_adjacent != current_word:
                adjacent_list.add(possible_adjacent)

    #print(adjacent_list)
    return adjacent_list

def findLadder(start, end, word_list):
    # A set to keeping track of the visisted node so it won't be listed again
    visited_set = set()

    # Create a queue to pop the word sequence
    queue = deque([[start]])

    #print (queue)
    
    # while there is still element in queue
    while queue:
        # Pop a the first sequence 
        current_list = queue.popleft()
        current_word = current_list[-1]

        # When we reach the ending word
        if current_word == end:
            #print("The current list is", current_list)
            return current_list
        
        if current_word not in visited_set:
            visited_set.add(current_word)
            adjacent_words = findAdjacent(current_word, word_list)

            # Create new lists with adjacent words generated and add list(s) into the queue
            for word in adjacent_words:
                # Apend the adjacent word into the current list, which is just popped out of the queue
                updated_ladder = list(current_list)
                updated_ladder.append(word)

                # After get updated list with adjacent word appended, append the list into the queue
                queue.append(updated_ladder)
                #print(queue)
                #print()
    return None

# This function will receive the word file and the pair file to test the program out
# It also include time counter to test how long it takes to generate the word ladder
def testing(word_file_name, pair_file_name):
    # Clock starts
    start_time = time.perf_counter()

    # Read the file and generate the word set
    word_set = readFile(word_file_name)

    # Open file, for every line we have a pair of words as start and end word to find the word ladder
    with open(pair_file_name) as pair_file:
        for line in pair_file:
            pair = line.strip().split()
            start_word = pair[0]
            end_word = pair[1]
            if (len(start_word) == len(end_word)):
                # Call findLadder function and store the result
                result_ladder = findLadder(start_word, end_word, word_set)

                # Clock stop
                end_time = time.perf_counter()

                # Calculate the elapsed time
                elapsed_time = end_time - start_time

                # Print the result 
                print ("**Looking for ladder from ", start_word, " to ", end_word)
                if (result_ladder):
                    print("The ladder is: ", result_ladder)
                    print("Shortest length ladder is ", len(result_ladder))
                    print("Elapsed time: ", round(elapsed_time,1), " seconds")
                else:
                    print("No ladder found from ", start_word, " to ", end_word)
                    print("Elapsed time: ", round(elapsed_time,1), " seconds")
            else:
                print(start_word, " and ", end_word, " doesn't have the same lenth")
            print()
            


if __name__ == '__main__':
    word_file = "words.txt"
    pair_file = "pairs.txt"

    
    testing(word_file, pair_file)
    

    


    
    


        

