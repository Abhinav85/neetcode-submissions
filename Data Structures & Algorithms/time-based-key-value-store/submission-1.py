class TimeMap:

    def __init__(self):
        self.time_map_obj = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map_obj:
            self.time_map_obj[key]["timestamp"].append(timestamp)
            self.time_map_obj[key]["values"][timestamp] = value
        else:
            self.time_map_obj[key] = {
                "timestamp" : [timestamp],
                "values": {
                    timestamp : value
                }
            }
        return None
        

        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        print (key, self.time_map_obj)
        if not (key in self.time_map_obj):
            return res
        timestamp_arr = self.time_map_obj[key]["timestamp"]
        l = 0
        r = len(timestamp_arr) - 1
        while l <= r:
            mid = (l + r) // 2
            num = timestamp_arr[mid]
            if num > timestamp:
                r = mid - 1
            elif num <= timestamp:
                l = mid + 1
                res=num
        if res == "":
            return res
        return self.time_map_obj[key]["values"][res]
        
