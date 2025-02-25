import unittest
import pandas as pd
import numpy as np
import os
import tempfile

import main as sp

class TestSequenceProcessor(unittest.TestCase):
    """
    A comprehensive test suite for the sequence processor module.
    
    This test suite validates the functionality of all key functions in the sequence processor,
    including data loading, sequence analysis, encoding, and the full data processing workflow.
    Tests cover both normal operation scenarios and edge cases to ensure robustness.
    """
    
    def setUp(self):
        """
        Set up the test environment before each test.
        
        This method:
        1. Creates a standard amino acid dictionary for testing encoding functions
        2. Generates a temporary CSV file with test sequence data
        3. Prepares the test environment for consistent and isolated test execution
        """
        # Standard amino acid dictionary
        self.amino_acids = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 
                           'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y', 'X']
        self.amino_dict = {aa: idx for idx, aa in enumerate(self.amino_acids)}
        
        # Create a simple test CSV file
        self.test_data = """id,sequence
1,ACDEFG
2,MNPQRS
3,TVWY
"""
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.csv')
        self.temp_file.write(self.test_data)
        self.temp_file.close()
        
    def tearDown(self):
        """
        Clean up the test environment after each test.
        
        This method removes any temporary files created during testing to prevent
        file system pollution and ensure test isolation.
        """
        os.unlink(self.temp_file.name)
    
    def test_load_data(self):
        """
        Test the load_data function for proper CSV parsing.
        
        This test validates that:
        1. The function correctly reads a CSV file into a pandas DataFrame
        2. The resulting DataFrame contains the expected data with proper column names
        3. The data types and values match expectations
        """
        column_names = ['id', 'sequence']
        result = sp.load_data(self.temp_file.name, column_names)
        
        expected_df = pd.DataFrame({
            'id': [1, 2, 3],
            'sequence': ['ACDEFG', 'MNPQRS', 'TVWY']
        })
        
        pd.testing.assert_frame_equal(result, expected_df)
    
    def test_calculate_max_length(self):
        """
        Test the calculate_max_length function for correct sequence length calculation.
        
        This test ensures that:
        1. The function correctly identifies the maximum sequence length in a DataFrame
        2. It returns the expected integer value representing the longest sequence
        """
        test_df = pd.DataFrame({
            'sequence': ['ABC', 'DEFGH', 'IJ']
        })
        result = sp.calculate_max_length(test_df)
        self.assertEqual(result, 5)
    
    def test_one_hot_encoding(self):
        """
        Test the one_hot_encoding function for proper sequence encoding.
        
        This test validates that:
        1. Sequences are correctly encoded into one-hot numeric representation
        2. The function properly handles padding with 'X' characters
        3. The resulting array has the expected shape and values
        4. Edge cases like empty sequences are handled appropriately
        
        The test examines both normal sequences and the empty sequence edge case.
        """
        # Test normal case
        sequence = "ACK"
        max_length = 5
        result = sp.one_hot_encoding(sequence, max_length, self.amino_dict)
    
        # Check dimensions
        self.assertEqual(result.shape, (max_length, len(self.amino_dict)))
    
        # Expected result: A (index 0), C (index 1), K (index 8) are encoded, rest are X (index 20)
        expected = np.zeros((max_length, len(self.amino_dict)), dtype=int)
        expected[0, 0] = 1  # A
        expected[1, 1] = 1  # C
        expected[2, 8] = 1  # K
        expected[3, 20] = 1  # X (padding)
        expected[4, 20] = 1  # X (padding)
    
        np.testing.assert_array_equal(result, expected)
    
        # Test empty sequence
        sequence = ""
        max_length = 3
        result = sp.one_hot_encoding(sequence, max_length, self.amino_dict)
    
        # Expected result: all X (index 20)
        expected = np.zeros((max_length, len(self.amino_dict)), dtype=int)
        expected[0, 20] = 1
        expected[1, 20] = 1
        expected[2, 20] = 1
    
        np.testing.assert_array_equal(result, expected)
        
    
    def test_letter_composition(self):
        """
        Test the letter_composition function for accurate amino acid frequency calculation.
        
        This test verifies that:
        1. The function correctly calculates the frequency of each amino acid in a sequence
        2. The resulting proportions sum to 1.0 for normal sequences
        """
        # Test normal case
        sequence = "AAACDE"
        result = sp.letter_composition(sequence, self.amino_dict)
        
        # Expected frequencies
        expected = np.zeros(len(self.amino_dict))
        expected[0] = 0.5     # A: 3/6
        expected[1] = 0.167   # C: 1/6
        expected[2] = 0.167   # D: 1/6
        expected[3] = 0.167   # E: 1/6
        
        np.testing.assert_almost_equal(result, expected, decimal=3)
        
        # Test empty sequence
        empty_result = sp.letter_composition("", self.amino_dict)
        self.assertEqual(sum(empty_result), 0)
    
    def test_full_workflow(self):
        """
        Test the complete process_sequences workflow as an integration test.
        
        This test validates that:
        1. The end-to-end processing pipeline works correctly
        2. The resulting DataFrame contains all expected columns
        3. The one-hot encoded arrays have the correct dimensions based on max sequence length
        4. All sequences in the input file are properly processed
        
        This test ensures that all components work together as expected in the full pipeline.
        """
        result_df = sp.process_sequences(self.temp_file.name)
        
        # Basic checks
        self.assertEqual(len(result_df), 3)
        self.assertIn('one_hot', result_df.columns)
        self.assertIn('letter_composition', result_df.columns)
        
        # Check that maximum length is calculated correctly
        max_len = len(max(result_df['sequence'], key=len))
        self.assertEqual(result_df['one_hot'].iloc[0].shape[0], max_len)

if __name__ == '__main__':
    unittest.main()