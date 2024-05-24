def dijk(graph, begin, end=False):
    length = {v: float('infinity') for v in graph}
    length[begin] = 0
    que = [(0, begin)]
    processed = set()
    finish = {v: None for v in graph}

    while que:
        now, point = min(que, key=lambda x: x[0])
        processed.add(now)
        que.remove(min(que, key=lambda x: x[0]))

        if now > length[point]:
            continue

        for neighbor, weight in graph[point].items():
            distance = now + weight

            if distance < length[neighbor]:
                length[neighbor] = distance
                que.append((distance, neighbor))
                finish[neighbor] = point

        if end and all(n in processed for n in graph[end].keys()):
            return length[end], finish

    return length, finish


def PATH(end, finish):
    path = [end]
    poi = finish[end]
    while not poi is None:
        path.append(poi)
        poi = finish[poi]
    return path[::-1]
