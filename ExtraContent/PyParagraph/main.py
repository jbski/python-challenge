import csv
import os
import re

# Determine the file path to read
txtfile = "raw_data/paragraph_1.txt"


# Open the text file for reading
with open(txtfile, 'r') as text:

    lines = text.read()
    
    # Split the paragraph into words using a space as a delimiter
    words = re.split(" ", lines)
    
    # Initialize a variable and count the number of letters in the paragraph - ignore spaces.
    num_letters = 0
    for line in lines:
        if line != " ":
            num_letters += 1

    # Initialize a variable and count the number of words in the paragraph
    numwords = 0
    for word in words:
       numwords += 1
    
    # Split the paragraph into sentences using the characters in the reg. expression as a delimiter
    sentence = re.split("(?<=[.!?]) +", lines)

    # Determin the total number of sentences
    num_sentences = (len(sentence))

    # Calculate the average number of words per sentence
    if num_sentences == 0:
        num_words_sentence = 0
    else:
        num_words_sentence = numwords / num_sentences

    # Determine the average number of letters per word
    num_letters_word = num_letters / numwords

    # Print the paragraph analysis results to the terminal
    print("\nParagraph Analysis")
    print("--------------------------------")
    print(f'Approximate Word Count:  {numwords}')
    print(f'Approximate Sentence Count: {num_sentences}')
    print(f'Average Letter Count per word: {num_letters_word:.2}' )
    print(f'Average Sentence Length: {num_words_sentence}\n')

   
    # Create a new file to write the paragraph output to
    output_file = open("data_output/paragraph_analysis_output.txt", "w")

    # Write the paragraph analysis results to a text file
    output_file.write(f'Paragraph Analysis\n')
    output_file.write(f"--------------------------------\n")
    output_file.write(f'Approximate Word Count:  {numwords}\n')
    output_file.write(f'Approximate Sentence Count: {num_sentences}\n')
    output_file.write(f'Average Letter Count per word: {num_letters_word:.2}\n')
    output_file.write(f'Average Sentence Length: {num_words_sentence}\n')

    output_file.close()
    

    


    




