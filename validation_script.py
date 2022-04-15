'''
This module will get all file names
'''
import os
import codecs
import json
rootdir = os.getcwd()
from raw_string_parser import get_parsable_data
from validator import bms_validation_function

files_with_corrupt_data = 0
count = 0
required_strings_for_parser = []
req_mapp={}
blunder = 0
default_files_list =[]
location_data_coming_but_vehicle_data_none = 0
files_with_incomplete_data = 0
files_with_ignition_off =0 
files_with_error_during_validation = 0
files_with_data_validation_errors = 0

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file != 'validation_script.py' and file!='raw_string_parser.py' and file[0] != '.' and file[-3:]!="pyc":
            file_path = subdir + os.sep + file
            with codecs.open(file_path) as data_file:
                count +=1
                try:
                    data = data_file.read()
                    req = get_parsable_data(data)
                    try:
                        if req[0][0]==None:
                            location_data_coming_but_vehicle_data_none +=1
                        else:
                            try:
                                bms_output_list = req[0][0].split(",")
                            except Exception as e:
                                print(e)

                            if len(bms_output_list)>70:
                                
                                if float(bms_output_list[102]) > 0:
                                    res = bms_validation_function(bms_output_list)   
                                    
                                    if res == [False,'#']:
                                        files_with_error_during_validation += 1
                                    else:
                                        if res[1]!="#" and res[0] != True and res[1]!=[]:
                                            blunder += 1
                                            req_mapp[req[0][1]]=res[1]
                                            files_with_data_validation_errors += 1

                                else:
                                    files_with_ignition_off += 1
                                    
                            else:
                                files_with_incomplete_data+=1

                    except Exception as ex:
                        print(file,ex, len(res),req,req[0][0])
                except Exception as e:
                    default_files_list.append(file_path)
                    files_with_corrupt_data += 1

with codecs.open("default_files_list.txt","w") as default_file:
    for path in default_files_list:
        default_file.write(path)
        default_file.write("\n")

#print(default_files_list)
print(count, files_with_corrupt_data, location_data_coming_but_vehicle_data_none, files_with_incomplete_data, files_with_ignition_off, files_with_error_during_validation, files_with_data_validation_errors)
#print(req_mapp)
results_info_list = []
results_info_list.append("Total Number of files: %d" %count)
results_info_list.append("Total Number of files with corrupt data: %d     Percent of such files: %f" %(files_with_corrupt_data,(files_with_corrupt_data/count)*100))
results_info_list.append("Total Number of files with location data coming but vehicle data is none: %d     Percent of such files: %f" %(location_data_coming_but_vehicle_data_none,(location_data_coming_but_vehicle_data_none/count)*100))
results_info_list.append("Total Number of files with files with incomplete data: %d     Percent of such files: %f" %(files_with_incomplete_data,(files_with_incomplete_data/count)*100))
results_info_list.append("Total Number of files with files with ignition off: %d     Percent of such files: %f" %(files_with_ignition_off,(files_with_ignition_off/count)*100))
results_info_list.append("Total Number of I could not validate: %d     Percent of such files: %f" %(files_with_error_during_validation,(files_with_error_during_validation/count)*100))
results_info_list.append("Total number of files with Data Validation Errors %d     Percent of such files: %f" %(files_with_data_validation_errors,(files_with_data_validation_errors/count)*100))
with codecs.open("results_file.txt","w") as result_file:
    result_file.write(json.dumps(results_info_list))
    result_file.write("\n")
    result_file.write(json.dumps(req_mapp))
#print(count,blunder,files_with_corrupt_data)
