public class valid_parenthese {
    private Map<char, char> parenthesePair = new HashMap<>(){{
put("(",")");
put("{","}");
put("[","]");
}}

    public boolean isValid(String input) {
        Stack<String> stack = new Stack<>();
        for (char i : input.toCharArray()) {
            if (parenthesePair.containsKey(i)) {
               stack.push(i); 
            } else {
                if (stack.isEmpty() || parenthesePair.get(stack.pop()) != i) return false;
            }
        }

        return stack.isEmpty();
    }
}
