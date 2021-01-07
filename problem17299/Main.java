import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());
        int[] numI = new int[num];
        int[] ans = new int[num];
        int[] f = new int[100000001];
        String[] temp = br.readLine().split(" ");
        
        for (int i=0; i<num; i++) {
            numI[i] = Integer.parseInt(temp[i]);
            f[numI[i]]++;
        }
        
        Stack<Integer> stack = new Stack<>();
        stack.push(0);
        for (int i=1; i<num; i++) {
            if (stack.isEmpty()) {
                stack.push(i);
            }
            while (!stack.isEmpty() && f[numI[stack.peek()]] < f[numI[i]]) {
                ans[stack.pop()] = numI[i];
            }
            stack.push(i);
        }
        while (!stack.empty()) {
            ans[stack.pop()] = -1;
        }
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for (int i=0; i<num; i++) {
            bw.write(ans[i] + " ");
        }
        bw.write("\n");
        bw.flush();
    }
}
