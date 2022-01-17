def longestMountain(A) -> int:
        """
        Note: Mountain arrays can be naturally symmetric but also non-symmetric! Example:
         /\
           \
            \
        """
        i = ans = 0
        
        while i < len(A):

            # define a new start point
            start = i
            
            # walk up as long as it goes
            while i + 1 < len(A) and A[i] < A[i + 1]:
                i += 1
            
            have_we_climbed_at_all = i > start
            
            if have_we_climbed_at_all:
                peak = i  # then we have reached a peak
            else:
                i += 1
                continue  # otherwise we walked flat or went down without ascent hence start over
            
            # walk down the peak as long as it goes (now that we have a peak)
            while i + 1 < len(A) and A[i] > A[i + 1]:
                i += 1
            
            have_we_gone_down_at_all = i > peak
            
            if have_we_gone_down_at_all:
                end = i
            else:
                i += 1
                continue  # otherwise we climbed back up or walked flat without descent hence start over
            
            # update longest mountain
            ans = max(ans, end - start + 1)
        
        return ans