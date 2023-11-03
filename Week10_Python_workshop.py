### This is an introductory workshop for Python coding
### Please see Gee's Github for more Python workshop materials: https://github.com/Gee-CityU 

# 1. Print function 
#print ("Hello World!")
#print ("Hellow Word!", "What's up?")

'''
Excercise-1: Use print function to show the sentence "I really like Gee's teaching."
'''

# 2. Variable
#x = "Hello Word!"
#print (x)
#y = 1
#print(y)

'''
Excercise-2: Store the sentence "I really like Gee's teaching." in the variable n,
             Use print function to show what is sroted in the variable n
'''

# 3. Variable types
#x = "Hello Word!"
#print (type (x))
#y = 1
#print (type (y))
#print (x,y)
#print("the property of x is:" ,type(x))
#print("the property of y is:" ,type(y))

'''
Excercise-3: Use the print and type function to explore what type of variable is n:
             n = "123"
'''

# 4. Tokenizer-1
#sentence = "Is Gee the best teacher?"
#print(sentence)
#words = sentence.split(" ")
#print(words)

# 5. Tokenizer-2
#sentence = "Is Gee the best teacher?"
#print(sentence)
#sentence_new = sentence.replace("?", "")
#print(sentence_new)
#words = sentence_new.split(" ")
#print(words)

'''
Excercise-4: Tokenize the sentence "Gee is the best teacher in the world." without punctuation
'''

# 5. Tokenizer-3
#sentence = "Is Gee the best teacher?"
#print(sentence)
#sentence_2 = sentence.replace("?", " ?")
#print(sentence_new)
#words = sentence_2.split(" ")
#print(words)

'''
Excercise-5: Tokenize the sentence "Gee is the best teacher, and we are the best students."

See the answer below
             
#sentence = "Gee is the best teacher, and we are the best students."
#print(sentence)
#sentence_2 = sentence.replace(".", " .")
#print(sentence_2)
#sentence_3 = sentence_2.replace(",", " ,")
#print(sentence_3)
#words = sentence_3.split(" ")
#print(words)
'''

# 6. Build a Tokenizer for research use in the future!
#def tokenizer(S):
    #sentence_0 = S.replace(".", "")
    #sentence_1 = sentence_0.replace(",", "")
    #sentence_2 = sentence_1.replace("?", "")
    #sentence_3 = sentence_2.replace(":", "")
    #sentence_4 = sentence_3.replace(";", "")
    #sentence_5 = sentence_4.replace("!", "")
    #sentence_6 = sentence_5.replace("~", "")
    #words = sentence_6.split(" ")
    #return (words)

#sentence = "I love CityU; However, the university is far from my home. Today I got COVID19! Yeah~"
#words = tokenizer(sentence)
#print(words)

'''
Excercise-6: Use your tokenizer to tokenize the sample. Observe the results and see how to improe your tokenizer
'''

# 7. upgrade tokenizer-2 print words one by one 

#def tokenizer(S):
    #sentence_0 = S.replace(".", "")
    #sentence_1 = sentence_0.replace(",", "")
    #sentence_2 = sentence_1.replace("?", "")
    #sentence_3 = sentence_2.replace(":", "")
    #sentence_4 = sentence_3.replace(";", "")
    #sentence_5 = sentence_4.replace("!", "")
    #sentence_6 = sentence_5.replace("~", "")
    #words = sentence_6.split(" ")
    #for word in words:
        #print(word)

#sentence = "I love CityU; However, the university is far from my home. Today I got COVID19! Yeah~"
#tokenizer(sentence)


# 8. Extension: Build a Counter for research use in the future
'''
def counter(S):
    wordcount = 0
    sentence_0 = S.replace(".", "")
    sentence_1 = sentence_0.replace(",", "")
    sentence_2 = sentence_1.replace("?", "")
    sentence_3 = sentence_2.replace(":", "")
    sentence_4 = sentence_3.replace(";", "")
    sentence_5 = sentence_4.replace("!", "")
    sentence_6 = sentence_5.replace("~", "")
    words = sentence_6.split(" ")
    for word in words:
        wordcount = wordcount + 1
    return(wordcount)

sentence = "I love CityU; However, the university is far from my home. Today I got COVID19! Yeah~"
print(counter(sentence))
'''


