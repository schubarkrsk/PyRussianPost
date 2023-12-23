def separate_responses(data: list):
    pass


def get_location(data: list):
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
