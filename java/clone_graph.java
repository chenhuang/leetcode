public class clone_graph {
    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        if (node == null) return null;
        Map<UndirectedGraphNode, UndirectedGraphnode> nodeMap = new HashMap<>(); // Here the initialization is using new syntax
        Queue<UndirectedGraphNode> q = new LinkedList<>(); // Here the Queue interface is intialized using LinkedList, operations include: add, poll, isEmpty
        q.add(node);
        UndirectedGraphNode graphCopy = new UndirectedGraphNode(graph.label);
        map.put(node, graphCopy);

        while (!q.isEmpty()) {
            UndirectedGraphNode node = q.poll();
            for (UndirectedGraphNode neighbor : node.neighbors) {
                if (map.containKeys(neighbor)) {
                    map.get(node).neighbors.add(map.get(neighbor));
                } else {
                    UndirectedGraphNode neighborCopy = new UndirectedGraphNode(neighbor.label);
                    map.get(node).neighbors.add(neighborCopy);
                    map.put(neighbor, neighborCopy);
                    q.add(neighbor);
                }
            }
        }

        return graphCopy; 
    }
}
