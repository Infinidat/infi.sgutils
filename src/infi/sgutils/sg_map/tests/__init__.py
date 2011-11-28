from infi import unittest

class SgMapTestCase(unittest.TestCase):

    def test_get_sg_to_hctl_mappings(self):
        from .. import get_sg_to_hctl_mappings as getter
        result = getter()

    def test_get_sd_to_hctl_mappings(self):
        from .. import get_sd_to_hctl_mappings as getter
        result = getter()

