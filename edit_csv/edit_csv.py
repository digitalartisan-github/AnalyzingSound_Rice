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
                header_data.append(row[j])

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
            tmp_val.append(data[j][i])
        flip_array.append(tmp_val)

    return flip_array







FilePath = '../result/WashingRice_out_edit.csv'

head = get_header_data(FilePath)
data = get_matrix_data(FilePath, True)

print("Header :", head)
print("Data :", data)
# Header : ['-2', '-1', '0', '1', '2']
# Data : [['A', 'X', '0.1', '11', 'T'], ['B', 'Y', '0.01', '111', 'TT'], ['C', 'Z', '0.001', '1111', 'TTT']]



### operate date
# data_flip = flip_array(data)
# print("Dafa Flip :", data_flip)