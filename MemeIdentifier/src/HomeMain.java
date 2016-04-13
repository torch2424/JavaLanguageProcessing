
public class HomeMain {
	
	//Our application name
    private static final String appName = "Meme Identifier";
    
    
	public static void main(String[] args) {
		
		//Print the welcome
        System.out.println("Welcome to the " + appName + "!");
        System.out.println();
        
        //Print asking for user input
        System.out.println("pls type ur meme beelow...");
        System.out.println();
        
        String memeInput = System.in();
	}
	
	//Function to exit the app
    public static void exitApp() {

        //Simply print spacing and exit
        System.out.println();
        System.exit(0);
    }

}
