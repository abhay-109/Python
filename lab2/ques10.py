# 10. Write a Python function that accepts a sentence and returns a set of all unique vowels
# used.
def sentence(sen):
    vovel=['a','e','i','o','u']
    l_vovel=[i for i in sen if i in vovel ]
    return set(l_vovel)
result=sentence(input("Enter the sentence : "))
print(result)

    
