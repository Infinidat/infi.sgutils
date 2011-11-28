from infi import unittest

class ScsiIdTestCase(unittest.TestCase):
    def test_sg0(self):
        from .. import sg_scsi_id
        result = sg_scsi_id("/dev/sg0")

    def test_sda(self):
        from .. import sg_scsi_id
        result = sg_scsi_id("/dev/sda")

