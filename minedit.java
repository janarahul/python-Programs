import java.util.*;

class minedit{
	static int  min(int a,int b,int c){
		if(a<=b&&a<=c){
			return a;
		}
		if(b<=a&&b<=c){
			return b;
		}
		if(c<=a&&c<=b){
			return c;
		}
		return 0;
	}
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		String str1 = sc.nextLine();
		String str2 = sc.nextLine();
		
		int m=str1.length(),n=str2.length();
		int[][] mat = new int[m+1][n+1];
		for(int i=0;i<m+1;i++){
			for(int j=0;j<n+1;j++){
				if(i==0){
					mat[i][j] = j;
				}else if(j==0){
					mat[i][j] = i;
				}else{
					int e = 1;
					if(str1.charAt(i-1)==str2.charAt(j-1)){
					
						e=0;
					}
					
					int a= mat[i-1][j]+1,b=mat[i][j-1]+1,c=mat[i-1][j-1]+e;
					
					mat[i][j] = min(mat[i-1][j]+1,mat[i][j-1]+1,mat[i-1][j-1]+e);
	
				}
			}
		}
		for(int i=0;i<m+1;i++){
			for(int j=0;j<n+1;j++){
				System.out.print(""+mat[i][j]+" ");
			}
			System.out.println();
		}
		System.out.println("Minimun edit distance= "+mat[m][n]);	
	}


}
