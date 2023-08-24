def find_all_children(node: dict, all_nodes: list[dict]) -> dict:

    ''' find all children of a node, return node with all of its children '''

    if not node.get('children'):
        return node
    else:
        children_node = []
        for child in node.get('children'):
            for n in all_nodes:
                if n.get('id') == child:
                    children_node.append(find_all_children(n, all_nodes))
                    break
        node_with_children = node | {'children_node': children_node} # add children_node to node
        return node_with_children
    
def sort_file_by_ids(nodes: list[dict], root_id='root') -> dict:

    ''' sort respones nodes by ids, sequence in `children` is the right order'''
    
    # find the root node, and recursively find its children
    for node in nodes:
        if node.get('id') == root_id:
            sorted_nodes = find_all_children(node, nodes)
            break
    return sorted_nodes




# if __name__ == '__main__':
#     import json
#     with open('inbox.json', 'r', encoding='utf-8') as f:
#         nodes = json.load(f)
    
#     sorted_nodes = sort_file_by_ids(nodes)
#     with open('inbox_sorted.json', 'w', encoding='utf-8') as f:
#         json.dump(sorted_nodes, f, ensure_ascii=False, indent=4)

