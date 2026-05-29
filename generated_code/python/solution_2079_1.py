from typing import List, Dict, Optional

class TrieNode:
    def __init__(self, name: str = ""):
        self.name: str = name
        # Use a dictionary sorted by keys (or sorted during traversal) to represent subfolders.
        # Python 3.7+ preserves insertion order, but we explicitly sort keys during serialization.
        self.children: Dict[str, 'TrieNode'] = {}
        self.is_deleted: bool = False

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = TrieNode()
        
        # Step 1: Build the Trie from the given paths.
        # Sort paths first to ensure a consistent, deterministic construction sequence if needed,
        # though sorting during serialization handles correctness.
        for path in paths:
            curr = root
            for folder in path:
                if folder not in curr.children:
                    curr.children[folder] = TrieNode(folder)
                curr = curr.children[folder]
                
        # Store serialized sub-tree representations to find duplicates.
        # Map: serialization_string -> list of nodes having this structure.
        seen: Dict[str, List[TrieNode]] = {}
        
        # Step 2: Post-order traversal to serialize each subfolder's structure.
        def serialize(node: TrieNode) -> str:
            if not node.children:
                return ""
            
            # Serialize all child sub-trees. Sorting the keys is CRITICAL to ensure
            # that structural identity is independent of the order paths were processed.
            sub_serials = []
            for child_name in sorted(node.children.keys()):
                child_serial = serialize(node.children[child_name])
                sub_serials.append(f"{child_name}({child_serial})")
                
            # Combine child serials into the current node's structure profile.
            serial_str = ",".join(sub_serials)
            
            # Group nodes by their structural signature.
            if serial_str:
                if serial_str not in seen:
                    seen[serial_str] = []
                seen[serial_str].append(node)
                
            return serial_str

        serialize(root)
        
        # Step 3: Identify and mark duplicate folders for deletion.
        # According to the problem, if two or more folders have the identical 
        # non-empty subfolder structure, they must be deleted.
        for serial, nodes in seen.items():
            if len(nodes) > 1:
                for node in nodes:
                    node.is_deleted = True
                    
        ans: List[List[str]] = []
        
        # Step 4: Construct the final answer by traversing non-deleted paths.
        # If a parent is deleted, all its subfolders are implicitly deleted/unreachable.
        def construct_paths(node: TrieNode, current_path: List[str]) -> None:
            for child_name, child_node in node.children.items():
                if not child_node.is_deleted:
                    current_path.append(child_name)
                    ans.append(list(current_path))
                    construct_paths(child_node, current_path)
                    current_path.pop()
                    
        construct_paths(root, [])
        return ans