import pandas as pd
import numpy as np

def load_data(filepath, column_names):
    """
    Load CSV data into a DataFrame.
    
    Args:
        filepath (str): The path to the CSV file to load.
        
    Returns:
        pd.DataFrame: A DataFrame containing the loaded data.
    """
    return pd.read_csv(filepath, header=0, names=column_names)

def calculate_max_length(df):
    """
    Determine the maximum length of sequences in a DataFrame column.
    
    Args:
        df (pd.DataFrame): DataFrame containing a column 'sequence' with sequence data.
        
    Returns:
        int: The maximum length of any sequence in the DataFrame.
    """
    return df['sequence'].str.len().max()

def one_hot_encoding(sequence, max_length, amino_dict):
    """
    Generate a one-hot encoded numpy array for a sequence.
    
    Args:
        sequence (str): The sequence to encode.
        max_length (int): The maximum length to which the sequence should be padded.
        amino_dict (dict): Dictionary mapping amino acids to their respective indices.
    
    Returns:
        np.ndarray: A flattened one-hot encoded array of the sequence.
    """
    base = ['X'] * max_length
    for index, ch in enumerate(sequence):
        base[index] = ch
    padded_sequence=''.join(base)

    encoded = np.zeros((max_length,len(amino_dict)),dtype=int)
    for id, ch in enumerate(padded_sequence):
        if id < max_length and ch in amino_dict:
            encoded[id,amino_dict[ch]]=1
    return encoded

def letter_composition(sequence, amino_dict):
    """
    Calculate the amino acid composition of a sequence.
    
    Args:
        sequence (str): The sequence from which to calculate composition.
        amino_dict (dict): Dictionary mapping amino acids to indices.
    
    Returns:
        np.ndarray: An array representing the frequency of each amino acid in the sequence.
    """
    comp_array = np.zeros(len(amino_dict), dtype=int)
    for char in sequence:
        if char in amino_dict:
            comp_array[amino_dict[char]] += 1
    return np.round(comp_array / len(sequence),decimals=3) if len(sequence) > 0 else comp_array


def process_sequences(filepath):
    """
    Process sequences from a CSV file to extract features and return them as a DataFrame.
    
    Args:
        filepath (str): Path to the CSV file containing sequences.
        
    Returns:
        pd.DataFrame: DataFrame with original sequences and their extracted features.
    """
    column_names = ['id', 'sequence']
    df = load_data(filepath,column_names)
    amino_acids = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y', 'X']
    amino_dict = {aa: idx for idx, aa in enumerate(amino_acids)}
    max_length = calculate_max_length(df)

    df['one_hot'] = df['sequence'].apply(lambda seq: one_hot_encoding(seq, max_length, amino_dict))
    df['letter_composition'] = df['sequence'].apply(lambda seq: letter_composition(seq, amino_dict))

    return df

def main(filepath):
    """Main function to process sequences from a file and return features."""
    return process_sequences(filepath)

if __name__ == '__main__':
    result_df = main('uniprot_sequences.csv')
    print(result_df.head())


