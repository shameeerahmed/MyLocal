"""
Utility functions for the data processing application.
"""

import json
from pathlib import Path
from typing import Dict, Any


def load_config(config_path: str = '.env') -> Dict[str, str]:
    """
    Load configuration from environment file.
    
    Args:
        config_path: Path to the configuration file
        
    Returns:
        Dictionary of configuration values
    """
    config = {}
    
    if Path(config_path).exists():
        with open(config_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    config[key.strip()] = value.strip()
    
    return config


def save_config(config: Dict[str, str], config_path: str = '.env') -> None:
    """
    Save configuration to environment file.
    
    Args:
        config: Configuration dictionary
        config_path: Path to save configuration
    """
    with open(config_path, 'w') as f:
        for key, value in config.items():
            f.write(f"{key}={value}\n")


def validate_file(filepath: str) -> bool:
    """
    Validate if a file exists and is readable.
    
    Args:
        filepath: Path to the file
        
    Returns:
        True if file exists and is readable
    """
    path = Path(filepath)
    return path.exists() and path.is_file() and path.stat().st_size > 0


def get_file_info(filepath: str) -> Dict[str, Any]:
    """
    Get information about a file.
    
    Args:
        filepath: Path to the file
        
    Returns:
        Dictionary with file information
    """
    path = Path(filepath)
    
    if not path.exists():
        return None
    
    return {
        'name': path.name,
        'size': path.stat().st_size,
        'created': path.stat().st_ctime,
        'modified': path.stat().st_mtime,
        'is_file': path.is_file()
    }
