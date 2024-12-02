import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class sceneswitch extends Application {

	boolean passvalidation = false;
	@FXML
	private Button login;
	@FXML
	private Button cancel;
	
	
	public void initialize() {
		login.setOnAction(new loginHandler());
		cancel.setOnAction(new loginHandler());
	}
	
	public static void main(String[] args) {
		launch(args);

	}
	
	

	@Override
	public void start(Stage primaryStage) throws Exception {
		
		if(check()) {
			FXMLLoader loader1 = new FXMLLoader();
			java.net.URL url1 = getClass().getResource("pmanger/borderpage.fxml");
			loader1.setLocation(url1);
			BorderPane borderPane = loader1.load();
			Scene scene1 = new Scene(borderPane);
			primaryStage.setScene(scene1);
			
			
		}else {
			FXMLLoader loader = new FXMLLoader();
			java.net.URL url = getClass().getResource("pmanger/loginpage.fxml");
			loader.setLocation(url);
			VBox box = loader.load();
			Scene scene = new Scene(box);
			primaryStage.setScene(scene);
		}
		primaryStage.show();
	
	}
	
	boolean check() {
		return passvalidation;
		
	}

	private class loginHandler implements EventHandler<ActionEvent>{

		@Override
		public void handle(ActionEvent e) {
			if(e.getSource().equals(login)) {
				passvalidation = true;
				
				
			}
			
		}
		
	}
}
