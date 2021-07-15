import json
import xmltodict
def json_conv(file):
    data_dict = xmltodict.parse(file.read())
    json_data = json.dumps(data_dict)

    return "".join(json_data)



if __name__ == "__main__":

    file = open("data-sample.xml", "r")
    list =json_conv(file)
    print (list)

