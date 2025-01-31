import pytest
from pathlib import Path
from src.data.processor import DataProcessor

def test_data_processor_init():
    processor = DataProcessor(Path("data"))
    assert processor.raw_dir.exists()
    assert processor.processed_dir.exists()
    assert processor.cache_dir.exists()

def test_stratified_sample():
    # Create test data
    test_data = pd.DataFrame({
        'categories': ['A']*100 + ['B']*50 + ['C']*30,
        'text': ['test']*180
    })
    
    processor = DataProcessor(Path("data"))
    sample = processor.create_stratified_sample(
        test_data,
        sample_size=90,
        min_category_size=10
    )
    
    assert len(sample) == 90
    assert all(sample['categories'].value_counts() >= 10)