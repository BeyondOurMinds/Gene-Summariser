import argparse
import os
import re
from .GroupB_Project5 import main


def get_next_run_dir(base_dir: str) -> str:
    """Find the next available run directory (e.g., run_001, run_002, etc.)"""
    results_dir = os.path.join(base_dir, 'results')
    
    if not os.path.exists(results_dir):
        return os.path.join(results_dir, 'run_001')
    
    # Find existing run directories
    existing_runs = []
    for item in os.listdir(results_dir):
        match = re.match(r'run_(\d+)', item)
        if match:
            existing_runs.append(int(match.group(1)))
    
    # Get next run number
    if existing_runs:
        next_run = max(existing_runs) + 1
    else:
        next_run = 1
    
    return os.path.join(results_dir, f'run_{next_run:03d}')


def app():
    parser = argparse.ArgumentParser(description="A simple CLI tool.", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-g','--gff', required=True, help='Path to GFF file')
    parser.add_argument('-f','--fasta', help='Path to optional reference FASTA file for sequence-derived metrics')
    parser.add_argument('-o','--outdir', help='Output directory for results', default=None)
    args = parser.parse_args()
    
    # Set default output directory relative to input file location with auto-increment
    if args.outdir is None:
        gff_dir = os.path.dirname(args.gff) or '.'
        args.outdir = get_next_run_dir(gff_dir)
    
    # Call the main function from GroupB_Project5.py with the parsed arguments
    main(args.gff, args.fasta, args.outdir)
    
    return 0