import csv
import math



def access_csv(fp):
    # filePath = '../result/WashingRice_out_edit.csv'
    file_path = fp
    f = open(file_path, "r")
    reader = csv.reader(f)
    # print(type(reader))
    # <class '_csv.reader'>

    return reader



def get_header_data(fp):

    header_data = []
    tmp_reader = access_csv(fp)
    for i, row in enumerate(tmp_reader):
        if i is 0:
            row_length = len(row)
            for j in range(row_length):
                ### cast, str -> float
                header_data.append(float(row[j]))

    return header_data



def get_matrix_data(fp, haed_bool):
    all_data = []
    tmp_reader = access_csv(fp)

    ### HEADER : True
    if haed_bool:
        for i, row in enumerate(tmp_reader):
            if i is not 0:
                all_data.append(row)

    ### HEADER : False
    else:
        for i, row in enumerate(tmp_reader):
            all_data.append(row)

    return all_data



def flip_array(data):
    flip_array = []

    u = len(data)
    v = len(data[0])
    for i in range(v):
        tmp_val = []
        for j in range(u):
            ### cast, str -> float
            tmp_val.append(float(data[j][i]))
        flip_array.append(tmp_val)

    return flip_array


def calc_data(data):
    return len(data[0]), len(data)






# FilePath = '../result/WashingRice_out_edit.csv'
FilePath = str(path)



head = get_header_data(FilePath)
data = get_matrix_data(FilePath, True)
Hz, frame = calc_data(data)
# print(len(data))

### operate date
data_flip = flip_array(data)




### Export Component-Out
output_ = FilePath
header = head
datalist_flip = data_flip ### omoi
hz_count = Hz
frame_count = frame
