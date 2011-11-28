import opcodes
import structures

def ioctl(device_path, op_number, buffer=None):
    with open(device_path) as fd:
        from fcntl import ioctl as _ioctl
        args = [fd, op_number,]
        if buffer is not None:
            args.extend([buffer, True])
        return _ioctl(*args)

def sg_scsi_id(device_path):
    """:returns: a :class:`.SG_GET_SCSI_ID` object"""
    from array import array
    size = struct.min_max_sizeof().max
    buffer = array("B", [0]*size)
    result = ioctl(device_path, opcodes.SG_GET_SCSI_ID, buffer)
    struct = structures.SG_GET_SCSI_ID.from_string(buffer)
    return struct

