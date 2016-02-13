from nrs import fileform
import os
import utils

def test_findheader_not_found():
    # Header should not be found in non-nsisi files.
    with open(os.path.join(utils.SAMPLES_DIR, 'empty'), 'rb') as empty:
        assert fileform._find_firstheader(empty) is None

def test_findheader_found():
    # Header found in NSIS installer.
    with open(os.path.join(utils.SAMPLES_DIR, 'example1.exe'), 'rb') \
            as nsis_file:
        firstheader = fileform._find_firstheader(nsis_file)
        assert firstheader is not None
        assert firstheader.siginfo == 0xDEADBEEF
        assert firstheader.magics == b'NullsoftInst'
        assert firstheader.c_size < firstheader.u_size