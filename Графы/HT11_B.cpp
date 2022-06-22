#include <iostream>
#include <cstdlib>

const int INF = 1000000000;
 
int main() {
    int n, m;
    std::cin >> n >> m;
    std::vector<std::vector<std::pair<int,int>>> g(n);
    g.
    int s = 1;
 
    vector<int> d (n, INF),  p (n);
    d[s] = 0;
    priority_queue < pair<int,int> > q;
    q.push (make_pair (0, s));
    while (!q.empty()) {
        int v = q.top().second,  cur_d = -q.top().first;
        q.pop();
        if (cur_d > d[v])  continue;
 
        for (size_t j=0; j<g[v].size(); ++j) {
            int to = g[v][j].first,
                len = g[v][j].second;
            if (d[v] + len < d[to]) {
                d[to] = d[v] + len;
                p[to] = v;
                q.push (make_pair (-d[to], to));
            }
        }
    }
}
