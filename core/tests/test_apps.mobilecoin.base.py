from common import *

if utils.USE_MOBILECOIN:
    from apps.mobilecoin import get_address


@unittest.skipUnless(utils.USE_MOBILECOIN, "mobilecoin")
class TestMobilecoinBase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, False)

    
if __name__ == "__main__":
    unittest.main()
