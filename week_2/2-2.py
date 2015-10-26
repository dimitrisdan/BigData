def bit_strings(N):

    end = N
    
    a = [0] * end
    
    def en(n):
        if n == end:
            print a
            return
        en(n+1)
        a[n]=1
        en(n+1)
        a[n]=0
    
    en(0)
    
    
print bit_strings(4)