import argparse
import string

import numpy as np


def main(documentsTxt):
    doc_list = []
    documents = documentsTxt.split('\n')
    rows = len(documents)
    for i in range(rows):
        doc_list = doc_list + documents[i].split(' ')
        documents[i] = documents[i].split(' ')

    doc_set = set()
    for word in doc_list:
        word = word.lower()
        doc_set.add(word)

    cols = len(doc_set)
    doc_set = sorted(doc_set)
    feature_matrix = np.zeros([rows, cols])
    for j in range(rows):
        for k in range(len(documents[j])):
            for l in range(cols):
                if documents[j][k].lower() == doc_set[l]:
                    feature_matrix[j][l] += 1

    print('# Features:', '\n', feature_matrix)
    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser("One Hot Encoder")
    parser.add_argument("--fpath", type=str, help="Name of the txt file to be read in")
    args = parser.parse_args()
    main(open(args.fpath).read())