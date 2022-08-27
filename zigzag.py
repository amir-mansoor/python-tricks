class Solution:
    def convert(self, s: str, numRows: int):
        if numRows == 1:
            return s
        row_map = {row:"" for row in range(1, numRows + 1)}
        print("Row Map: ",row_map)
        row = 1
        up = True
        print("Given String: "+s)
        for letter in s:
            row_map[row] += letter
            #print("Row map with row", row_map)
            if(row == 1) or ((row < numRows) and up):
                row +=1 
                up = True
                #print(row_map)
            else:
                row -= 1
                up = False

        converted = ""
        for row in range(1,numRows+1):
            converted += row_map[row]
            print("Converted: "+converted)
        return converted

x = Solution()
ans = x.convert("helloworld",3)
#print(ans)
