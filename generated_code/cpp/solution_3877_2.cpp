#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <unordered_map>

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
        
        // Count frequencies of each unique valid card
        unordered_map<string, int> counts;
        for (const string& card : valid_cards) {
            counts[card]++;
        }
        
        // Group identical cards and identify singletons.
        // Identical cards are always compatible because they differ in exactly 1 position?
        // Wait, the rule says: "differ in exactly 1 position". 
        // If two cards are identical (e.g., "ax" and "ax"), they differ in 0 positions.
        // Let's re-verify: "differ in exactly 1 position" means Hamming distance == 1.
        // Therefore, identical cards are NOT compatible. They must differ in exactly 1 position.
        
        // Build the graph where an edge exists if two cards differ in exactly 1 position.
        // Since we can match any two distinct card indices that satisfy the condition, 
        // this is a Maximum Cardinality Matching problem on a general graph.
        // However, let's look closely at the properties of the cards containing 'x'.
        // Every card has 2 characters, and at least one is 'x'.
        // Possible formats for a card containing 'x':
        // Type 1: "xx"
        // Type 2: "ax" where a != x
        // Type 3: "xa" where a != x
        //
        // Let's check compatibility (Hamming distance == 1):
        // - "xx" is compatible with "ax" (differs at pos 0) and "xa" (differs at pos 1).
        // - "ax" is compatible with "bx" (differs at pos 0) and "xx" (differs at pos 0).
        // - "xa" is compatible with "xb" (differs at pos 1) and "xx" (differs at pos 1).
        // - "ax" and "xb" differ in both positions (distance 2), so NOT compatible.
        // - "ax" and "xa" differ in both positions (distance 2), so NOT compatible.
        //
        // This reveals that the graph is BIPARTITE!
        // Partition L: Cards of the form "ax" (where position 1 is 'x', position 0 is not 'x').
        // Partition R: Cards of the form "xa" (where position 0 is 'x', position 1 is not 'x').
        // What about "xx"? 
        // "xx" connects to "ax" (in L) and "xa" (in R). 
        // If we treat "xx" as its own entity, it can connect to both sides.
        // But notice there are no edges between any two nodes in L ("ax" and "bx" differ at pos 0, 
        // but wait! "ax" and "bx" differ at pos 0, and they both have 'x' at pos 1. 
        // So their distance is 1! 
        // Ah! "ax" and "bx" differ in exactly 1 position (pos 0). So they ARE compatible!
        // My previous deduction was wrong. "ax" and "bx" ARE compatible.
        
        // Let's re-evaluate edges:
        // Group A: cards of form " _ x " (position 1 is x) -> includes "ax", "bx", ..., "xx"
        // Group B: cards of form " x _ " (position 0 is x) -> includes "xa", "xb", ..., "xx"
        //
        // If two cards are both in Group A (e.g., "ax" and "bx"), they differ only at position 0. 
        // Since they are distinct strings, they differ in exactly 1 position. So ALL distinct cards in Group A are connected to each other! Group A forms a clique (minus identical copies).
        // Similarly, ALL distinct cards in Group B form a clique.
        // What about an edge between Group A and Group B?
        // A card "ax" (from A) and "xb" (from B) -> distance is 2 (unless a=x and b=x, which is "xx").
        // So the only cross-edges between the two groups involve "xx".
        // Specifically, "xx" (which belongs to both groups) connects to "ax" (differs at pos 0) and "xa" (differs at pos 1).
        
        // Since the graph structure allows any distinct cards within Group A to match, and any distinct cards within Group B to match,
        // we can use Edmond's Blossom algorithm for general matching, or since N is typically small in LeetCode string problems,
        // we can just implement the standard Maximum Bipartite Matching if it were bipartite, but it's a general graph.
        // Let's implement the Blossom Algorithm for Maximum Matching on General Graphs to be absolutely optimal and correct.

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

        // Blossom Algorithm Helper Functions
        vector<int> match(n, -1);
        vector<int> p(n);
        vector<int> base(n);
        vector<int> used(n);
        vector<int> blossom(n);

        auto lca = [&](int u, int v) {
            vector<bool> path(n, false);
            while (true) {
                u = base[u];
                path[u] = true;
                if (match[u] == -1) break;
                u = p[match[u]];
            }
            while (true) {
                v = base[v];
                if (path[v]) return v;
                v = p[match[v]];
            }
        };

        auto mark_blossom = [&](int l, int u, queue<int>& q) {
            while (base[u] != l) {
                int v = match[u];
                blossom[base[u]] = blossom[base[v]] = true;
                p[v] = u;
                u = p[v];
                if (used[v] == 1) {
                    used[v] = 0;
                    q.push(v);
                }
            }
        };

        auto augment_path = [&](int s) {
            fill(used.begin(), used.end(), -1);
            fill(p.begin(), p.end(), -1);
            for (int i = 0; i < n; ++i) base[i] = i;

            queue<int> q;
            q.push(s);
            used[s] = 0;

            while (!q.empty()) {
                int u = q.front();
                q.pop();

                for (int v : adj[u]) {
                    if (base[u] == base[v] || match[u] == v) continue;
                    if (v == s || (match[v] != -1 && p[match[v]] != -1)) {
                        int l = lca(u, v);
                        fill(blossom.begin(), blossom.end(), false);
                        mark_blossom(l, u, q);
                        mark_blossom(l, v, q);
                        for (int i = 0; i < n; ++i) {
                            if (blossom[base[i]]) {
                                base[i] = l;
                            }
                        }
                    } else if (p[v] == -1) {
                        p[v] = u;
                        if (match[v] == -1) {
                            for (int curr = v; curr != -1; ) {
                                int prev_u = p[curr];
                                int next_curr = match[prev_u];
                                match[curr] = prev_u;
                                match[prev_u] = curr;
                                curr = next_curr;
                            }
                            return true;
                        }
                        int next_v = match[v];
                        p[next_v] = v;
                        used[next_v] = 0;
                        q.push(next_v);
                    }
                }
            }
            return false;
        };

        int max_matching = 0;
        for (int i = 0; i < n; ++i) {
            if (match[i] == -1) {
                if (augment_path(i)) {
                    max_matching++;
                }
            }
        }

        return max_matching;
    }
};