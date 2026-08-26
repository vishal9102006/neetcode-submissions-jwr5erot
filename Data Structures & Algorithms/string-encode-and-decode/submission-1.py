class Solution:

    def encode(self, strs):
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s):
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find '#'
            while s[j] != '#':
                j += 1

            # Get length of the string
            length = int(s[i:j])

            # Get the actual string
            start = j + 1
            end = start + length

            result.append(s[start:end])

            # Move to the next encoded string
            i = end

        return result