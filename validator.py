"""
This module will validate the bms output.
"""
from typing import Dict

from validation_map import bms_validation


def bms_validation_function(bms_output_list: list) -> bool:

    """This function will take bms_output as string and will parse it
        and will match it to the expected ouput

    Args:
        bms_output (_str_): bms output as string
        _uuid (_str_): uuid string
        test_resp(_dict_): response object for test containing two keys: test_status and test_errors

    """
    test_errors = []

    try:
        flag = True
        for entries in bms_validation:
            
            index_ = entries["index"] + 1
            
            if entries["range"] == True:
                if (
                    float(bms_output_list[index_]) < entries["lower_limit"]
                    or float(bms_output_list[index_]) > entries["upper_limit"]
                ):
                    error_string = (
                        "The vaue of {} is {} should be between {} - {}".format(
                            entries["name"],
                            bms_output_list[index_],
                            entries["lower_limit"],
                            entries["upper_limit"],
                        )
                    )
                    
                    test_errors.append(error_string)
                    flag = False
            else:
                if bms_output_list[index_] in range(
                    entries["lower_limit"], entries["upper_limit"] + 1
                ):
                    error_string = (
                        "The vaue of {} is {} should be between {} - {}".format(
                            entries["name"],
                            bms_output_list[index_],
                            entries["lower_limit"],
                            entries["upper_limit"],
                        )
                    )
                    
                    test_errors.append(error_string)
                    flag = False

        if flag == False:
            return [False, test_errors]
        return [True,'#']

    except Exception as e:
        print(e,len(bms_output_list))
        return [False,'#']
