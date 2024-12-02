

import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.BorderPane;
import javafx.stage.Stage;

public class loginpageControler  {
	
	
	Stage s;
	

	
	calculatorAssignment switcher = new calculatorAssignment();
	@FXML
	private Button login;
	
	
	public void initialize() {
		login.setOnAction(new loginpagehandler());
	}
	


	
	class loginpagehandler implements EventHandler<ActionEvent> {

		@Override
		public void handle(ActionEvent e) {
			
			
		}

		
		
	}
}
