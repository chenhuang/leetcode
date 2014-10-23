import java.util.LinkedList;
// Implement a int hash function using open hasing basically a linkedlist


public class hash {
    private ArrayList<LinkedList<int>> values = new ArrayList<LinkedList<int>>(100);
    private int HASH_TABLE_SIZE;

    public hash(int size) {
        HASH_TABLE_SIZE = size;
        values = new ArrayList<LinkedList<int>>(size);
    }

    public boolean insert(String key, int value) {
        int hashed_key = hashfunc(key);
        if (values.get(hashed_key) == null) {
            values.add(hashed_key, new LinkedList<int>());
        }

        LinkedList<int> list = values.get(hashed_key);
        list.add(value);
    }

    public boolean delete(int value) {

    }

    public boolean find(int value) {

    }
  
    private int hashfunc(String key) {
        //return md5(key)%hash_table_size;
        int sum = 0;
        for (int i = 0; i < key.length(); i++) {
            sum = sum * 33 + (int)(key.charAt(i));
        }
        sum = sum % HASH_TABLE_SIZE;
        return sum;
    }


public static void main(String[] args) {

    }
}
