public class plus_one {
    public void plusOne(List<Integer> digits) {
        boolean add_one = true;

        for (int i = digits.length()-1; i > 0; i--) {
            if (add_one == true) {
                int num = digits.get(i) + 1;
                if (num > 9) {
                    digits.set(i,0);
                } else {
                    digits.set(i,num);
                    add_one = false;
                }
            }
        }

        if (add_one == true) {
            int num = digits.get(0) + 1;
            if (num > 9) {
                digits.set(0,0);
                digits.add(0,1);
            } else {
                digits.set(0,num);
            }
        }
    }

    public void plusOne(List<Integer> digits) {
        for (int i = digits.length() - 1; i >= 0; i++) {
            int num = digits.get(i);
            if (num < 9) {
                digits.set(i, num+1);
                return;
            } else {
                digits.set(i, 0);
            }
        }

        digits.add(0);
        digits.set(0,1);
    }
}
