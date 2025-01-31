from pathlib import Path
import json
from typing import Dict, List, Optional
import pandas as pd
from tqdm import tqdm

class DataProcessor:
    def __init__(self, data_dir: Path):
        self.data_dir = data_dir
        self.raw_dir = data_dir / "raw"
        self.processed_dir = data_dir / "processed"
        self.cache_dir = data_dir / "cache"
        
        # Create directories if they don't exist
        self.raw_dir.mkdir(exist_ok=True)
        self.processed_dir.mkdir(exist_ok=True)
        self.cache_dir.mkdir(exist_ok=True)
    
    def read_metadata(self, file_path: str) -> pd.DataFrame:
        """Read and process the arXiv metadata file"""
        data = []
        with open(file_path, 'r') as f:
            for line in tqdm(f, desc="Reading metadata"):
                data.append(json.loads(line))
        return pd.DataFrame(data)
    
    def create_stratified_sample(
        self,
        df: pd.DataFrame,
        sample_size: int = 100000,
        min_category_size: int = 20
    ) -> pd.DataFrame:
        """Create a stratified sample based on categories"""
        # Get category counts
        category_counts = df['categories'].value_counts()
        
        # Filter categories with enough samples
        valid_categories = category_counts[category_counts >= min_category_size].index
        
        # Filter DataFrame
        df_filtered = df[df['categories'].isin(valid_categories)]
        
        # Create stratified sample
        sample = df_filtered.groupby('categories', group_keys=False).apply(
            lambda x: x.sample(
                n=min(len(x), int(sample_size * len(x) / len(df_filtered)))
            )
        )
        
        return sample.reset_index(drop=True)