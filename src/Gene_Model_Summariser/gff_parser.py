import gffutils
from typing import Optional

class GFF_Parser:

    def __init__(self, db: gffutils.FeatureDB) -> None:
        self.db = db

    def get_genes(self) -> list[gffutils.Feature]:
        """Retrieve all gene features from the GFF database."""
        genes = list(self.db.features_of_type('gene'))
        return genes
    
    def get_transcripts(self, gene_id: str) -> list[gffutils.Feature]:
        """Retrieve all transcript features for a given gene ID."""
        transcripts = list(self.db.children(gene_id, featuretype='mRNA', order_by='start'))
        return transcripts
    
    def count_exons(self, transcript_id: str) -> int:
        """Count the number of exons for a given transcript ID."""
        exons = list(self.db.children(transcript_id, featuretype='exon'))
        exon_count = len(exons)
        return exon_count