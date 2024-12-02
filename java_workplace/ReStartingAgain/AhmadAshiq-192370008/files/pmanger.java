
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class pmanger extends Application {

	public static void main(String[] args) {
		launch(args);

	}

	@Override
	public void start(Stage stage) throws Exception {
		
		FXMLLoader loader = new FXMLLoader();
		java.net.URL url = getClass().getResource("pmanger/borderpage.fxml");
		loader.setLocation(url);
		BorderPane pane = loader.load();
		Scene scene = new Scene(pane);
		stage.setScene(scene);
		
		stage.show();
		
	}

}
