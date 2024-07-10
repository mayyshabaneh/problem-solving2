def word_break(s, word_dict):
    new_word = None
    for i in range (len(s)):
        new_word += s[i]
        if new_word in word_dict:
            return True
    return False
print(word_break("applepenapple",["apple","pen"]))