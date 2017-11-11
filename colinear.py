import itertools


class Solution:
    def my_solution(self, point_list):
        if len(point_list) > 1000:
            print("Number of points exceeds 1000")
            exit(1)

        maximum_triplets_allows = 100000000
        if len(list(itertools.combinations(pointlist, 3))) > maximum_triplets_allows:
            return -1

        self.verify_coordinates(point_list)
        # print(len(list((itertools.combinations(point_list, 3)))))
        i = 0
        for triplet in itertools.combinations(pointlist, 3):
            if self.is_colinear(triplet):
                print(triplet)
                i = i + 1
        return i

    def is_colinear(self, triplet):
        val1 = triplet[0][0] * (triplet[1][1] - triplet[2][1])
        val2 = triplet[1][0] * (triplet[2][1] - triplet[0][1])
        val3 = triplet[2][0] * (triplet[0][1] - triplet[1][1])
        val4 = val1 + val2 + val3
        val5 = val4 / 2
        if val5 == 0:
            return True
        else:
            return False

    def verify_coordinates(self, point_list):
        points_dict = dict(point_list)
        points_x = list(points_dict.keys())
        points_y = list(points_dict.values())
        self.verify_coordinate_value(points_x)
        self.verify_coordinate_value(points_y)

    def verify_coordinate_value(self, co_list):
        for each_value in co_list:
            if each_value > 9999:
                print("One of the point's x or y co-ordinate value exceeds 9999")
                exit(2)


if __name__ == '__main__':
    pointlist = [(0, 0), (1, 1), (2, 2), (3, 3), (3, 2), (4, 2), (5, 1)]
    Solution = Solution()
    result = Solution.my_solution(pointlist)
    print(result)
