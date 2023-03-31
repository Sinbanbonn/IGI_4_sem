import re
import constants

some_text = "One important issue that is 1  be1coming 1incre1asingly relevan  t1t in today's society is climate change. Climate change is a long-term shift in global or regional climate patterns, and it is primarily caused by human activity such as the burning of fossil fuels and deforestation. The consequences of climate change are far-reaching and can have a significant impact on the planet, including rising sea levels, more frequent and severe weather events, and the extinction of many plant and animal species."
def sent_count(text):
    #counter = re.findall(constants.for_sent_count, text)
    new_text = re.sub(constants.abb, lambda m: m.group(0).replace('.', '|'), text)
    sentences = re.split(constants.for_sent_count, new_text)
    return len(sentences)



def non_dec_sent(text):
    counter = re.findall(constants.for_non_dec, text)
    return len(counter)

def word_search(text):
    counter = len(re.findall(constants.word_reg, text))
    numbers = len(re.findall(constants.numb_reg, text))
    return counter - numbers

def average_len(text):
    counter = re.findall(constants.word_reg, text)
    numbers = re.findall(constants.numb_reg, text)

    gen_count = 0
    numb_count = 0

    for value in counter:
        gen_count += len(value)

    for value in numbers:
        numb_count += len(value)

    value = (gen_count - numb_count)/word_search(text)
    return value

def top_rep(text, n, k):
    words = re.findall(constants.for_n_k, text.lower())
    n_grams = [' '.join(words[i:i+n]) for i in range(len(words)-n+1)]
    my_dict = {}
    answer = []

    for value in n_grams:
        if value in my_dict:
            my_dict[value] += 1
        else:
            my_dict[value] = 1

    for key, value in my_dict.items():
        if value >= k:
            answer.append(key)

    return answer






print(top_rep(some_text , 2,2))