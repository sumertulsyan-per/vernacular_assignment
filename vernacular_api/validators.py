def validate_finite_values_entity(data):
    res_dict = {}
    partially_filled_flag = False
    res_dict["parameters"] = {data["key"]: []}
    if data["values"]:
        if "support_multiple" in data.keys():
            if not data["support_multiple"]:
                lis = list()
                lis.append(data["values"][0])
                data["values"] = lis
        for value in data["values"]:
            if value["entity_type"] in data["type"]:
                partially_filled_flag = True
                if value["value"] in data["supported_values"]:
                    filled_status = res_dict.get("filled", "NoKey")
                    if filled_status:
                        res_dict["filled"] = True
                        res_dict["parameters"][data["key"]].append(value["value"].upper())
                else:
                    res_dict["filled"] = False
            else:
                res_dict["filled"] = False
    else:
        res_dict["filled"] = False
        res_dict["partially_filled"] = False

    if res_dict["filled"]:
        res_dict["partially_filled"] = False
        res_dict["trigger"] = ""
    else:
        res_dict["parameters"] = {}
        if partially_filled_flag:
            res_dict["partially_filled"] = True
            res_dict["trigger"] = data["invalid_trigger"]
        else:
            res_dict["partially_filled"] = False
            res_dict["trigger"] = data["invalid_trigger"]

    if data["pick_first"] and data["values"] and data["values"][0]["entity_type"] in data["type"] and \
            data["values"][0]["value"] in data["supported_values"]:
        res_dict["parameters"][data["key"]] = data["values"][0]["value"].upper()
    return res_dict


def validate_numeric_values_entity(data):
    res_dict = {}
    partially_filled_flag = False
    res_dict["parameters"] = {data["key"]: []}
    if data["values"]:
        if "support_multiple" in data.keys():
            if not data["support_multiple"]:
                lis = list()
                lis.append(data["values"][0])
                data["values"] = lis
        for value in data["values"]:
            if value["entity_type"] in data["type"]:
                partially_filled_flag = True
                if "constraint" in data.keys():
                    if data["constraint"]:
                        globals()[data["var_name"]] = value["value"]
                        if eval(data["constraint"]):
                            filled_status = res_dict.get("filled", "NoKey")
                            if filled_status:
                                res_dict["filled"] = True
                                res_dict["parameters"][data["key"]].append(value["value"])
                        else:
                            res_dict["filled"] = False
                    else:
                        filled_status = res_dict.get("filled", "NoKey")
                        if filled_status:
                            res_dict["filled"] = True
                            res_dict["parameters"][data["key"]].append(value["value"])
                else:
                    filled_status = res_dict.get("filled", "NoKey")
                    if filled_status:
                        res_dict["filled"] = True
                        res_dict["parameters"][data["key"]].append(value["value"])
            else:
                res_dict["filled"] = False
    else:
        res_dict["filled"] = False
        res_dict["partially_filled"] = False

    if res_dict["filled"]:
        res_dict["partially_filled"] = False
        res_dict["trigger"] = ""
    else:
        res_dict["parameters"] = {}
        if partially_filled_flag:
            res_dict["partially_filled"] = True
            res_dict["trigger"] = data["invalid_trigger"]
        else:
            res_dict["partially_filled"] = False
            res_dict["trigger"] = data["invalid_trigger"]

    if data["pick_first"] and data["values"] and data["values"][0]["entity_type"] in data["type"]:
        if "constraint" in data.keys():
            if data["constraint"]:
                globals()[data["var_name"]] = data["values"][0]["value"]
                if eval(data["constraint"]):
                    res_dict["parameters"][data["key"]] = data["values"][0]["value"]
            else:
                res_dict["parameters"][data["key"]] = data["values"][0]["value"]
        else:
            res_dict["parameters"][data["key"]] = data["values"][0]["value"]
    return res_dict

