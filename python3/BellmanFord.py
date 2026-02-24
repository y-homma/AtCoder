def bellmanford(V, E): #vertex, edge = (from, to, cost)
    dist = [10 ** 20] * V
    dist[0] = 0
    for _ in range(V):
        update = False
        for efrom, eto, ecost in E:
            if dist[efrom] < 10 ** 20 and dist[eto] > dist[efrom] + ecost:
                dist[eto] = dist[efrom] + ecost
                update = True

        if not update: break

    return dist
