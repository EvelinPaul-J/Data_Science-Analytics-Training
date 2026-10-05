def top_k_frequent_logs(logs, k):
    count = {}
    for log in logs:
        tag = log.split(":")[0]
        if tag in count:
            count[tag] += 1
        else:
            count[tag] = 1
    sorted_tags = sorted(count, key=lambda x: (-count[x], x))
    return sorted_tags[:k]
logs = [
    "ERROR: db timeout",
    "INFO: user login",
    "ERROR: auth failed",
    "WARNING: disk low",
    "ERROR: lost connection",
    "INFO: user logout"
]
print(top_k_frequent_logs(logs, 2))