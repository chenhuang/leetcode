public class min_stack {
    private Stack<Integer> stack = new Stack<>();
    private Stack<Integer> minStack = new Stack<>();

    public boolean push(x) {
       if (x <= minStack.peek() || minStack.isEmpty()) minStack.push(x);
       return stack.push(x); 
    }

    public int pop() {
        if (stack.isEmpty()) return null;
        if (stack.peek().equals(minStack.peek())) {
            minStack.pop();
        } 
        return stack.pop();
    }

    public int top() {
        if (stack.isEmpty()) return null;
        return stack.peek();
    }
    
    public int getMin() {
        if (stack.isEmpty()) return null;
        return minStack.peek();
    }
}

