import os


class Utils:
    @staticmethod
    def export(data: dict, out_dir: str = os.getcwd()):
        import json
        #
        out_dir = os.path.join(out_dir, "blob")
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "colors.json"), mode="w", encoding="utf-8") as f:
            json.dump(data, f, sort_keys=True)
            f.close()
        with open(os.path.join(out_dir, "colors.txt"), mode="w", encoding="utf-8") as f:
            f.write("\n".join(sorted(list(data.keys()))) + "\n")
            f.close()
        print("Saved into: '{}'".format(out_dir))
