import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.Scanner;
import java.util.Stack;

public class Main {
	private static int priority(char ch) {
		if(ch=='(') return 0;
		if(ch == '+' || ch=='-') return 1;
		else return 2;
	}
	
    public static void main(String[] args) throws IOException {
    	Scanner sc = new Scanner(System.in);
    	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    	
    	String inLine = sc.nextLine();
    	char[] equation = inLine.toCharArray();
    	
    	Stack<Character> op = new Stack<Character>();
    	
    	for(int i=0; i<equation.length; i++) {
    		if(equation[i]>='A' && equation[i]<='Z') {
    			bw.write(equation[i]);
    		}
    		else if(equation[i] == '(') {
    			op.push(equation[i]);
    		} else if(equation[i] == ')') {
    			while(!op.isEmpty()) {
    				if(op.peek() == '(') {
    					op.pop();
    					break;
    				}
    				bw.write(op.pop());
    			} 
    		} else {
    			while(!op.isEmpty() && priority(op.peek())>=priority(equation[i])) bw.write(op.pop());
    			op.push(equation[i]);
    		}
    	}
    	while(!op.isEmpty()) {
    		bw.write(op.pop());
    	}
    	bw.write("\n");
    	bw.flush();
    }
}
