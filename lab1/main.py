import codecs
import functools
import graphviz as gv

# files = ["morze.csv"]
files = ["morze.csv", "ocean.csv", "spokojny.csv", "woda.csv"]


def add_nodes(graph, nodes):
    for n in nodes:
        if isinstance(n, tuple):
            graph.node(n[0], **n[1])
        else:
            graph.node(n)
    return graph


def add_edges(graph, edges):
    for e in edges:
        if isinstance(e[0], tuple):
            graph.edge(*e[0], **e[1])
        else:
            graph.edge(*e)
    return graph


styles = {
    'graph': {
        'label': 'A Fancy Graph',
        'fontsize': '16',
        'fontcolor': 'white',
        'bgcolor': '#333333',
        'rankdir': 'BT',
    },
    'nodes': {
        'fontname': 'Helvetica',
        'shape': 'hexagon',
        'fontcolor': 'white',
        'color': 'white',
        'style': 'filled',
        'fillcolor': '#006699',
    },
    'edges': {
        'style': 'dashed',
        'color': 'white',
        'arrowhead': 'open',
        'fontname': 'Courier',
        'fontsize': '12',
        'fontcolor': 'white',
    }
}


def apply_styles(graph, styles):
    graph.graph_attr.update(
        ('graph' in styles and styles['graph']) or {}
    )
    graph.node_attr.update(
        ('nodes' in styles and styles['nodes']) or {}
    )
    graph.edge_attr.update(
        ('edges' in styles and styles['edges']) or {}
    )
    return graph


main_nodes_names = list(map(lambda x: x.split(".")[0], files))
# main_nodes_names = ["morze"]


def create_graph(nodes_list, edged, main_node):
    graph_with_nodes = add_nodes(gv.Graph(format='svg', engine='twopi', graph_attr={"root": str(main_node), "ranksep": "15"}),
                                 nodes_list)
    full = add_edges(graph_with_nodes, edged)

    styled = apply_styles(full, styles)
    return styled


for main_node in main_nodes_names:
    nodes_set = set()
    edges = []

    for file in files:

        current_main_node_node = file.split(".")[0]
        for line in codecs.open("resources/" + file, 'r', 'utf-8'):
            if not line.startswith("1,") and "PUSTE" not in line:
                splitted = line.split(",")
                value = int(splitted[0])
                word = splitted[1]
                if not main_node == word:
                    nodes_set.add(word)
                edges.append(((current_main_node_node, word), {'label': str(900 / value)}))
        # nodes_list = list(map(lambda x: (x, {"label": ""}), nodes_set))
        nodes_list = list(nodes_set)
        # nodes_list.append((main_node, {"root": "True"}))
        nodes_list.append(main_node)

    g = create_graph(nodes_list, edges, main_node)
    g.render(filename='img/full_' + main_node)

# print()
#
# graph = functools.partial(gv.Graph, format='svg', layout='circo')
#
# graph_with_nodes = add_nodes(gv.Graph(format='svg'), nodes_set)
# full = add_edges(graph_with_nodes, edges)
#
# styled = apply_styles(full, styles)
#
# styled.render(filename='img/full')

