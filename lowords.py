word_list=input("enter a list of words(comma-seperated):").split(',')
long_len=0
for word in word_list:
    word=word.strip()
    curr_len = len(word)
    if curr_len > long_len:
        long_len = curr_len
        long_word = word
print(f"the longest word:'{long_word}'with length{long_len}")
