# Opening the  Book
with open("books/frankenstein.txt") as f:
    file_contents = f.read()

# Word counting
def word_count(file_contents):
    counter = 0
    for x in file_contents.split():
        counter += 1
    return(counter)

# Counting the number of Words
def letters_count(file_contents):
    letters = {}
    lower_file_contents = file_contents.lower()
    for l in lower_file_contents:
        if l.isalpha():
            if l in letters:
                letters[l] += 1
            else:
                letters[l] = 1
    letters_list = list(letters.items())
    letters_list.sort(key=lambda item: item[1], reverse=True)
    
    
    print("---Begin report of books/frankenstein.txt---")
    print(f"{word_count(file_contents)} words found in the document")
    for c in letters_list: 
        print(f"The {c} character was found {letters.get(c)} times")


        
letters_count(file_contents) 
        
            
         
            
    
        