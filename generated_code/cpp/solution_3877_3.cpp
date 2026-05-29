#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int score(vector<string>& cards, char x) {
        // Filter cards that contain the character 'x'
        vector<string> valid_cards;
        for (const string& card : cards) {
            if (card[0] == x || card[1] == x) {
                valid_cards.push_back(card);
            }
        }

        // Separate cards into two sets based on whether they are identical to "xx"
        // or contain exactly one 'x'.
        // Case 1: "xx"
        // Case 2: "ax" or "xa" where a != x
        int xx_count = 0;
        unordered_map<char, int> other_counts;

        for (const string& card : valid_cards) {
            if (card[0] == x && card[1] == x) {
                xx_count++;
            } else {
                // Find the character that is not 'x'
                char other = (card[0] == x) ? card[1] : card[0];
                other_counts[other]++;
            }
        }

        int points = 0;

        // Pair up the "ax" and "xa" cards that share the same non-x character.
        // For a fixed character 'a' (!= x), any card like "ax" or "xa" contains 'x' and 'a'.
        // Two such cards differ in exactly 1 position if and only if they are NOT identical.
        // Wait, the definition of compatible is "differ in exactly 1 position".
        // If we have "ax" and "xa", they differ in both positions (pos 0: a vs x, pos 1: x vs a).
        // If we have "ax" and "bx", they differ in 1 position (pos 0).
        // Let's re-evaluate compatibility for 2-letter cards containing 'x':
        // Type A: "xx"
        // Type B: "ax" (where a != x)
        // Type C: "xa" (where a != x)
        //
        // Compatibility matrix:
        // 1. "xx" and "xx": differ in 0 positions -> NOT compatible.
        // 2. "xx" and "ax": differ in 1 position (pos 0) -> COMPATIBLE.
        // 3. "xx" and "xa": differ in 1 position (pos 1) -> COMPATIBLE.
        // 4. "ax" and "bx" (a != b): differ in 1 position (pos 0) -> COMPATIBLE.
        // 5. "ax" and "ay": differ in 0 positions if x==y (same card), or if "ax" and "ax" -> 0 positions.
        // 6. "xa" and "xb" (a != b): differ in 1 position (pos 1) -> COMPATIBLE.
        // 7. "ax" and "xa": differ in 2 positions -> NOT compatible.
        // 8. "ax" and "xb" (a != b): differ in 2 positions -> NOT compatible.
        //
        // This forms a graph matching problem. Since the graph structure depends on positions:
        // Let's group non-"xx" cards by their format:
        // Left-x group: "xa" cards, indexed by 'a'
        // Right-x group: "ax" cards, indexed by 'a'
        //
        // Connections:
        // - "xx" can connect to ANY "xa" or "ax".
        // - Any "ax" can connect to any "bx" (a != b). This means all "ax" cards form a complete graph 
        //   except loops (self-matching isn't allowed, identical cards aren't compatible).
        // - Any "xa" can connect to any "xb" (a != b).
        
        // Let's count frequencies of each unique card string to fully model the multi-graph.
        unordered_map<string, int> counts;
        for (const string& card : valid_cards) {
            counts[card]++;
        }

        // This is a Maximum General Graph Matching problem. Given the constraints of typical 
        // LeetCode problems and the small alphabet (26 lowercase letters), the number of unique 
        // nodes (card types) is at most 26 * 26 = 676, or rather just the ones containing 'x':
        // "xx" (1 type), "ax" (25 types), "xa" (25 types). Total 51 unique card types.
        // Since it's a small graph, we can use a randomized multi-matching approach or 
        // Tutte matrix / Blossom algorithm, or dynamic programming/max flow if bipartite.
        // Notice that "ax" and "bx" are compatible, "xa" and "xb" are compatible. 
        // This is not strictly bipartite.
        // However, we can use a backtracking search with memoization or a greedy approach if applicable,
        // or standard Blossom algorithm for maximum matching.
        
        // Given this is a standard competitive programming template, let's implement a simple 
        // Edmonds' Blossom algorithm or a randomized greedy matching (Max Cardinality Matching) 
        // since the state space of remaining cards can be represented if counts are small, 
        // or we can explicitly build the adjacency matrix of available individual cards.
        
        // Let's unroll all valid cards into an explicit list of vertices.
        // The total number of cards could be up to 10^5 (implied by standard constraints).
        // If N is large, Blossom algorithm on individual cards O(V^3) will TLE.
        // We must optimize based on the specific structure of the components.
        
        // Let's analyze the components:
        // Total "ax" cards can all be matched with each other, provided they have different 'a'.
        // Total "xa" cards can all be matched with each other, provided they have different 'a'.
        // "xx" can match with any "ax" or "xa".
        
        // Let's do a greedy approach or state reduction.
        // Actually, we can count:
        // L[c] = count of "xc" where c != x
        // R[c] = count of "cx" where c != x
        // num_xx = count of "xx"
        
        // For the Left group ("xc"): any two cards with different characters can match.
        // This is equivalent to the problem: given buckets of items, match items from different buckets.
        // For the Right group ("cx"): same thing.
        // "xx" can match with any item from Left or Right group.
        
        // Let's count total items in Left group: sum(L[c])
        // Max bucket size in Left group: max(L[c])
        // If we just match within Left group: max pairs we can form is min(sum(L)/2, sum(L) - max(L)).
        // Any leftovers must be from the majority bucket (if max(L) > sum(L)/2), and they are identical 
        // cards (e.g., multiple "xa"s), which cannot match with each other.
        // These leftovers can, however, match with "xx".
        
        // Let's formalize the matching between groups:
        // Left group leftovers can match with "xx".
        // Right group leftovers can match with "xx".
        // Also, "xx" can just match with ANY element of Left or Right group to assist.
        
        // Let's count frequencies:
        vector<int> L(26, 0);
        vector<int> R(26, 0);
        int xx = 0;
        
        for (const string& card : cards) {
            if (card[0] == x && card[1] == x) {
                xx++;
            } else if (card[0] == x) {
                L[card[1] - 'a']++;
            } else if (card[1] == x) {
                R[card[0] - 'a']++;
            }
        }
        
        int sum_L = 0, max_L = 0;
        for (int c : L) {
            sum_L += c;
            max_L = max(max_L, c);
        }
        
        int sum_R = 0, max_R = 0;
        for (int c : R) {
            sum_R += c;
            max_R = max(max_R, c);
        }
        
        // Internal matching within L:
        // We can form pairs of distinct elements. 
        // Leftover elements that cannot be paired within L because they belong to the same majority bucket:
        int leftover_L = max(0, 2 * max_L - sum_L);
        // Elements successfully paired internally in L:
        int paired_L = (sum_L - leftover_L) / 2;
        // Note: if sum_L - leftover_L is odd, one element is left over but it can't pair with the majority.
        // Actually, if sum_L is odd and max_L <= sum_L/2, leftover_L is 0, but 1 element remains unpaired.
        // So total unpaired elements from L after maximizing internal pairs:
        int unpaired_L = sum_L - 2 * paired_L; 
        // These unpaired_L elements contain 'leftover_L' elements of the majority character, 
        // and at most 1 element of another character (if sum_L is odd and max_L <= sum_L/2).
        
        // Similarly for R:
        int leftover_R = max(0, 2 * max_R - sum_R);
        int paired_R = (sum_R - leftover_R) / 2;
        int unpaired_R = sum_R - 2 * paired_R;
        
        points += paired_L + paired_R;
        
        // Now we have unpaired_L elements from L, unpaired_R elements from R, and xx elements of "xx".
        // "xx" can pair with ANY element from L or R.
        // Can the unpaired elements from L pair with unpaired elements from R?
        // No, because "xc" and "dy" are not compatible (differ in both positions).
        // Can they pair with "xx"? Yes.
        
        // So we can use "xx" to clear out unpaired_L and unpaired_R elements.
        // Each "xx" can pair with 1 element from L or R.
        int match_with_xx = min(xx, unpaired_L + unpaired_R);
        points += match_with_xx;
        xx -= match_with_xx;
        
        // If there are still "xx" left, they cannot pair with each other. 
        // But we could potentially break one internal pair in L or R (which frees up 2 elements) 
        // to pair them with 2 "xx" cards, increasing the total pairs by 1 (since 2 "xx" + 2 elements = 2 pairs, 
        // whereas before we had 1 internal pair and 2 unused "xx" = 1 pair).
        // Let's see if this trade-off is beneficial:
        // Breaking 1 internal pair reduces points by 1, frees 2 elements. 
        // If we have at least 2 "xx" left, we can form 2 new pairs with "xx", gaining 2 points.
        // Net gain: +1 point.
        // We can do this as long as we have internal pairs and at least 2 "xx" cards.
        if (xx >= 2) {
            // Elements freed from L must be able to pair with "xx". Any element from L can pair with "xx".
            // So we can just break pairs from L and R.
            int pairs_to_break = min(paired_L + paired_R, xx / 2);
            points += pairs_to_break;
        }
        
        return points;
    }
};