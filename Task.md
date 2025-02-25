# Abcam AI Engineer

We would like to ask you to do Python coding task, to be presented during the interview. We
expect you to take 10 minutes to talk through your solution to the task, after which we will
spend about 20 minutes asking questions.

Please note the following:

* We suggest you take a maximum of 2 hours working on this task. During the interview, you
  can explain what you would do if you had more time.
* Your code doesn’t necessarily need to run or be entirely complete; we are primarily looking for
  evidence of good software design principles and development practices, as well as scalability,
  extensibility etc.
* Your code should be configured such that it can be readily packaged / installed.
* We are looking for proficiency with commonly used Python data science libraries (pandas, numpy,
  scikit-learn, etc.), so please make use of these libraries where applicable even if implementable
  without them.

## Coding Task

### 1. Coding

#### The Brief

You are being given a CSV file containing sequence data extracted from UniProt named
‘uniprot_sequences.csv’. We ask that you use Python to extract a series of features from the
sequence data and present it in a performant data structure. You are allowed (and encouraged) to
use the following Python libraries as well as anything from the Python standard library: pandas,
numpy, and scikit-learn.

#### Details

The provided csv file contains around 1,000 entries (or rows). Each row has a unique identifier and
a sequence of letters. Note the sequence of letters is in fact an amino acid sequence, and each row
corresponds to a protein, but this biological context is not relevant for this exercise – you can
just think of the data as a couple of identifiers, each associated with a string of letters.

The letters are drawn from the following list (with each letter corresponding to a different amino
acid):

``` 
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y', 'X'] 
```

When considering ordered features, such as one-hot encodings, use the above order. Note that the
character ‘X’ indicates a missing or ambiguous amino acid in the sequence.

Your task is to extract two features from each sequence and return a data structure that includes
the listed features for all of the sequences given in ‘uniprot_sequences.csv’.

Expected features for each sequence:

* *One Hot Encoded Letter Vector* - Each letter in the sequence is encoded as a 21-length one-hot
  encoded vector resulting in a vector of length L * 21, where L is the length of the longest
  sequence in the file. As an example, the amino acid ‘C’ (cysteine) can be encoded as the
  vector [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0].
  Vectors of this feature should be the same length for all sequences, so for sequences shorter
  than the longest sequence in the set, pad the end of the sequence with the one-hot encoding of
  ‘X’ until it is of the same length as the longest.
* *Letter Composition* - The letter composition as a 21-length vector.
  Your result should be a 21-length vector where each position describes the frequency of a letter
  in the sequence. Each position (based on the above array) would be the resulting value of An / A
  where An is the count of the letter in position n and A is the total number of letters in the
  sequence. For example, the sequence ‘ADHAIPNNAP’ would result in an AAC vector
  of [0.3, 0, 0.1, 0, 0, 0, 0.1, 0.1, 0, 0, 0, 0.2, 0.2, 0, 0, 0, 0, 0, 0, 0, 0].

Your code must show evidence of good documentation following the Google Python style guide with
docstrings and in-code comments where appropriate.
Please include a test suite using the testing library of your choice.

#### Summary

Your final deliverable will be the Python files containing your code.
You do not need to include output of the program containing the features for the sequences, but
there should be a single function call that will return the data structure containing all features
for all sequences. 
