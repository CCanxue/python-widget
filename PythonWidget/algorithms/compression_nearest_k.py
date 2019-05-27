#coding: utf-8


#临近k个值进行压缩



#method1
def compression(k,seq):
    return zip(*([iter(seq)] * k))
    
 #method 2
def compression2(k, seq):
    return zip(*[seq[i::k] for i in range(k)])

#method3
def compression3(k, seq):
    return [seq[i:i+k] for i in range(0, len(seq)+1, k)][:len(seq)/k]
