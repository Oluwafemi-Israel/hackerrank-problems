# https://www.hackerrank.com/contests/apt-coding-challenge/challenges/toll-cost-digits


if __name__ == '__main__':
    road_nodes, road_edges = map(int, input().split())

    adj = [[] for i in range(road_nodes)]
    for ee in range(road_edges):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        adj[a].append((b, +c % 10))
        adj[b].append((a, -c % 10))

    ovis = [False] * road_nodes
    vis = [[False] * 10 for i in range(road_nodes)]

    ans = [0] * 10
    for s in range(road_nodes):
        if ovis[s]: continue
        queue = [(s, 0)]
        vis[s][0] = True
        f = 0
        ct = [0] * 10
        while f < len(queue):
            i, d = queue[f]
            f += 1
            ct[d] += 1
            for j, nd in adj[i]:
                nd = (nd + d) % 10
                if not vis[j][nd]:
                    vis[j][nd] = True
                    queue.append((j, nd))

        for i, d in queue:
            if ovis[i]:
                continue
            ovis[i] = True
            d = -d % 10
            for nd in range(10):
                ans[(nd + d) % 10] += ct[nd] - vis[i][nd]

    for v in ans: print(v)
