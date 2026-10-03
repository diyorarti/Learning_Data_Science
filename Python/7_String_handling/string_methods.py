"""
String Methods: split(), join(), replace()
"""

# split() 
text = "apple banana mango"
words = text.split(",")
# for w in words:
#     print(w)
# print(words)
# print(type(words))

# join()
words1 = ['Hi', 'Everyone', 'Eid', 'Muborak!']
text1 = " ".join(words1)
#print(text1)

# replace()
text3 = "Hello World!"
#print(text3)
text4 = text3.replace("World", "Python")
#print(text4)

hi = "hi everyone"
#print(hi)
hi.replace('h', 'H') # unchanged / not saved the result
#print(hi)
hi1 = hi.replace('h', 'H')
#print(hi1)


text_space = "  hi,  everyone, how are        yoou doing?"
words = text_space.split(',')
clean_text = " ".join(words)
print(clean_text)