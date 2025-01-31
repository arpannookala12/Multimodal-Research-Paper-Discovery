from pathlib import Path
from typing import Optional
from pydantic import BaseSettings

class Settings(BaseSettings):
    # Project paths
    PROJECT_ROOT: Path = Path(__file__).parent.parent.parent
    DATA_DIR: Path = PROJECT_ROOT / "data"
    CACHE_DIR: Path = DATA_DIR / "cache"
    
    # Model settings
    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
    EMBEDDING_DIMENSION: int = 384
    
    # Processing settings
    BATCH_SIZE: int = 1000
    MAX_MEMORY_PERCENT: float = 75.0
    
    class Config:
        env_file = ".env"

settings = Settings()