# 13. Write a program that reads a text and counts the frequency of each character (excluding
# spaces and special characters) using a dictionary.
d={}
def count_no_special(text):
    text=list(text)
    uique=set(list(text))
    for char in uique:
        if char.isalpha():
            d[char]=text.count(char)
count_no_special(input('Enter the text : '))
print(d)
