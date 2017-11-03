import csv
import random
from text_cleaner import TextCleaner

if __name__ == "__main__":
    # our datasets
    datasets = [
        'bbc',
        'fake',
        'cnn',
        'fox'
    ]
    data = []
    
    # process all the datasets
    for dataset in datasets:
        with open('data/{0}/aggregated/all.csv'.format(dataset), 'r') as df:
            _data = csv.reader(df, delimiter=',')
            for i,line in enumerate(_data):
                if i > 0:
                    _parsed = line[0]
                    data.extend(_parsed)
  
    # imdb
    data_path = 'data/imdb/'
    # objective
    with open(data_path + "objective.txt", 'r') as f:
        objective = unicode(f.read(), errors='ignore')
    # subjective
    with open(data_path + "subjective.txt", 'r') as f:
        subjective = unicode(f.read(), errors='ignore')
    
    # put all text together
    data = " ".join(data)
    data = data + objective + subjective
    data = data.replace('\n', ' ')
    
    # split and clean data
    cleaner = TextCleaner()
    data = cleaner.clean_for_dictionary(data)
    data = data.split()

    # turn into a set, add UNK for unseen words
    words = set([ word.strip() for word in data ])
    for a in cleaner.additional:
        words.add(a)
    words = list(words)
    words.append('UNK')
    words.sort()

    # write all the lines
    data_path = 'data/dictionary/'
    with open(data_path+"words.dictionary.txt", 'w') as f:
        for word in words:
            f.write("{0}\n".format(word))
    with open(data_path+"label.dictionary.txt", 'w') as f:
        labels = ["objective", "subjective", "other"]
        for l in labels:
            f.write("{0}\n".format(l))