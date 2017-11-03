from sklearn.model_selection import train_test_split
from text_cleaner import TextCleaner

def save_input_file(name, X, y):
    """ Save input file for convert script.

        Args:
            name - name of the file { 'train', 'test', 'val' }
            X - training data
            y - labels
    """
    with open("data/imdb/aggregated/{0}.input.txt".format(name), 'w') as f:
        cleaner = TextCleaner()
        for i in range(len(X)):
            sentence = cleaner.clean_for_eval(X[i])
            label = y[i]
            f.write("{0}\t{1}\n".format(sentence, label))

if __name__ == "__main__":
    # load data
    data_path = "data/imdb/raw/"
    with open(data_path + "objective.txt", 'r') as f:
        objective = [ 
            unicode(s, errors='ignore').replace('.','').strip() for s in f.read().splitlines() ]
    with open(data_path + "subjective.txt", 'r') as f:
        subjective = [ 
            unicode(s, errors='ignore').replace('.','').strip() for s in f.read().splitlines() ]

    # create labels 
    objective_labels  = [ "objective"  for _ in range(5000) ]
    subjective_labels = [ "subjective" for _ in range(5000) ]

    # join data
    data = objective + subjective
    labels = objective_labels + subjective_labels

    # split data
    X_train, X_test, y_train, y_test = train_test_split(
        data, labels, test_size=0.20, random_state=42)
    X_train, X_val, y_train, y_val   = train_test_split(
        X_train, y_train, test_size=0.05, random_state=42)

    # save files
    save_input_file("train", X_train, y_train)
    save_input_file("test",  X_test,  y_test)
    save_input_file("val",   X_val,   y_val)