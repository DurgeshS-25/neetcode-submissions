class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        li_01 = defaultdict(list)

        for i in strs:
            count = [0]*26
            for j in i:
                count[ord(j)-ord('a')] +=1
            
            li_01[tuple(count)].append(i)

        

        return list(li_01.values())
        