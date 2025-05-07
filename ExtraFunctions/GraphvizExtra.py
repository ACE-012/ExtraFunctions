from . import install
try:
    import graphviz
except ModuleNotFoundError:
    install("graphviz") if input("graphviz is not installed\n install?(y/N)").lower()=='y' else exit(0)
    import graphviz

def visualize_tree(tree:dict,name='decision_tree',view=True,format='png',branch=['Left','Right'],attributes:list=[]):
    graph=__visualize_tree(tree,branch,attributes)
    graph.render(name,view=view,format=format)

def __visualize_tree(tree:dict,branch:list[str],attributes:list[str],graph=None,node_id=0)->graphviz.Digraph:
    if graph is None:
         graph = graphviz.Digraph(comment='Decision Tree', graph_attr={'rankdir': 'TB'})
    if type(tree)!=dict:
         graph.node(str(node_id), label=f"Class: {tree}")
    else:
        features=""
        for each in attributes:
            features+=f"{each}: {tree[each]}\n"
        graph.node(str(node_id), label=features)
        child_id = node_id * 2 + 1
        for each in branch:
            if tree[each]!=-1:
                graph.edge(str(node_id), str(child_id))
                __visualize_tree(tree[each],branch,attributes, graph,child_id)
                child_id+=1
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
