class Solution(object):
    def rotateTheBox(self, box):
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """

        m, n = len(box), len(box[0])


        for i in range(m):
            pos = n - 1

            for j in range(n - 1, -1, -1):
                if box[i][j] == '*':
                    pos = j - 1

                elif box[i][j] == '#':
                    box[i][j] = '.'
                    box[i][pos] = '#'
                    pos -= 1

        # Step 2: Rotate 90 degrees clockwise
        result = [[''] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                result[j][m - 1 - i] = box[i][j]

        return result
        