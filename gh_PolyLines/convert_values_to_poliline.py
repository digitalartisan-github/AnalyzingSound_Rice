# gh の中身

import random
import rhinoscriptsyntax as rs


a = []
zigzag = []
pl_off = []


# convert values to poliline
def wave_line(values, r, in_d):

    ### interpolation dist
    # inter_dist = 4 * 0.5
    inter_dist = in_d

    for i in xrange(len(values)):
        tmp_pt = rs.AddPoint(values[i], i*r, 0)
        tmp_pt_m = rs.MirrorObject(tmp_pt, (0,0,0), (0,10,0), True)

        # zigzag
        if i%2 == 0:
            tmp_pt_0 = rs.CopyObject(tmp_pt)
            tmp_pt_0 = rs.MoveObject(tmp_pt_0, (0,-1*(inter_dist),0))
            tmp_pt_1 = rs.CopyObject(tmp_pt)
            tmp_pt_1 = rs.MoveObject(tmp_pt_1, (0,1*(inter_dist),0))
            zigzag.append(tmp_pt_0)
            zigzag.append(tmp_pt_1)
        else:
            tmp_pt_0 = rs.CopyObject(tmp_pt_m)
            tmp_pt_0 = rs.MoveObject(tmp_pt_0, (0,-1*(inter_dist),0))
            tmp_pt_1 = rs.CopyObject(tmp_pt_m)
            tmp_pt_1 = rs.MoveObject(tmp_pt_1, (0,1*(inter_dist),0))
            zigzag.append(tmp_pt_0)
            zigzag.append(tmp_pt_1)

    tmp_polyline = rs.AddPolyline(zigzag)
    return zigzag, tmp_polyline


# test data
rand_values = []
rand_count = 240
for i in xrange(rand_count):
    tmp_value = random.randrange(5, 100)
    rand_values.append(tmp_value)



pts, pl = wave_line(rand_values, 10, 2)

a = pl
