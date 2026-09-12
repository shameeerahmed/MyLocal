"""
Core data processor module for handling data transformations.
"""

import pandas as pd
from typing import Union, Dict, List
from pathlib import Path


class DataProcessor:
    """Handle data processing operations."""
    
    def __init__(self):
        """Initialize the data processor."""
        self.data = None
        self.metadata = {}
    
    def load_csv(self, filepath: str) -> pd.DataFrame:
        """
        Load data from a CSV file.
        
        Args:
            filepath: Path to the CSV file
            
        Returns:
            Loaded DataFrame
        """
        self.data = pd.read_csv(filepath)
        self.metadata['source'] = filepath
        print(f"Loaded {len(self.data)} rows from {filepath}")
        return self.data
    
    def load_json(self, filepath: str) -> pd.DataFrame:
        """
        Load data from a JSON file.
        
        Args:
            filepath: Path to the JSON file
            
        Returns:
            Loaded DataFrame
        """
        self.data = pd.read_json(filepath)
        self.metadata['source'] = filepath
        print(f"Loaded {len(self.data)} rows from {filepath}")
        return self.data
    
    def clean_data(self) -> pd.DataFrame:
        """
        Clean the loaded data (remove nulls, duplicates, etc).
        
        Returns:
            Cleaned DataFrame
        """
        if self.data is None:
            raise ValueError("No data loaded. Call load_csv() or load_json() first.")
        
        # Remove duplicates
        self.data = self.data.drop_duplicates()
        
        # Remove rows with all NaN values
        self.data = self.data.dropna(how='all')
        
        print(f"Data cleaned: {len(self.data)} rows remaining")
        return self.data
    
    def filter_data(self, column: str, value: str) -> pd.DataFrame:
        """
        Filter data by column value.
        
        Args:
            column: Column name to filter on
            value: Value to filter by
            
        Returns:
            Filtered DataFrame
        """
        if self.data is None:
            raise ValueError("No data loaded.")
        
        self.data = self.data[self.data[column] == value]
        print(f"Filtered to {len(self.data)} rows")
        return self.data
    
    def get_summary(self) -> Dict:
        """
        Get summary statistics of the data.
        
        Returns:
            Dictionary with summary information
        """
        if self.data is None:
            raise ValueError("No data loaded.")
        
        return {
            'rows': len(self.data),
            'columns': list(self.data.columns),
            'dtypes': self.data.dtypes.to_dict(),
            'missing': self.data.isnull().sum().to_dict()
        }
    
    def save_data(self, filepath: str, format: str = 'csv') -> None:
        """
        Save processed data to file.
        
        Args:
            filepath: Output file path
            format: File format ('csv' or 'json')
        """
        if self.data is None:
            raise ValueError("No data to save.")
        
        if format == 'csv':
            self.data.to_csv(filepath, index=False)
        elif format == 'json':
            self.data.to_json(filepath, orient='records')
        else:
            raise ValueError(f"Unsupported format: {format}")
        
        print(f"Data saved to {filepath}")
