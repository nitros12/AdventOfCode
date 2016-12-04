from stuff import vec2d
import math


def deg_sin(x):
    return math.sin(math.radians(x))


class Solution:
    def __init__(self, vectors):
        self.vectors = vectors

    @staticmethod
    def _parse_vector(vecstr, direction=0):
        return vec2d.Vec2D(deg_sin(direction), deg_sin(90-direction)) * vec2d.Vec2D(int(vecstr[1:]), int(vecstr[1:]))

    def reduce_vectors(self):
        end = vec2d.Vec2D(0, 0)
        current_rot = 0
        current_rot = 0
        for i in self.vectors:
            current_rot += {"L": -90, "R": 90}[i[0]]
            end += self._parse_vector(i, current_rot)
        return abs(end)

    def complete(self):
        final_vector = self.reduce_vectors()
        return round(final_vector.x + final_vector.y)

if __name__ == "__main__":
    challengeInput = input("Problem input: ").strip("\n").split(", ")
    mySolution = Solution(challengeInput)

    print("Solution is: {}".format(mySolution.complete()))
