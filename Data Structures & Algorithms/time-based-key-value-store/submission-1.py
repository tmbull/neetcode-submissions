class TimeMap:
    # internal map: key -> {timestamp -> value}
    # built-in dict maintains insertion order, so we can do dict[key].values()[0] if the timestamp is not found

    def __init__(self):
        self.values = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.values:
            self.values[key][timestamp] = value
        else:
            self.values[key] = {timestamp: value}

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.values:
            return ""

        timestamps = self.values[key]
        if timestamp in timestamps:
            return timestamps[timestamp]
        else:
            for ts,value in reversed(timestamps.items()):
                if ts <= timestamp:
                    return value
            return ""
        
