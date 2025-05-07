from __init__ import install
try:
    import graphviz
except ModuleNotFoundError:
    install("graphviz") if input("graphviz is not installed\n install?(y/N)").lower()=='y' else exit(0)
    import graphviz

def visualize_tree(tree,name='decision_tree',view=True,format='png'):
    tree=__visualize_tree(tree)
    tree.render(name,view=view,format=format)

def __visualize_tree(tree, graph=None, node_id=0):
    if graph is None:
         graph = graphviz.Digraph(comment='Decision Tree', graph_attr={'rankdir': 'TB'})
    if type(tree)==str:
         graph.node(str(node_id), label=f"Class: {tree}")
    else:
         graph.node(str(node_id), label=f"Feature: {tree['Label']}\nThreshold: {tree['val']}\n Gini:{tree['gini']}")
         left_child_id = node_id * 2 + 1
         right_child_id = node_id * 2 + 2
         graph.edge(str(node_id), str(left_child_id), label='Left')
         graph.edge(str(node_id), str(right_child_id), label='Right')
         __visualize_tree(tree['Left'], graph, left_child_id)
         __visualize_tree(tree['Right'], graph, right_child_id)
    return graph

if __name__=='__main__':
    tree = {
       'Label': 'feature1', 'val': 0.5,'gini':0.5,
       'Left': {
            'Label': 'feature2', 'val': 0.3,'gini':0.4,
           'Left': "yes",
           'Right': "no"
       },
       'Right': "yes"
   }
    visualize_tree(tree)
