public class evaluate_reverse_polish_notation {
    public int RPN(String[] input) {
        if (input.length == 0) return null; 
        Stack<Integer> stack = new Stack<>();
        
        for (String i : input) {
            if (i.equals("+")) {
                stack.push(stack.pop()+stack.pop());
            } else if (i.equals("-")) {
                stack.push((stack.pop()-stack.pop())*-1);
            } else if (i.equals("*")) {
                stack.push(stack.pop() * stack.pop());
            } else if (i.equals("/")) {
                int denominator = stack.pop();
                stack.push(stack.pop()/denominator);
            } else {
                stack.push(int(i));
            }
        }

        return stack.pop();
    }

    private static final Set<String> OPERATORS = new HashSet<>(Array.asList("+","-","*","/"));
    
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        for (String token : tokens) {
            if (OPERATORS.contains(token)) {
                int y = stack.pop();
                int x = stack.pop();
                stack.push(Integer.parseInt(token));
            } else {
                stack.push(Integer.parseInt(token));
            }
        }
        return stack.pop();
    }
    
    private int eval(int x, int y, String operator) {
        switch (operator) {
            case "+": return x + y;
            case "-": return x - y;
            case "*": return x * y;
            case "/": return x / y;
        }
    }

// Very cool implementation of interface operator
    interface Operator {
        int eval(int x, int y);
    }

    private static final Map<String, Operator> OPERATORS = new HashMap<String, Operator>() {{
put("+", new Operator(){
    public int eval(int x, int y) return x + y;
});
put("-", new Operator() {
    public int eval(int x, int y) return x - y;
});
put("*", new Operator() {
    public int eval(int x, int y) return x * y;
});
put("/", new Operator() {
    public int eval(int x, int y) return x / y;
});
}};

public int evalRPNII(String[] tokens) {
    Stack<Integer> stack = new Stack<>();
    for (String token : tokens) {
        if (OPERATORS.containsKey(token)) {
            int y = stack.pop();
            int x = stack.pop();
            stack.push(OPERATORS.get(token).eval(x, y));
        } else {
            stack.push(Integer.parseInt(token));
        }

    }

    return stack.pop();
}

}
