from typing import List, Dict
from collections import defaultdict

class TrieNode:
    def __init__(self):
        # Maps folder name to its corresponding TrieNode child
        self.children: Dict[str, TrieNode] = {}
        # Stores the serialized sub-tree representation of this node
        self.serial: str = ""
        # Flag to mark if this folder/node should be deleted
        self.deleted: bool = False

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = TrieNode()
        
        # 1. Build the Trie from the given paths.
        # Sorting ensures that children are processed in lexicographical order later.
        for path in sorted(paths):
            curr = root
            for folder in path:
                if folder not in curr.children:
                    curr.children[folder] = TrieNode()
                curr = curr.children[folder]
                
        # Map to store the frequency of each unique sub-tree serialization
        serial_count = defaultdict(int)
        # Map to store all nodes that share a particular sub-tree serialization
        serial_to_nodes = defaultdict(list)
        
        # 2. Post-order DFS to serialize the sub-tree structure of each node.
        def serialize(node: TrieNode) -> str:
            if not node.children:
                return ""
            
            # Since paths were sorted, iterating over keys directly preserves order.
            # Otherwise, sorted(node.children.keys()) would be required.
            sub_serials = []
            for name, child in node.children.items():
                child_serial = serialize(child)
                sub_serials.append(f"{name}({child_serial})")
                
            # Combine the serialized sub-trees of all children
            node.serial = "".join(sub_serials)
            
            # Track serialization frequencies for non-empty sub-trees
            serial_count[node.serial] += 1
            serial_to_nodes[node.serial].append(node)
            
            return node.serial
            
        serialize(root)
        
        # 3. Mark duplicate folders for deletion.
        # Folders are identical if they have the same non-empty sub-tree structure.
        for serial, count in serial_count.items():
            if count > 1:
                for node in serial_to_nodes[serial]:
                    node.deleted = True
                    
        ans = []
        
        # 4. Deep DFS to reconstruct valid paths that haven't been deleted.
        def construct_paths(node: TrieNode, current_path: List[str]):
            # If a folder is marked deleted, its entire sub-tree is pruned/ignored.
            if node.deleted:
                return
                
            if current_path:
                ans.append(list(current_path))
                
            for name, child in node.children.items():
                current_path.append(name)
                construct_paths(child, current_path)
                current_path.pop()
                
        construct_paths(root, [])
        return ans