"""
Tests for the data processor module.
"""

import pytest
import pandas as pd
from src.data_processor import DataProcessor


class TestDataProcessor:
    """Test cases for DataProcessor class."""
    
    @pytest.fixture
    def processor(self):
        """Create a processor instance for testing."""
        return DataProcessor()
    
    def test_initialization(self, processor):
        """Test that processor initializes correctly."""
        assert processor.data is None
        assert processor.metadata == {}
    
    def test_get_summary_no_data(self, processor):
        """Test that get_summary raises error when no data loaded."""
        with pytest.raises(ValueError):
            processor.get_summary()
    
    def test_clean_data_no_data(self, processor):
        """Test that clean_data raises error when no data loaded."""
        with pytest.raises(ValueError):
            processor.clean_data()


if __name__ == "__main__":
    pytest.main([__file__])
