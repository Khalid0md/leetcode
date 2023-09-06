def add_whitespace(words, line_char_limit):
    wordsArray = words.split()
    res = []
    string = []
    currentLength = 0
    
    for word in wordsArray:
        # Check if adding the current word to the current line exceeds the line length
        if currentLength + len(string) + len(word) <= line_char_limit:
            string.append(word)
            currentLength += len(word)
        else:
            res.append(' '.join(string))
            string = [word]
            currentLength = len(word)
        #balance the whitespaces
    
    if string:
        res.append(' '.join(string))
    
    for i in range(len(res)):
        if len(res[i]) < line_char_limit:
            res[i] += " " * (line_char_limit - len(res[i]))
    
    return res

print(add_whitespace("a cat is an animal", 6))