#what  are the time complexitiesfor sorting?
from operator import itemgetter, attrgetter
strs = ["eat","tea","tan", "bcr", "ate","nat","bat", "bar"]

#This is how  strings should be sorted in python
#This is how s
result = list()
for word in strs:
    sorted_word = sorted(word)
    print(sorted_word)
    ''.join(sorted_word)
    result.append(word)
print(result)

#this will sort a list lexicographically,all the way to  the final character in a string
sr = sorted(result)
print(sr)

#both sorted() and .sort() take in a key that specifies a function or other callable 
#to be called on each list element prior to making comparisons

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
print(sorted(student_tuples, key=lambda student: student[2]))

#both sorted(0) and .sort() accept a reverse parameter with a boolean value
#this is used to flag  descending sorts
sorted(student_tuples, key=lambda student: student[2], reverse=True)

#aside:python lambdas, small anonymous functions
#lambda arguments : expression
x = lambda a : a + 10

#The operator module has itemgetter(), attrgetter(), and a methodcaller() function.
#these make things faster
#allows for multiple levels of sorting, for  example sort by grade then by age, perfect! like a java comparator
sorted(student_tuples, key=itemgetter(1,2))

print(list(reversed("Khalid")))