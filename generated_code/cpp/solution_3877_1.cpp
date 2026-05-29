#include <vector>
#include <string>
#include <algorithm>
#include <queue>

using namespace std;

class Solution {
public:
    int score(vector<string>& cards, char x) {
        // Filter cards that contain the letter 'x'
        vector<string> valid_cards;
        for (const string& card : cards) {
            if (card[0] == x || card[1] == x) {
                valid_cards.push_back(card);
            }
        }
        
        int n = valid_cards.size();
        if (n < 2) return 0;
        
        // Build an adjacency list representing compatibility.
        // Two cards are compatible if they differ in exactly 1 position.
        vector<vector<int>> adj(n);
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int diff = 0;
                if (valid_cards[i][0] != valid_cards[j][0]) diff++;
                if (valid_cards[i][1] != valid_cards[j][1]) diff++;
                
                if (diff == 1) {
                    adj[i].push_back(j);
                    adj[j].push_back(i);
                }
            }
        }
        
        // Since each card has 2 lowercase letters and contains 'x', it must be of the form "xa" or "ax".
        // If it is "xx", it can match with "xa" or "ax" (differing by 1 character).
        // Notice that any valid card has a specific "parity" based on the position of 'x'.
        // This makes the compatibility graph bipartite. 
        // Finding the maximum number of pairs is equivalent to Maximum Bipartite Matching.
        // We use the Hopcroft-Karp algorithm (or BFS/DFS augmenting paths) to find the maximum matching.
        
        vector<int> match(n, -1);
        int max_matching = 0;
        
        // Helper lambda for DFS augmenting path detection
        vector<bool> visited(n, false);
        auto dfs = [&](auto& self, int u) -> bool {
            for (int v : adj[u]) {
                if (!visited[v]) {
                    visited[v] = true;
                    // If v is not matched, or we can find an augmenting path for its match
                    if (match[v] < 0 || self(self, match[v])) {
                        match[u] = v;
                        match[v] = u;
                        return true;
                    }
                }
            }
            return false;
        };
        
        // Greedy initialization & standard matching augmentation
        for (int i = 0; i < n; ++i) {
            if (match[i] < 0) {
                fill(visited.begin(), visited.end(), false);
                if (dfs(dfs, i)) {
                    max_matching++;
                }
            }
        }
        
        return max_matching;
    }
};