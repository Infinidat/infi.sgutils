from infi.instruct import Struct, FixedSizeArray
from infi.instruct import SNInt32 as Int
from infi.instruct import SNInt16 as Short


# http://tldp.org/HOWTO/SCSI-Generic-HOWTO/g_scsi_id.html
class SG_GET_SCSI_ID(Struct):
    _fields_ = [
                Int("host_no"),
                Int("channel"),
                Int("scsi_id"),
                Int("lun"),
                Int("scsi_type"),
                Short("h_cmd_per_lun"),
                Short("d_queue_depth"),
                FixedSizeArray("unused", 2, Int),
               ]


