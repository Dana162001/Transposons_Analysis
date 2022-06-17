def seq_in_trans(s_coords, t_coords):
    output = [0]*len(t_coords)
    for i, t in enumerate(t_coords):
        for s in s_coords:
            if t[0] <= s[0] and t[1]>=s[1]:
                output[i]+=1
    return output
