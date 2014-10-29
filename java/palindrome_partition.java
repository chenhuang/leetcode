import java.util.*;

public class palindrome_partition {
    public ArrayList<ArrayList<String>> partition(String s) {
        return partition_rec(s,new ArrayList<String>());
    }
    
    public boolean isValid(String s) {
        for (int i = 0; i < s.length()/2; i++) {
            if (s.charAt(i) != s.charAt(s.length()-i-1)){
                    return false;
            }
        }
        return true;
    }
    
    public ArrayList<ArrayList<String>> partition_rec(String s, ArrayList<String> record) {

        ArrayList<ArrayList<String>> result = new ArrayList<ArrayList<String>>();
        if (s.length() == 0) {
            result.add(record);
        } else {
            for (int i = 1; i <= s.length(); i++) {
                if (isValid(s.substring(0,i)))  {
                    ArrayList<String> new_record = new ArrayList<String>(record);
                    new_record.add(s.substring(0,i));
                    ArrayList<ArrayList<String>> subresult = partition_rec(s.substring(i,s.length()),new_record);
                    for (int j = 0; j < subresult.size(); j++) {
                        result.add(subresult.get(j));
                    }
                }
            }
        }
        
        return result;
    }
    

    public static void main(String[] args) {
        palindrome_partition p = new palindrome_partition();
        ArrayList<ArrayList<String>> result = p.partition("bb");
        System.out.println(result.size());
        for (int i = 0; i < result.size(); i++) {
            System.out.println(result.get(i));
        }
    }
}
