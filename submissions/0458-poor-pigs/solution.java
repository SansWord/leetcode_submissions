public class Solution {
    public int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
        if(buckets <= 1) {
            return 0;
        }
        int round = minutesToTest / minutesToDie;
        int maxPerRound = round+1;
        int current = 1;
        int n = 1;
        while (true) {
            current *= maxPerRound;
            if (current >= buckets) {
                return n;
            }
            n++;
        }
    }
}
