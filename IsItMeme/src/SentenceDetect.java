import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;

import opennlp.tools.sentdetect.SentenceDetector;
import opennlp.tools.sentdetect.SentenceDetectorME;
import opennlp.tools.sentdetect.SentenceModel;


//Class to use OpenNlp to detect is a string is a sentence
public class SentenceDetect {
	
	//Our sentence Detector
	SentenceDetector sDetect;
	
	public SentenceDetect() {
		
		//Get our current location
		File currentLocation = new File(SentenceDetect.class.getProtectionDomain().getCodeSource().getLocation().getFile());
		
		//Initialize our variables for try catch
		sDetect = null;
        InputStream modelIn = null;
        try {
        	
            // Loading sentence detection model / Loading training data
     	   modelIn = new FileInputStream(currentLocation.getParentFile().getParent() + "/en-sent.bin");
     	   final SentenceModel sentenceModel = new SentenceModel(modelIn);
     	   modelIn.close();
           
     	   //Assign our now trained Sentence detector
           sDetect = new SentenceDetectorME(sentenceModel);
          
         } catch (final IOException ioe) {
         	
        	 //Error
            ioe.printStackTrace();
            
            //Exit the app
            HomeMain.exitApp();
            
         } finally {
        	 
        	 //Close the training data input stream
            if (modelIn != null) {
               try {
                  modelIn.close();
               } catch (final IOException e) {} // oh well!
            }
         }
	}
	
	//Function to return if a string is a sentence
	public boolean isSentence(String input) {
		
		//Check the input
		if(sDetect.sentDetect(input).length > 0) return true;
		else return false;
	}
	
	//Function to return the number of sentences in a meme
	public int numSentences(String input) {
		
		return sDetect.sentDetect(input).length;
	}

}
