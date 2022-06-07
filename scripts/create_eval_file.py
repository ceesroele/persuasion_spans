"""
Utility to check correctness of evaluation method as compared to the SemEval-2021
reference method.

Create evaluation file based on test set and score it using the SemEval-2020 scorer
"""

import spacy
import json

TEST_DATA_FILE = 'assets/test_set_task2.txt'
TRAIN_DATA_FILE = 'assets/training_set_task2.txt'


def token_to_index(doc):
    """List of (start,end) tuples for all tokens in a doc (excluding trailing whitespace)"""
    lst = []
    cur = 0
    for t in doc:
        tlength = len(t.text)
        tlength_with_ws = len(t.text_with_ws)
        lst.append((cur, cur + tlength))
        cur += tlength_with_ws
    return lst


def span_start_end_multilabel(doc, spans_key='sc'):
    """Dictionary from span labels to of list of character indexes
    of every matching character in every span"""
    tok2index = token_to_index(doc)
    lst = []
    for span in doc.spans[spans_key]:
        start = tok2index[span.start][0]
        end = tok2index[span.end - 1][1]
        label = span.label_
        fragment = span.text
        lst.append((start, end, label, fragment))
    return lst


def read_data(fname: str):
    """Read and return all texts in the data file"""
    with open(fname, 'r') as f:
        lst = json.load(f)
        for rec in lst:
            r_id = rec['id']
            text = rec['text']
            yield r_id, text


def read_all_labels(fname: str) -> set:
    """Read and return set of all used labels in the data file"""
    labelset = set()
    with open(fname, 'r') as f:
        lst = json.load(f)
        for rec in lst:
            labels = rec['labels']
            for l in labels:
                labelset.add(l['technique'])
    return labelset


def main():
    #nlp = spacy.load('en_manipulation_detector')
    from evaluate_char import make_spancat_char_scorer
    nlp = spacy.load('./training/model-best')

    lst = []

    for r_id, text in read_data(TEST_DATA_FILE):
        doc = nlp(text)
        spans_list = span_start_end_multilabel(doc, spans_key='mnp')
        obj = {'id': r_id, 'text': text, 'labels': []}
        for start, end, label, fragment in spans_list:
            obj['labels'].append(
                {'start': start, 'end': end, 'technique': label, 'text_fragment': fragment}
            )
        lst.append(obj)

    with open('prediction.json', 'w') as f:
        json.dump(lst, f, indent=4)

    with open('labels.lst', 'w') as f:
        for l in read_all_labels(TRAIN_DATA_FILE):
            f.write(f'{l}\n')


if __name__ == '__main__':
    main()
