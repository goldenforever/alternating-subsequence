def alt_sub(array, processors=2):
    subresults = []
    singles = []
    for i in range(processors):
        left = (i*len(array))//processors
        right = ((i + 1)*len(array))//processors
        subarray = singles + array[left:right]
        subseq = []
        for num in subarray:
            if not subseq:
                subseq.append(num)
                continue
            if subseq[-1] == num:
                continue
            if len(subseq) == 1:
                subseq.append(num)
                continue
            if (num - subseq[-1]) * (subseq[-1] - subseq[-2]) < 0:
                subseq.append(num)
                continue
            subseq[-1] = num
        if len(subseq) < 2:
            # Special case where all numbers in a subarray are equal
            singles = [subseq[0]]
        else:
            singles = []
            subresults.append([len(subseq),              # 0: length
                               subseq[1] > subseq[0],    # 1: increases at start?
                               subseq[-1] > subseq[-2],  # 2: increases at end?
                               subseq[0],                # 3: first number
                               subseq[-1]])              # 4: last number
    # Merge second last and last until one remains
    while len(subresults) != 1:
        last = subresults.pop()
        s_last = subresults.pop()
        sum_len = s_last[0]+last[0]-1
        if (s_last[2] and last[1] and s_last[4] > last[3]) or \
                (not (s_last[2] or last[1]) and s_last[4] < last[3]):
            sum_len += 1
        elif (s_last[2] and last[1] and s_last[4] <= last[3]) or \
                (not (s_last[2] or last[1]) and s_last[4] >= last[3]):
            sum_len -= 1
        subresults.append((sum_len, s_last[1], last[2], s_last[3], last[4]))
    # Handle special case
    if singles:
        if (singles[0] > subresults[0][4] and not subresults[0][2]) or \
                (singles[0] < subresults[0][4] and subresults[0][2]):
            return subresults[0][0] + 1
    return subresults[0][0]