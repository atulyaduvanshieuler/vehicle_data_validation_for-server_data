# name, index, lowerlimit, upperlimit, range

"""
name: Physical name of that index
index: What is the index in the output
lower_limit: Lower limit of that value
upper_limit: Upper limit of that value
var_type: What is the variable type should we receive
range: Shows whether we will receive discrete values or continuous values(google it if dont know about discrete and continuous) 
        True if values are continuous, False in case of discrete values
"""
#isme ik kam h 
bms_validation = [
    {
        "name": "BMS Data Pack I Master",
        "index": 3,
        "lower_limit": -4294967296,
        "upper_limit": 4294967296,
        
        "range": True,
    },
    {
        "name": "Pack Q SoC Trimmed",
        "index": 4,
        "lower_limit": 0,
        "upper_limit": 100,
        
        "range": True,
    },
    {
        "name": "SOH",
        "index": 5,
        "lower_limit": 0,
        "upper_limit": 100,
        
        "range": True,
    },
    {
        "name": "Pack V Sum of Cells",
        "index": 6,
        "lower_limit": 63,
        "upper_limit": 83,
        
        "range": True,
    },
    {
        "name": "BMS Status",
        "index": 7,
        "lower_limit": 0,
        "upper_limit": 4,
        
        "range": True,
    },
    {
        "name": "Aux Temperature_1",
        "index": 8,
        "lower_limit": 0,
        "upper_limit": 40,
        
        "range": True,
    },
    {
        "name": "Aux Temperature_2",
        "index": 9,
        "lower_limit": 0,
        "upper_limit": 40,
        
        "range": True,
    },
    {
        "name": "Aux Temperature_3",
        "index": 10,
        "lower_limit": 0,
        "upper_limit": 40,
        
        "range": True,
    },
    {
        "name": "Aux Temperature_4",
        "index": 11,
        "lower_limit": 0,
        "upper_limit": 40,
        
        "range": True,
    },
    {
        "name": "Aux Temperature_5",
        "index": 12,
        "lower_limit": 0,
        "upper_limit": 40,
        
        "range": True,
    },
    {
        "name": "Aux Temperature_6",
        "index": 13,
        "lower_limit": 0,
        "upper_limit": 40,
        
        "range": True,
    },
    {
        "name": "CMU1 Cell Voltage_1",
        "index": 15,
        "lower_limit": 3100,
        "upper_limit": 4200,
        
        "range": True,
    },
    {
        "name": "CMU1 Cell Voltage_2",
        "index": 16,
        "lower_limit": 3100,
        "upper_limit": 4200,
        
        "range": True,
    },
    {
        "name": "CMU1 Cell Voltage_3",
        "index": 17,
        "lower_limit": 3100,
        "upper_limit": 4200,
        
        "range": True,
    },
    {
        "name": "CMU1 Cell Voltage_4",
        "index": 18,
        "lower_limit": 3100,
        "upper_limit": 4200,
        
        "range": True,
    },
    {
        "name": "CMU1 Cell Voltage_5",
        "index": 19,
        "lower_limit": 3100,
        "upper_limit": 4200,
        
        "range": True,
    },
    {
        "name": "CMU1 Cell Voltage_6",
        "index": 20,
        "lower_limit": 3100,
        "upper_limit": 4200,
        
        "range": True,
    },
    {
        "name": "CMU1 Cell Voltage_7",
        "index": 21,
        "lower_limit": 3100,
        "upper_limit": 4200,
        
        "range": True,
    },
    {
        "name": "CMU1 Cell Voltage_8",
        "index": 22,
        "lower_limit": 3100,
        "upper_limit": 4200,
        
        "range": True,
    },
    {
        "name": "CMU1 Cell Voltage_9",
        "index": 23,
        "lower_limit": 3100,
        "upper_limit": 4200,
        
        "range": True,
    },
    {
        "name": "CMU1 Cell Voltage_10",
        "index": 24,
        "lower_limit": 3100,
        "upper_limit": 4200,
        
        "range": True,
    },
    {
        "name": "CMU2 Cell Voltage_1",
        "index": 33,
        "lower_limit": 3100,
        "upper_limit": 4200,
        
        "range": True,
    },
    {
        "name": "CMU2 Cell Voltage_2",
        "index": 34,
        "lower_limit": 3100,
        "upper_limit": 4200,
        
        "range": True,
    },
    {
        "name": "CMU2 Cell Voltage_3",
        "index": 35,
        "lower_limit": 3100,
        "upper_limit": 4200,
        
        "range": True,
    },
    {
        "name": "CMU2 Cell Voltage_4",
        "index": 36,
        "lower_limit": 3100,
        "upper_limit": 4200,
        
        "range": True,
    },
    {
        "name": "CMU2 Cell Voltage_5",
        "index": 37,
        "lower_limit": 3100,
        "upper_limit": 4200,
        
        "range": True,
    },
    {
        "name": "CMU2 Cell Voltage_6",
        "index": 38,
        "lower_limit": 3100,
        "upper_limit": 4200,
        
        "range": True,
    },
    {
        "name": "CMU2 Cell Voltage_7",
        "index": 39,
        "lower_limit": 3100,
        "upper_limit": 4200,
        
        "range": True,
    },
    {
        "name": "CMU2 Cell Voltage_8",
        "index": 40,
        "lower_limit": 3100,
        "upper_limit": 4200,
        
        "range": True,
    },
    {
        "name": "CMU1 Cell Voltage_9",
        "index": 41,
        "lower_limit": 3100,
        "upper_limit": 4200,
        
        "range": True,
    },
    {
        "name": "CMU2 Cell Voltage_10",
        "index": 42,
        "lower_limit": 3100,
        "upper_limit": 4200,
        
        "range": True,
    },
    {
        "name": "Fully Charge Flag",
        "index": 99,
        "lower_limit": 0,
        "upper_limit": 1,
        
        "range": False,
    },
    {
        "name": "BMS data Balancing limit",
        "index": 103,
        "lower_limit": 0,
        "upper_limit": 4200,
        
        "range": True,
    },
    {
        "name": "BMS Data Pre Charge Limit/Active",
        "index": 104,
        "lower_limit": 0,
        "upper_limit": 1,
        
        "range": False,
    },
    {
        "name": "BMS Data Balancing Active",
        "index": 105,
        "lower_limit": 0,
        "upper_limit": 1,
        
        "range": False,
    },
    {
        "name": "Dynamic In Limit",
        "index": 118,
        "lower_limit": 0,
        "upper_limit": 200,
        
        "range": True,
    },
    {
        "name": "Dynamic Out Limit",
        "index": 119,
        "lower_limit": 0,
        "upper_limit": 250,
        
        "range": True,
    },
    {
        "name": "ControllerData Motor Temp",
        "index": 52,
        "lower_limit": -50,
        "upper_limit": 200,
        
        "range": True,
    },
    {
        "name": "ControllerData Controller Temp",
        "index": 53,
        "lower_limit": -50,
        "upper_limit": 200,
        
        "range": True,
    },
    {
        "name": "ControllerData SpeedhighLow",
        "index": 60,
        "lower_limit": -60,
        "upper_limit": 60,
        
        "range": True,
    },
    {
        "name": "ControllerData Frequency",
        "index": 76,
        "lower_limit": -500,
        "upper_limit": 500,
        
        "range": True,
    },
    {
        "name": "ControllerData Motor Torque",
        "index": 78,
        "lower_limit": -100,
        "upper_limit": 100,
        
        "range": True,
    },
    {
        "name": "ControllerData Acceleration Rate",
        "index": 81,
        "lower_limit": 1,
        "upper_limit": 250,
        
        "range": True,
    },
    {
        "name": "ControllerData Acceleration Release Rate",
        "index": 82,
        "lower_limit": 1,
        "upper_limit": 250,
        
        "range": True,
    },
    {
        "name": "ControllerData Brake Rate",
        "index": 83,
        "lower_limit": 1,
        "upper_limit": 250,
        
        "range": True,
    },
    {
        "name": "ControllerData Drive Current Limit",
        "index": 84,
        "lower_limit": 10,
        "upper_limit": 100,
        
        "range": True,
    },
    {
        "name": "ControllerData Regen Current Limit",
        "index": 85,
        "lower_limit": 5,
        "upper_limit": 100,
        
        "range": True,
    },
    {
        "name": "ControllerData Brake Current Limit",
        "index": 86,
        "lower_limit": 5,
        "upper_limit": 100,
        
        "range": True,
    }
]
