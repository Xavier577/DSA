class Solution:
        def countPoints(self, rings: str) -> int:
            rods = {}

        for idx, char in enumerate(rings):
            if idx % 2 != 0:
                color = rings[idx - 1]
                position = char

                if position in rods:
                    rods[position].append(color)
                else:
                    rods[position] = [color]

        print(rods)

        color_spect = {'R': 0, 'G': 0, 'B': 0}
        n = 0

        for position in rods:
            for c in rods[position]:
                color_spect[c] += 1

            if color_spect['R'] > 0 and color_spect['G'] > 0 and color_spect['B'] > 0:
                n += 1 

            color_spect = {'R': 0, 'G': 0, 'B': 0}


        return n