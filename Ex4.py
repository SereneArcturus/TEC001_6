def word_frequency(text): 
    words = text.lower().split()  
    total_words = len(words)  
    counts = {} 
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    sorted_words = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:5]
    top_5 = dict(sorted_words)
    sum_top_5 = sum(top_5.values())
    proportion = (sum_top_5 / total_words) * 100

    print("Top 5:", top_5)
    print("Total words:", total_words)
    print("Proportion of 5 most common words:", sum_top_5, "/", total_words, "=", round(proportion, 2), "%")
text_input = input("Type your text you want here to count and analyze: ")
word_frequency(text_input)