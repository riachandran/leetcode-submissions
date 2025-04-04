class Solution:
    def simplifyPath(self, path: str) -> str:
        path_objs = path.split("/")
        final_path = []
        for idx,val in enumerate(path_objs[1:]):
            if val == "..": 
                if len(final_path) > 0: 
                    final_path.pop(-1)
                    continue
            elif val != "" and val != ".": final_path.append("/"+val)
            elif val == ".": continue
        if final_path == []: return "/"
        return "".join(final_path)
