"""
Split code to different version parsers
"""
import os
import binascii

from datetime import datetime

def convert_from_hex_to_int(val):
    #print(val)
    #print(len(val))
    return int(val,16)

def get_parsable_data(hex_string):
    """
    """
    resp = []
    if hex_string:
        number_of_data = convert_from_hex_to_int(hex_string[18:20])
        start_addr = 20
        for _ in range(number_of_data):
            created_at = datetime.fromtimestamp(int(convert_from_hex_to_int(
                hex_string[start_addr: start_addr + 16]) * 0.001)).isoformat()
            location_data = hex_string[start_addr+18:start_addr+48]
            # 8 + 1 + 4 + 4 + 2 + 2 + 1 + 2 + 2 + 1 + 1
            # 28 bytes would include everything from `timestamp` to `no_of_total_ids`
            addr = start_addr + 48
            event_io_id = convert_from_hex_to_int(hex_string[addr:addr + 4])
            addr += 4
            n_of_total_byte_io = convert_from_hex_to_int(hex_string[addr:addr + 4])
            addr += 4

            one_byte_data = {}
            n1_of_one_byte_io = convert_from_hex_to_int(hex_string[addr:addr + 4])
            addr += 4  # Update address to move cursor after `n1_of_one_byte_io`
            for _ in range(n1_of_one_byte_io):
                key = convert_from_hex_to_int(hex_string[addr:addr + 4])
                addr += 4
                val = convert_from_hex_to_int(hex_string[addr:addr + 2])
                addr += 2
                one_byte_data[key] = val

            two_byte_data = {}
            n2_of_two_byte_io = convert_from_hex_to_int(hex_string[addr:addr + 4])
            addr += 4  # Update address to move cursor after `n2_of_one_byte_io`
            for _ in range(n2_of_two_byte_io):
                key = convert_from_hex_to_int(hex_string[addr:addr + 4])
                addr += 4
                val = convert_from_hex_to_int(hex_string[addr:addr + 4])
                addr += 4
                two_byte_data[key] = val

            four_byte_data = {}
            n4_of_four_byte_io = convert_from_hex_to_int(hex_string[addr:addr + 4])
            addr += 4  # Update address to move cursor after `n4_of_four_byte_io`
            for _ in range(n4_of_four_byte_io):
                key = convert_from_hex_to_int(hex_string[addr:addr + 4])
                addr += 4
                val = convert_from_hex_to_int(hex_string[addr:addr + 8])
                addr += 8
                four_byte_data[key] = val

            eight_byte_data = {}
            n8_of_eight_byte_io = convert_from_hex_to_int(
                hex_string[addr:addr + 4])
            addr += 4  # Update address to move cursor after `n8_of_eight_byte_io`
            for _ in range(n8_of_eight_byte_io):
                key = convert_from_hex_to_int(hex_string[addr:addr + 4])
                addr += 4
                val = convert_from_hex_to_int(hex_string[addr:addr + 16])
                addr += 16
                eight_byte_data[key] = val

            nx_of_x_byte_io = convert_from_hex_to_int(hex_string[addr:addr + 4])
            addr += 4
            x_bytes_io_map = {}
            for _ in range(nx_of_x_byte_io):
                nxth_io_id = convert_from_hex_to_int(hex_string[addr: addr + 4])
                addr += 4
                length_of_data = convert_from_hex_to_int(hex_string[addr: addr + 4])
                addr += 4
                data = binascii.unhexlify(hex_string[addr: (length_of_data * 2) + addr])
                x_bytes_io_map[nxth_io_id] = data
                addr += (length_of_data * 2)
            vehicle_data_string = x_bytes_io_map.get(539).decode() if x_bytes_io_map.get(539) else None
            resp.append((vehicle_data_string, created_at, location_data, {**one_byte_data, **two_byte_data, **four_byte_data, **eight_byte_data}, ))
            start_addr = addr

    return resp


