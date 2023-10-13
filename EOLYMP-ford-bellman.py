#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int INF = INT16_MAX;

int main() {

    int n, m;
    cin >> n >> m;

    vector<vector<int>> edges;
    for (int i = 0; i < m; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        edges.push_back({u, v, w});
    }

    vector<int> dist(n, INF);
    dist[0] = 0;

    for (int i = 0; i < n - 1; ++i) {
        for (const auto& edge : edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            if (dist[u - 1] != INF && dist[u - 1] + w < dist[v - 1]) {
                dist[v - 1] = dist[u - 1] + w;
            }
        }
    }

    for (int d : dist) {
        if(d < INF)
            cout << d << " ";
        else
            cout << 30000 << " ";
    }

    return 0;
}
