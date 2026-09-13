def linear_interpolation(values: list) -> list:
   
    res = values.copy()
    n = len(res)
    
    i = 0
    while i < n:
        if res[i] is not None:
           
            left_idx = i
            i += 1
        else:
           
            right_idx = i
            while right_idx < n and res[right_idx] is None:
                right_idx += 1
            
        
            v_left = res[left_idx]
            v_right = res[right_idx]
         
            for j in range(i, right_idx):
                res[j] = v_left + (j - left_idx) / (right_idx - left_idx) * (v_right - v_left)
            
    
            i = right_idx
            
    return res