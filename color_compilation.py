from utils import Utils

class ColorCompilation:
    DOUBTFUL_COLORS = {"Lime": "Green", }

    def __init__(self):
        self.colors = dict()
        self.colors.update(self.get_colours())
        self.cross_rename(self.DOUBTFUL_COLORS)

    @staticmethod
    def get_colours():
        import colour
        d = colour.RGB_TO_COLOR_NAMES
        out = dict()
        for rgb_tuple in d.keys():
            names_list = d.get(rgb_tuple)
            for name in names_list:
                if name not in out.keys():
                    out[name] = rgb_tuple
        return {k: out.get(k) for k in sorted(list(set(out.keys())))}

    def cross_rename(self, d: dict):
        for target in d.keys():
            replacement = d.get(target)
            update = {target: self.colors.get(replacement), replacement: self.colors.get(target)}
            self.colors.update(update)


def test():
    # from color_compilation import ColorCompilation
    cc = ColorCompilation()
    Utils.export(cc.colors)


if __name__ == '__main__':
    test()
