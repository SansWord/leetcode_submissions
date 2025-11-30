class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split("/")
        simplifiedPath = []
        for dir in dirs:
            if dir == "" or dir == ".":
                continue

            if dir == "..":
                if simplifiedPath:
                    simplifiedPath.pop()
            else:
                simplifiedPath.append(dir)

        return "/" + "/".join(simplifiedPath)
        
