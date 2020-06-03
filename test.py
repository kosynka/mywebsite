import operator

def zen_words(n):
    zen_text = """Beautiful is better than ugly.     
    Explicit is better than implicit.  
    Simple is better than complex.     
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
    """

    zen_map = dict()

    for word in zen_text.split():
        cleaned_word = word.strip('.,!-').lower()
        if cleaned_word not in zen_map:
            zen_map[cleaned_word] = 0
        
        zen_map[cleaned_word] += 1

    zen_items = zen_map.items()
    word_count_items = sorted(
        zen_items, key=operator.itemgetter(1), reverse=True
    )
    
    return word_count_items[:n]

# print(zen_words(5))
