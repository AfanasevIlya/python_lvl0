def find_step(word):
    count = 0
    for c in word:
        if c.isalpha():
            count += 1
    return count


def caesar_pepper(msg):
    low_al = 'abcdefghijklmnopqrstuvwxyz'
    up_al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alph_len = 26
    lst = msg.split()
    res_lst = list()
    for word in lst:
        res_word = ''
        step = find_step(word)
        for c in range(len(word)):
            if word[c].isalpha():
                if word[c] == word[c].lower():
                    start_index = low_al.index(word[c])
                    final_index = (start_index + step) % alph_len
                    res_word += low_al[final_index]
                else:
                    start_index = up_al.index(word[c])
                    final_index = (start_index + step) % alph_len
                    res_word += up_al[final_index]
            else:
                res_word += word[c]
        res_lst.append(res_word)
    return ' '.join(res_lst)


msg = input()
print(caesar_pepper(msg))
