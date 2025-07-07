def parse_event(data):
    # PUSH
    if "head_commit" in data:
        return {
            "type": "push",
            "author": data["head_commit"]["author"]["name"],
            "to_branch": data["ref"].split("/")[-1],
            "timestamp": data["head_commit"]["timestamp"]
        }
    # PULL REQUEST
    elif "pull_request" in data:
        pr = data["pull_request"]
        if data["action"] == "opened":
            return {
                "type": "pull_request",
                "author": pr["user"]["login"],
                "from_branch": pr["head"]["ref"],
                "to_branch": pr["base"]["ref"],
                "timestamp": pr["created_at"]
            }
        elif data["action"] == "closed" and pr.get("merged"):
            return {
                "type": "merge",
                "author": pr["user"]["login"],
                "from_branch": pr["head"]["ref"],
                "to_branch": pr["base"]["ref"],
                "timestamp": pr["merged_at"]
            }
    return None
