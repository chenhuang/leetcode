/*
* 
*   Given a sorted integer array where the range of elements are [0, 99] inclusive, return its missing ranges.
*   For example, given [0, 1, 3, 50, 75], return [“2”, “4->49”, “51->74”, “76->99”]
*
*   Because the range is fixed, one approach could be iterate from 0 to 99, and identify all missing elements, then merge continuous elements. Two pass could do it. 
*   Note that the two passes could be merged: every time a element is found, it will be compared with it's previous missing elements and if it's not continuous, output previous range pair and intialize a new node pair. 
*/

//O(min(vals[-1]-end)+min(vals[0], start))
public class find_missing_ranges {
    public List<String> findMissingRanges(int[] vals, int start, int end) {
        List<String> output = new ArrayList<String>();
        if (vals.length == 0) {
            output.add(start+"->"+end);     
            return output
        }

        int NULL_VALUE = vals[0] - 2;
        int range_left = NULL_VALUE, range_right = NULL_VALUE;

        int i = start;
        int j = 0;
        while (i < end+1) {
            if (j < vals.length && i <= vals[j]) {
                if (range_left == NULL_VALUE) {
                    range_left = i;
                    range_right = i;
                } else {
                    if (i == range_right+1) {
                        range_right = i;
                    } else {
                        if (range_left != range_right) {
                            output.add(range_left+"->"+range_right);
                        } else {
                            output.add(new String(range_left));
                        }
                        range_left = i;
                        range_righ = i;
                    }
                }
                i++;
            } else {
                if (j > vals.length-1) {
                    output.add(i+"->"+end);
                    return output;
                } else {
                    j++;
                }
            }
        }
        return output;
    }

    public List<String> findMissingRangesII(int[] vals, int start, int end) {
        List<Strings> ranges = new ArrayList<>();
        int prev = start - 1;
        for (int i = 0; i <= vals.length; i++) {
            int curr = (i == vals.length) ? end + 1 : vals[i];
            if (curr - prev >= 2) {
                ranges.add(getRange(prev + 1, curr - 1));
            }
            prev = curr;
        }
        return ranges;
    }

    private String getRange(int from, int to) {
        return (from == to) ? String.valueOf(from) : from + "->" + to;
    }

/* Python code would be a lot easier: time: O((start-end+1)*n)
 * output = []
 * last_pair = [start-2, start-2]
 * for i in range(start, end+1):
 *  if i not in vals:
 *      if last_pair[1] == i - 1: 
 *          last_pair[1] = i
 *      else:
 *         if last_pair[0] == last_pair[1]:
 *              output.append(last_pair[0])
 *         else:
 *              output.append(last_pair[0]+"->"+last_pair[1])
*          last_pair = [i,i]
 *         
 *  return output 
 * */

}
