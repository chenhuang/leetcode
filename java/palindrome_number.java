public class palindrome_number {
    public boolean palindrom(int num) {
       // determine lenght of the number 
       int length = 1;
       while (num/length > 9) length *= 10; // 121/1 > 9, 121/10 > 9, 121/100 < 9
       while (num > 9) { // 121
            if (num/length == num % 10) { // 1 == 1,
                num = num % length; // 21
                num = num/10; // 2
                length /= 100; // 1
            } else {
                return false;
            }
       }
       return true;
    }

    public static void main(String[] args) {
        palindrome_number pn = new palindrome_number();
        System.out.println(pn.palindrom(121));
        System.out.println(pn.palindrom(1));
        System.out.println(pn.palindrom(11));
        System.out.println(pn.palindrom(123));
    }
}
