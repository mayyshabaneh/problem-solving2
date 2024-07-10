def word_break(s, word_dict):
    new_word = ""
    for i in range(len(s)):
        new_word += s[i]
        if new_word in word_dict:
            pass
        else:
            return False
    return True

print(word_break("applepenapple", ["apple", "pen"]))
