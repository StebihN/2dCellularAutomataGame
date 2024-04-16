class Utils:
    @staticmethod
    def constrain(val, min_val, max_val):
        return min(max_val, max(min_val, val))

    @staticmethod
    def map_range(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min
