class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        def parseLog(logStr: str):
            log = logStr.split(":")
            # parse id
            log[0] = int(log[0])
            # parse timestamp
            log[2] = int(log[2])
            # id, action, timestamp
            return log
        
        time = [ 0 for _ in range(n)]
        exec_stack = []

        for logStr in logs:
            id, action, timestamp = parseLog(logStr)
            if action == "start":
                if exec_stack:
                    pre_id, pre_timestamp = exec_stack[-1]
                    time[pre_id] += timestamp - pre_timestamp
                exec_stack.append([id, timestamp])

            if action == "end":
                curr_id, curr_timestamp = exec_stack.pop()
                time[curr_id] += timestamp - curr_timestamp + 1
                if exec_stack:
                    exec_stack[-1][1] = timestamp + 1



        return time
        
