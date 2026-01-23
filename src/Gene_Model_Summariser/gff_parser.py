import gffutils
from typing import Optional

class GFF_Parser:

    def __init__(self, db: gffutils.FeatureDB) -> None:
        self.db = db

    def get_genes(self) -> list[gffutils.Feature]:
        """Retrieve all gene features from the GFF database."""
        return list(self.db.features_of_type('gene'))