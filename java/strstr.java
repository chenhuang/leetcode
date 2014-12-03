public class strstr {

    public int strstr(String source, String target) {
        int source_len = source.length();
        int target_len = target.length();

        for (int i = 0; i < target_len - source_len; i++) {
            if (isEqual(source, target, i)) {
                return i;
            }
        }

        return -1;
    }

    public boolean isEqual(String source, String target, int index) {
        for (int i = index; i < index+source.length(); i++) {
            if (source.charAt(i-index) != target.charAt(i)) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        strstr ss = new strstr();
        System.out.println(ss.strstr("issi","mississippi"));
        System.out.println(ss.strstr("mississippi","issi"));
    }

}
