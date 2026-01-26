from pathlib import Path
#importing Set for type hint -> e.g.: seen_ids: Set[str]
from typing import Set
import Bio.SeqIO as SeqIO

#set up a custom exception for FASTA validation errors
class FastaValidationError(Exception):
    """Raised when FASTA validation fails."""
    pass

#accepting file path as Path or str
def validate_fasta(file_path: Path | str) -> None:
    """
    Validates a FASTA file format using BioPython's SeqIO.
    
    Performs comprehensive checks:
    - At least one sequence present
    - No duplicate sequence IDs
    - No empty sequences or headers
    - Valid nucleotide characters (ACGTN, case-insensitive)
    
    Args:
        file_path: Path to the FASTA file
        
    Raises:
        FastaValidationError: If file fails validation checks
        
    Example:
        >>> validate_fasta("genome.fasta")
        >>> validate_fasta("bad.fasta")  #raises FastaValidationError
    """
    file_path = Path(file_path)
    
    #validation state tracking with type hints
    seen_ids: Set[str] = set()
    sequence_count: int = 0
    valid_chars: Set[str] = set('ACGTN')
    
    #parse sequences - BioPython will raise ValueError if malformed
    #try/except block here to catch exceptions where they happen
    try:
        for record in SeqIO.parse(str(file_path), "fasta"):
            sequence_count += 1
            
            #check for empty or whitespace-only header
            if not record.id or not record.id.strip():
                raise FastaValidationError(
                    f"Empty header at sequence {sequence_count}"
                )
            
            #check for duplicate IDs
            if record.id in seen_ids:
                raise FastaValidationError(
                    f"Duplicate sequence ID: '{record.id}'"
                )
            seen_ids.add(record.id)
            
            #check for empty sequences
            if len(record.seq) == 0:
                raise FastaValidationError(
                    f"Empty sequence for ID: '{record.id}'"
                )
            
            #check for invalid characters (case-insensitive)
            seq_upper: str = str(record.seq).upper()
            invalid_chars: Set[str] = set(seq_upper) - valid_chars
            
            if invalid_chars:
                raise FastaValidationError(
                    f"Invalid characters {invalid_chars} in sequence '{record.id}'"
                )
    
    except ValueError as e:
        #biopython raises ValueError for malformed FASTA
        raise FastaValidationError(
            f"Malformed FASTA format: {e}"
        ) from e
    
    #raise validation error if no sequences found
    if sequence_count == 0:
        raise FastaValidationError("No sequences found in file")