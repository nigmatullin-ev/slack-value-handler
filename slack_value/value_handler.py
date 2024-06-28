def get_values_data(values):
    keys = list(values.keys())
    value_data = {}

    for key in keys:
        element_name = str(list(values[key].keys())[0])

        if element_name.rfind("input") != -1:
            value = values[key][element_name]["value"]
            value_data.update({element_name: value})

        elif element_name.rfind("selector") != -1:
            try:
                value = values[key][element_name]["selected_option"]["value"]
                value_data.update({element_name: value})
            except TypeError:
                value_data.update({element_name: None})

        elif element_name.rfind("checkbox") != -1:
            selected_options = values[key][element_name]["selected_options"]

            if len(selected_options) > 0:
                checkboxes_value = [selected_option["value"] for selected_option in selected_options]
                value_data.update({element_name: checkboxes_value})
            else:
                value_data.update({element_name: None})

        elif element_name.rfind("datepicker") != -1:
            value = values[key][element_name]["selected_date"]
            value_data.update({element_name: value})

        elif element_name.rfind("multioptions") != -1:
            value = [opt['value'] for opt in values[key][element_name]["selected_options"]]
            value_data.update({element_name: value})

        elif element_name.rfind("button") != -1:
            value = values[key][element_name]["value"]
            value_data.update({element_name: value})

    return value_data
