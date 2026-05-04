#!/usr/bin/env python3
"""
Script to run Gazebo with the fieldbot model in the field_test.world
Launches gazebo directly with proper environment configuration.
"""

import subprocess
import os
from pathlib import Path


def run_gazebo():
    """Launch Gazebo with the fieldbot model in field_test.world"""
    
    # Get paths
    project_root = Path(__file__).resolve().parent
    sim_dir = project_root / 'sim'
    world_path = sim_dir / 'worlds' / 'field_test_embedded.world'
    
    # Verify paths exist
    if not world_path.exists():
        print(f"Error: World file not found at {world_path}")
        return False
    
    if not (sim_dir / 'models').exists():
        print(f"Error: Models directory not found at {sim_dir / 'models'}")
        return False
    
    # Set up environment with model path
    env = os.environ.copy()
    env['GZ_SIM_RESOURCE_PATH'] = str(sim_dir)
    
    # Also set GAZEBO_MODEL_PATH for compatibility
    env['GAZEBO_MODEL_PATH'] = str(sim_dir / 'models')
    
    print(f"GZ_SIM_RESOURCE_PATH: {env['GZ_SIM_RESOURCE_PATH']}")
    print(f"GAZEBO_MODEL_PATH: {env['GAZEBO_MODEL_PATH']}")
    print(f"World file: {world_path}")
    print("Launching Gazebo...\n")
    
    try:
        # Use 'gz sim' command directly with the world file and verbose logging
        subprocess.run(
            ['gz', 'sim', '-v', '4', str(world_path)],
            env=env,
            check=False
        )
    except FileNotFoundError:
        print("Error: 'gz' command not found. Please ensure Gazebo is installed.")
        return False
    except Exception as e:
        print(f"Error launching Gazebo: {e}")
        return False
    
    return True


if __name__ == '__main__':
    success = run_gazebo()
    exit(0 if success else 1)
