public class Solution{
    public RandomListNode copyRandomList(RandomListNode head) {
        if (head == null) {
            return null;
        }


        // stores the mapping between 
        HashMap<RandomListNode, RandomListNode> map = new HashMap<RandomListNode, RandomListNode>();
        RandomListNode dummy = new RandomListNode(0);
        RandomListNode pre = dummy, newNode;

        while (head != null) {
            if (map.containsKey(head)) {
                newNode = map.get(head);
            } else {
                newNode = new RandomListNode(head.label);
                map.put(head, newNode);
            }
            pre.next = newNode;
            
            if (head.random != null) {
                if (map.containsKey(head.random)) {
                    newNode.random = map.get(head.random); 
                } else {
                    newNode.random = new RandomListNode(head.random.val);
                    map.put(head.random,newNode.random);
                }
            }

            pre = pre.next
            head = head.next
        }

        return dummy.next
    }
}
