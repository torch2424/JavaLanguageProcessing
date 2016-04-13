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
		
		SentenceDetector sDetect = null;
        InputStream modelIn = null;
        try {
        	
            // Loading sentence detection model
     	   modelIn = getClass().getResourceAsStream("../en-sent.bin");
     	   final SentenceModel sentenceModel = new SentenceModel(modelIn);
     	   modelIn.close();
          
            sDetect = new SentenceDetectorME(sentenceModel);
          
         } catch (final IOException ioe) {
         	//Error
            ioe.printStackTrace();
         } finally {
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

}
