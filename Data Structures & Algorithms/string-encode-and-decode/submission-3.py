class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_1 = ""
        for i in strs:
            encode_1+= str(len(i))+'#'+i

        return encode_1

    def decode(self, s: str) -> List[str]:
        decode_1 = []
        i = 0

        while i<len(s):
            j = i

            while s[j] !='#':
                j+=1
            length =int(s[i:j])


            decode_1.append(s[j+1:j+1+length])

            i = j+1+length

        return decode_1

