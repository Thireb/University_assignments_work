import javafx.application.Application;
import javafx.collections.ObservableList;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ListView;
import javafx.scene.control.SelectionMode;
import javafx.scene.control.TextArea;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class passwordmanger extends Application {

	public static void main(String[] args) {
		launch(args);

	}

	@Override
	public void start(Stage primaryStage) throws Exception {
		
		
		Button btn[] = new Button[6];
		
		
		HBox horizontal = new HBox();
		
		VBox vertical = new VBox();
		ListView listView = new ListView();

        listView.getSelectionModel().setSelectionMode(SelectionMode.MULTIPLE);

        for(int i=0; i<4; i++) {
        	listView.getItems().add(Integer.toString(i));
            	
        }
    


        Button button = new Button("Read Selected Value");

        button.setOnAction(event -> {
            ObservableList<String> selectedIndices = listView.getSelectionModel().getSelectedItems();

            for(String item : selectedIndices){
                System.out.println(item + " times fuck you");
            }
        });
		
		horizontal.getChildren().addAll(listView, button);
		
		vertical.getChildren().add(horizontal);
		
		Scene scene = new Scene(vertical, 500, 100);
		
		primaryStage.setScene(scene);
		primaryStage.setTitle("Password Manger");
		primaryStage.show();
		
	}

}
