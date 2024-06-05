def edge_detector_1(thickness_array:list)->[int ,int]:
    '''edge detection based on non zero value'''
    left_edge=0
    right_edge=0
    for i ,val in enumerate(thickness_array):
        if val!=0:
            left_edge=i
            break
    for i ,val in enumerate(reversed(thickness_array)):
        if val!=0:
            right_edge=len(thickness_array)-i-1
            break
    if left_edge!=0 and right_edge!=0:
        return [left_edge ,right_edge]
    else:
        raise ValueError

def edge_detector_2(thickness_array:list) ->[int ,int]:
    '''edge detection based on 40% thresh hold'''
    pass



