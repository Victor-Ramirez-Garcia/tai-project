from typing import List, Dict, Tuple

class TrieNode:
    def __init__(self, name: str = ""):
        self.name: str = name
        # Using a sorted dict (via sorting keys later) or a dict where we iterate in sorted order.
        # Since Python 3.7+ dicts preserve insertion order, we can sort keys when serializing.
        self.children: Dict[str, 'TrieNode'] = {}
        self.is_deleted: bool = False

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        # Step 1: Build the Trie
        root = TrieNode()
        for path in paths:
            curr = root
            for folder in path:
                if folder not in curr.children:
                    curr.children[folder] = TrieNode(folder)
                curr = curr.children[folder]
                
        # Keep track of the structure serialized strings and the nodes that share them
        seen_structures: Dict[str, List[TrieNode]] = {}
        
        # Step 2: Serialize the subtree structure using Post-Order Traversal
        def serialize(node: TrieNode) -> str:
            if not node.children:
                return ""
            
            # Subfolders must be processed in a deterministic order (alphabetical)
            sub_serializations = []
            for child_name in sorted(node.children.keys()):
                child_str = serialize(node.children[child_name])
                sub_serializations.append(f"{child_name}({child_str})")
            
            # Combine the subfolder structures into a unique representation for the current node
            structure_str = ",".join(sub_serializations)
            
            # Register this structure to find duplicates
            if structure_str not in seen_structures:
                seen_structures[structure_str] = []
            seen_structures[structure_str].append(node)
            
            return structure_str
            
        serialize(root)
        
        # Step 3: Mark identical folders for deletion
        # Only folders with at least one subfolder (non-empty structure) can be duplicates
        for structure_str, nodes in seen_structures.items():
            if len(nodes) > 1:
                for node in nodes:
                    node.is_deleted = True
                    
        # Step 4: Construct the remaining paths using Pre-Order Traversal
        ans: List[List[str]] = []
        
        def collect_paths(node: TrieNode, current_path: List[str]) -> None:
            # If marked for deletion, skip this node and all of its subfolders
            if node.is_deleted:
                return
            
            # If it's not the root node, add its path to the final answer
            if node.name:
                current_path.append(node.name)
                ans.append(list(current_path))
                
            # Recurse for all children
            for child_name in node.children:
                collect_paths(node.children[child_name], current_path)
                
            # Backtrack
            if node.name:
                current_path.pop()
                
        collect_paths(root, [])
        return ans