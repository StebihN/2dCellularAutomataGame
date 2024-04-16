from Materials.Cell import Cell
from Materials.Usable.Air import Air
from Utils.Utils import Utils


class Water(Cell):
    def __init__(self, cell_type, color, mass):
        super().__init__(cell_type, color)
        self.mass = mass
        self.min_mass = 0.1
        self.max_mass = 1.0
        self.max_compression = 0.02
        self.min_flow = 0.01
        self.max_flow = 1
        self.min_color = 0.01
        self.max_color = 1.1

    def update(self, surroundings):
        if self.mass <= self.min_mass:
            return self.update_water(surroundings)

        if surroundings["bottom"].cell_type == "water" or surroundings["bottom"].cell_type == "air":
            flow = self.calculate_water_amount(self.mass + surroundings["bottom"].mass) - surroundings[
                "bottom"].mass

            if flow > self.min_flow:
                flow *= 0.5

            flow = Utils.constrain(flow, 0, min(self.max_flow, self.mass))

            self.mass -= flow
            surroundings["bottom"].mass += flow

        if self.mass <= self.min_mass:
            return self.update_water(surroundings)

        if surroundings["left"].cell_type == "water" or surroundings["left"].cell_type == "air":
            flow = (self.mass - surroundings["left"].mass) / 4

            if flow > self.min_flow:
                flow *= 0.5

            flow = Utils.constrain(flow, 0, self.mass)

            self.mass -= flow
            surroundings["left"].mass += flow

        if self.mass <= self.min_mass:
            return self.update_water(surroundings)

        if surroundings["right"].cell_type == "water" or surroundings["right"].cell_type == "air":
            flow = (self.mass - surroundings["right"].mass) / 4

            if flow > self.min_flow:
                flow *= 0.5

            flow = Utils.constrain(flow, 0, self.mass)

            self.mass -= flow
            surroundings["right"].mass += flow

        if self.mass <= self.min_mass:
            return self.update_water(surroundings)

        if surroundings["top"] == "water":
            flow = self.mass - self.calculate_water_amount(self.mass + surroundings["top"].mass)

            if flow > self.min_flow:
                flow *= 0.5

            flow = Utils.constrain(flow, 0, min(self.max_flow, self.mass))

            self.mass -= flow
            surroundings["top"].mass += flow

        return self.update_water(surroundings)

    def update_water(self, surroundings):
        if self.cell_type == "air":
            if self.mass != 0:
                self.cell_type = "water"
                self.color = self.water_color()
                return None, None
            else:
                return None, None
        elif self.cell_type == "water":
            if surroundings["top"].cell_type == "sand":
                sand = surroundings["top"]
                self.color = self.water_color()
                return sand, "top"
            elif surroundings["bottom"].cell_type == "wood":
                wood = surroundings["bottom"]
                return wood, "bottom"
            elif self.mass <= self.min_mass:
                self.cell_type = "air"
                self.mass = 0
                self.color = "#cef"
                return None, None
            else:
                self.color = self.water_color()
                return None, None

    def calculate_water_amount(self, total_mass):
        if total_mass <= 1:
            return 1
        elif total_mass < 2 * self.max_mass + self.max_compression:
            return (self.max_mass * self.max_mass + total_mass * self.max_compression) / (
                    self.max_mass + self.max_compression)
        else:
            return (total_mass + self.max_compression) / 2

    def water_color(self):
        m = Utils.constrain(self.mass, self.min_color, self.max_color)

        r = 0
        g = 100
        if m < 1:
            b = 255
            r = int(Utils.map_range(m, 0.01, 1, 200, 1))
            r = Utils.constrain(r, 1, 200)
            g = int(Utils.map_range(m, 0.01, 1, 220, 120))
        else:
            b = 215

        return '#{:02x}{:02x}{:02x}'.format(r, g, b)
