import nltk
import csv
import random
import os

""" Processes dataset for MTURK tasks.
"""
class ProcessDataset():
    def __init__(self):
        pass

    def aggregate(self, dataset_path, categories, uml):
        """ Process bbc dataset to create amassed train, val, 
            and test data files.

            Args:
                dataset_path - the path to the raw data.
                categories - list of subfolders
                uml - whether or not to parse for <TEXT> tags
        """
        all_sentences = []

        for c in categories:
            # tokenize all files for a category
            sent = self.tokenize_category(dataset_path, c, uml)
            all_sentences.extend(sent)

        columns = [
            'sentence',
            'category',
            'file_name',
            'index'
        ]

        # write all the sentences to the same place.
        with open('data/{0}/aggregated/all.csv'.format(dataset_path), 'w') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(columns)
            writer.writerows(all_sentences)

    def get_file_list(self, category):
        """ Lists all files in the sub-folder for a category. """
        return os.listdir(category)

    def tokenize_category(self, dataset_path, category, uml):
        """ Tokenize all files in a category (into sentences).

            Args: 
                dataset_path - the path to the raw data.
                category - the type of article (maps to a subfolder.)

            Returns:
                the list of sentences from all the files in a category
        """
        file_names = self.get_file_list("data/{0}/raw/{1}/".format(dataset_path, category))
        out = []
        for fn in file_names:
            if uml:
                with open("data/{0}/raw/{1}/{2}".format(dataset_path, category, fn), 'r') as df:
                    text = df.read()
                    if '<TEXT>' in text:
                        text = text.split('<TEXT>')[1].split('</TEXT>')[0]
                    else:
                        print fn
                    sent = nltk.sent_tokenize(
                        unicode(text, errors='ignore').replace('\n', ' ').replace(',','^'))
                    out.extend([[s, category, fn, i ] for i,s in enumerate(sent)])
            else:
                with open("data/{0}/raw/{1}/{2}".format(dataset_path, category, fn), 'r') as df:
                    sent = nltk.sent_tokenize(unicode(df.read(), errors='ignore').replace('\n', ' ').replace(',','^'))
                    out.extend([[ s, category, fn, i ] for i,s in enumerate(sent)])
        return out

if __name__ == "__main__":
    configs = [
        {
            "dataset_path": "bbc",
            "categories": [
                'business',
                'entertainment',
                'politics',
                'sport',
                'tech'
            ],
            "uml": False
        }, {
            "dataset_path": "fake",
            "categories": [
                'buzzfeedfake',
                'randomfake',
                'randomsatire'
            ],
            "uml": False
        }, {
            "dataset_path": "cnn",
            "categories": [
                'cnn_crime',
                'cnn_entertainment',
                'cnn_health',
                'cnn_living',
                'cnn_politics',
                'cnn_technology',
                'cnn_travel'
            ],
            "uml": True
        }, {
            "dataset_path": "fox",
            "categories": [
                'foxnews_health',
                'foxnews_science_technology',
                'foxnews_sports',
                'foxnews_travel'
            ],
            "uml": True
        }
    ]

    process = ProcessDataset()
    for config in configs:
        process.aggregate(config['dataset_path'], config['categories'], config['uml'])