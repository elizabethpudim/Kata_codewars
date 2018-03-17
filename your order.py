def find_number(word):
    index = 0
    if word[index].isdigit():
        return int(word[index])
    return find_number(word[index + 1:])


def order(sentence):
    return " ".join(sorted(sentence.split(), key=find_number))