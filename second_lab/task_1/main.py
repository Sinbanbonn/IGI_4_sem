from our_functions import *
some_text = "One important issue that is 1  be1coming 1incre1asingly relevan  t1t in today's society is climate change. Climate change is a long-term shift in global or regional climate patterns, and it is primarily caused by human activity such as the burning of fossil fuels and deforestation. The consequences of climate change are far-reaching and can have a significant impact on the planet, including rising sea levels, more frequent and severe weather events, and the extinction of many plant and animal species."

print("sentence count is ", sent_count(some_text))
print("non-dec sentence count is ", non_dec_sent(some_text))
print("word count is ", word_search(some_text))

print("Average num of words is ", average_len(some_text))

print("Top n k is ", top_rep(some_text, 2 , 3 ))



