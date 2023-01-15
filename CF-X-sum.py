def main():
    T = int(input())
    
    for test in range(T):
        pos = list(map(int, input().split()))
        
        n = pos[0]
        m = pos[1]
        
        grid = []
        
        for i in range(n):
            grid.append(list(map(int, input().split())))
        
        
        main_diagonal_sums = {}
        right_diagonal_sums = {}
        
        d_diff = n - 1
        d_sum = 0
        
        while d_diff >= -m+1:
            i = max(0, d_diff)
            main_sum = 0
            while i < n and  i - d_diff < m:
                main_sum+=grid[i][i - d_diff]
                i+=1
            main_diagonal_sums[d_diff] = main_sum
            d_diff-=1
        
        while d_sum <= n+m-2:
            i = min(m-1, d_sum)
            right_sum = 0
            while d_sum - i < n and  i >= 0:
                right_sum+=grid[d_sum - i][i]
                i-=1
            right_diagonal_sums[d_sum] = right_sum
            d_sum+=1
            
        max_sum = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                max_sum = max(max_sum, main_diagonal_sums[i-j] + 
                right_diagonal_sums[i+j] - cell )
                
        print(max_sum)
        
    
    
if __name__ == "__main__":
    main()
