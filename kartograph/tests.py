from unittest import TestCase

class TestImport(TestCase):

    def test_import(self):
        # Make sure we can import under various python versions
        from kartograph import Kartograph
