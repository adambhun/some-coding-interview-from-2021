import math
import pandas as pd
import itertools


class Shape:
    def __init__(self):
        self.csv = pd.read_csv("shapes.csv", sep=",", header=0)
        self.df = pd.DataFrame(self.csv, dtype=int)
        self.df.set_index("id", inplace=False)

    def fetch_shape(self, id):
        try:
            return [i for i in self.df.loc[id]]
        except:
            return False

    def get_vertices(self, x, y, z, w, h, d):
        vertices = [
            [x, y, z],
            [x, y, z + d],
            [x, y + h, z],
            [x, y + h, z + d],
            [x + w, y, z],
            [x + w, y, z + d],
            [x + w, y + h, z],
            [x + w, y + h, z + d],
        ]
        return vertices

    def every_point(self, x, y, z, w, h, d):
        every_x = [i for i in range(x, x + w + 1)]
        every_y = [i for i in range(y, y + h + 1)]
        every_z = [i for i in range(z, z + d + 1)]
        return list(itertools.product(*[every_x, every_y, every_z]))

    def point_collision(self, points_1, points_2):
        if self.compare_distances(points_1, points_2) <= 0:
            return True
        else:
            return False

    def shape_collision(self, points_1):
        results = []
        for i in self.df.iterrows():
            specs = []
            for j in i[1]:
                specs.append(j)
        specs.pop(0)
        points_2 = self.every_point(*specs)
        results.append(self.point_collision(points_1, points_2))
        results.sort(reverse=True)
        if results[0] == True:
            return True
        else:
            return False

    def distance(self, x1, y1, z1, x2, y2, z2):
        d = math.sqrt(
            math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) + math.pow(z2 - z1, 2) * 1.0
        )
        return d

    def compare_distances(self, points_1, points_2):
        distances = []
        for i, j in zip(points_1, points_2):
            distances.append(self.distance(*i, *j))
        return min(distances)

    def add_shape(self, x, y, z, w, h, d):
        points_1 = self.every_point(x, y, z, w, h, d)
        if self.shape_collision(points_1) == True:
            return False
        else:
            new_id = len(self.df.index)
            shape = {"id": new_id, "x": x, "y": y, "z": z, "w": w, "h": h, "d": d}
            self.df = self.df.append(shape, ignore_index=True)
            self.df.to_csv("shapes.csv", index=False)
            return new_id

    def modify_shape(self, id, x, y, z):
        backup_numbers = (id, *self.fetch_shape(id))
        backup_row = self.df.loc[id]
        points_1 = self.every_point(
            x, y, z, backup_numbers[4], backup_numbers[5], backup_numbers[6]
        )
        self.df = self.df.drop([id])
        if self.shape_collision(points_1) == True:
            self.df.append(backup_row, ignore_index=True)
            return False
        else:
            shape = {
                "id": backup_numbers[0],
                "x": x,
                "y": y,
                "z": z,
                "w": backup_numbers[4],
                "h": backup_numbers[5],
                "d": backup_numbers[6],
            }
            self.df = self.df.append(shape, ignore_index=True)
            self.df.to_csv("shapes.csv", index=False)
            return True
