def separate_responses(data: list):
    first_block = data[0]
    fb_adress_parametrs = first_block["AddressParameters"]
    address_parametrs = {
        "index_from": fb_adress_parametrs["OperationAddress"]["Index"],
        "location_from": fb_adress_parametrs["OperationAddress"]["Description"],
        "index_to": fb_adress_parametrs["DestinationAddress"]["Index"],
        "location_to": fb_adress_parametrs["DestinationAddress"]["Description"]
    }
    tracking_list = []
    for info in data:
        finance_info = info["FinanceParameters"]
        finance = {
            "declared_value": finance_info["Value"],
            "mass_rate": finance_info["MassRate"],
            "insr_rate": finance_info["InsrRate"],
            "air_rate": finance_info["AirRate"],
            "rate": finance_info["Rate"],
            "custom_duty": finance_info["CustomDuty"]
        }
        operation_info = info["OperationParameters"]
        operation = {
            "type": operation_info["OperType"]["Name"],
            "status": operation_info["OperAttr"]["Name"],
            "index": info["AddressParameters"]["OperationAddress"]["Index"],
            "location": info["AddressParameters"]["OperationAddress"]["Description"],
            "timestamp": info["OperationParameters"]["OperDate"]
        }
        status_dict = {
            "finance": finance,
            "operation": operation
        }
        tracking_list.append(status_dict)

    return {
        "from_to": address_parametrs,
        "traking": tracking_list
    }




def waypoints_handler(data: list):
    locations = []
    for position in data:
        date = position["OperationParameters"]["OperDate"]
        status = position["OperationParameters"]["OperAttr"]["Name"]
        operation_address = position["AddressParameters"]["OperationAddress"]
        info = {
            "date": date,
            "status": status,
            "index": operation_address["Index"],
            "location": operation_address["Description"]
        }
        locations.append(info)

    return locations
