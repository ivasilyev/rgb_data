import os


class Utils:
    @staticmethod
    def export(data: dict, file_prefix: str, out_dir: str = os.getcwd()):
        import json
        #
        out_dir = os.path.join(out_dir, "blob")
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "{}.json".format(file_prefix)), mode="w", encoding="utf-8") as f:
            json.dump(data, f, sort_keys=True)
            f.close()
        with open(os.path.join(out_dir, "{}.txt".format(file_prefix)), mode="w", encoding="utf-8") as f:
            f.write("\n".join(sorted(list(data.keys()))) + "\n")
            f.close()
        print("Saved into: '{}'".format(out_dir))

    @staticmethod
    def generate_boilerplate(data: dict, file_prefix: str, out_dir: str = os.getcwd()):
        out = "\n".join(["class BoilerPlate:"] + ["    {} = {}".format(
            *[str(i) for i in [k, data.get(k)]]) for k in data.keys()])
        out_dir = os.path.join(out_dir, "boilerplate")
        with open(os.path.join(out_dir, "{}.py".format(file_prefix)), mode="w", encoding="utf-8") as f:
            f.write(out + "\n")
            f.close()
        print("Saved into: '{}'".format(out_dir))
