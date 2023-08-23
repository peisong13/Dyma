def sort_file_by_ids(nodes: list) -> list:
    ''' sort respones nodes by ids, sequence in `children` is the right order'''
    # 1. add 'sorted_children_nodes' to each node if 'children' is not empty
    sorted_nodes = [node if node.get('children') is None else node | {'sort_children_nodes': []} for node in nodes]

    # 2. move nodes to 'sort_children_nodes' if its id is in 'children', delete node after move # TODO: change this, not reliable
    for node in sorted_nodes:
        if node.get('children') is None:
            continue
        for child in node['children']:
            for i, n in enumerate(sorted_nodes):
                if n['id'] == child:
                    node['sort_children_nodes'].append(n)
                    del sorted_nodes[i]
                    break
    
    return sorted_nodes

