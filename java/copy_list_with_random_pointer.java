public class copy_list_with_random_pointer {
    public RandomListNode copyRandomList(RandomListNode head) {
        Map<RandomListNode, RandomListNode> nodeMap = new HashMap<,>();

        RandomListNode cur = head;
        RandomListNode dummyHead = new RandomListNode();
        RandomListNode dummycur = dummyHead;

        while (cur != null) {
           dummycur.val = cur.val;
           nodeMap.put(cur, dummycur);
           dummycur.next = new RandomListNode();
           dummycur = dummycur.next;
           cur = cur.next;
        }

        dummycur = dummyHead;
        cur = head;

        while (cur != null) {
            if nodeMap.hasKey(cur.random) {
                dummycur.random = nodeMap.get(cur.random);
            }
            dummycur = dummycur.next;
            cur = cur.next;
        }

        return dummyHead;
    }
}
