# Однокоренные
def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if ((str(*root_word).lower() in i.lower())
                or (i.lower() in str(*root_word).lower())):
            same_words.append(i)
    return(same_words)

word1 = ['rich']
words1 = ['richiest', 'orichalcum', 'cheers', 'richies']
word2 = ['Disablement']
words2 = ['Able', 'Mable', 'Disable', 'Bagel']

print(f'Исходный код:\nresult1 = single_root_words{word1+words1}')
print(f'result2 = single_root_words{word2+words2}')

result1 = single_root_words(word1, *words1)
result2 = single_root_words(word2, *words2)
print(f'\nВывод на консоль:\nresult1 = {result1}')
print(f'result2 = {result2}')