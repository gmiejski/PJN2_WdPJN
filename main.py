import codecs
import functools
import graphviz as gv

# files = ["morze.csv"]
files = ["morze.csv", "ocean.csv", "spokojny.csv", "woda.csv"]

nodes = set()
edges = []

for file in files:
    mainNodeName = file.split(".")[0]
    nodes.add(mainNodeName)
    for line in codecs.open("resources/" + file, 'r', 'utf-8'):
        if not line.startswith("1,") and "PUSTE" not in line:
            print(line)
            splitted = line.split(",")
            value = int(splitted[0])
            word = splitted[1]
            nodes.add(word)
            edges.append(((mainNodeName, word), {'label': str(900 / value)}))

print()


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


graph = functools.partial(gv.Graph, format='svg')

graph_with_nodes = add_nodes(gv.Graph(format='svg'), nodes)
full = add_edges(graph_with_nodes, edges)

styled = apply_styles(full, styles)

styled.render(filename='img/full')