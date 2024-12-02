import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.HBox;
import javafx.stage.Stage;

public class counter extends Application {

		int x= 0;
		TextField textfield = new TextField();
		
		Button add = new Button("ADD");
		Button sub = new Button("Subtract");
		
	public static void main(String[] args) {
		launch(args);

	}

	@Override
	public void start(Stage primary) throws Exception {
		HBox line = new HBox();
		
		textfield.setText(Integer.toString(x));
		add.setOnAction(new buttonHandler());
		sub.setOnAction(new buttonHandler());
		line.getChildren().addAll(textfield, add, sub);
		Scene scene = new Scene(line);
		primary.setScene(scene);
		primary.show();
		
	}
	class buttonHandler implements EventHandler<ActionEvent>{

		@Override
		public void handle(ActionEvent e) {
			if(e.getSource() == add) {
				
				x++;
				textfield.setText(Integer.toString(x));
				
			}else if(e.getSource().equals(sub)) {
				--x;
				textfield.setText(Integer.toString(x));
			}
			
		}
		
	}

}
