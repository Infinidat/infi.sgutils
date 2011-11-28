from infi import unittest

class SgMapTestCase(unittest.TestCase):

    def test_get_sg_to_hctl_mappings(self):
        from .. import get_sg_to_hctl_mappings as getter
        result = getter()
        self.assertIn("/dev/sg0", result.keys())

    def test_get_sd_to_hctl_mappings(self):
        from .. import get_sd_to_hctl_mappings as getter
        self.assertIn("/dev/sda", result.keys())
        result = getter()

    def test_sg_to_sd(self):
        from .. import get_sd_from_sg
        self.assertEqual("sda", get_sd_from_sg("sg1"))

