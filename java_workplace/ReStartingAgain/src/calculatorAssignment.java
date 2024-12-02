import javax.print.DocFlavor.URL;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class calculatorAssignment extends Application {

	
	public static boolean logincheck(boolean value) {
		boolean check = value;
		return check;
	}

	public static void main(String[] args) {
		launch(args);

	}

	@Override
	public void start(Stage primaryStage) throws Exception {
		
		
		if(logincheck(false) == false) {
			FXMLLoader loader1 = new FXMLLoader();
			java.net.URL url1 = getClass().getResource("pmanger/loginpage.fxml");
			loader1.setLocation(url1); 	
			VBox vbox1 = loader1.load();	
			Scene scene1 = new Scene(vbox1);
			primaryStage.setScene(scene1);
			
		}else {
			FXMLLoader loader = new FXMLLoader();
			java.net.URL url = getClass().getResource("calculator.fxml");
			loader.setLocation(url); 	
			VBox vbox = loader.load();	
			Scene scene = new Scene(vbox);
			primaryStage.setScene(scene);
		}
		
		primaryStage.show();
		
	}

}
