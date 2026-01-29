import pytest
import gffutils
from pathlib import Path
from Gene_Model_Summariser.QC_check import QC_flags
from Gene_Model_Summariser.gff_parser import GFF_Parser

@pytest.fixture
def gff_db_fixture(tmp_path):
    """
    Create a GFF database from a fixture GFF file for testing.
    """
    gff_fixture = Path(__file__).parent / "Fixtures" / "models.gff3"
    db_path = tmp_path / "test.db"
    db = gffutils.create_db(str(gff_fixture), dbfn=str(db_path), force=True, keep_order=True)
    return db


fastaFile = Path(__file__).parent / "Fixtures" / "ref.fasta"

class TestQCCheck:

    def test_gff_QC(self, gff_db_fixture):
        """
        Test the gff_QC method to ensure it generates QC flags correctly.
        """

        flags = QC_flags(gff_db_fixture).gff_QC()

