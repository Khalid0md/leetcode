import re

def filterBadwords(bad_words, message):
    def replace_bad_words(match):
        word = match.group(0)
        return '*' * len(word)

    # Prepare the list of bad words
    bad_word_list = bad_words.lower().split()

    # Create a regex pattern for matching bad words with wildcards
    pattern_parts = []
    for word in bad_word_list:
        if '*' in word:
            regex_word = re.escape(word).replace(r'\*', r'\w*').replace(r'\?', r'\w?')
            pattern_parts.append('(?i)' + regex_word)
        else:
            pattern_parts.append('(?i)\\b' + re.escape(word) + r'\\b')
    pattern = '|'.join(pattern_parts)

    # Replace bad words in the message
    filtered_message = re.sub(pattern, replace_bad_words, message)

    return filtered_message

# Test cases
bad_words = "lame jerk dummy bollocks crikey"
message1 = "Jerk, I wasn't going to do that. Crikey!"
result1 = filterBadwords(bad_words, message1)
print(result1)