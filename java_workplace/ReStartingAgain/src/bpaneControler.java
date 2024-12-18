import java.io.File;
import java.util.ArrayList;

import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.ListView;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;

public class bpaneControler {

	
	@FXML
	private ListView<String> list;
	@FXML
	private Button view;
	@FXML
	private Button edit;
	@FXML
	private Button save;
	@FXML
	private TextField websiteField;
	@FXML
	private TextField emailField;
	@FXML
	private TextField passField;
	@FXML
	private TextArea notes;
	
	int indax = 0;
	String web = null;
	String email = null;
	String pass = null;
	String note = null;
	
	String[] listArray = new String[10];// values to be put into the list of whom we'll get the index of.
	String[] websiteArray = new String[10];
	String[] emailArray = new String[10];
	String[] passArray = new String[10];
	String[] notesArray = new String[10];
	File file;
	ArrayList<String> lister = new ArrayList<>();;
	
	public void initializeFile() {
		try {
			file = new File("csv.csv");
			file.createNewFile();
			readAndWrite(file);
		} catch (Exception e) {
			e.getStackTrace();
		}
	}
	
	public void readAndWrite(File file) {
		String[] strArray = null;
		ArrayList<String[]> arrayList = new ArrayList<>();
		String string = null;
		try {
			for (int i = 0; i < websiteArray.length; i++) {
				strArray = StandAlone.readCertainLine(file, i);
				string = StandAlone.readLine(file, i);
				arrayList.add(strArray);
				lister.add(string);
				
				listArray = arrayList.get(i);
				
				for(int j=0; j<4;j++) {
					
					if (j == 0) {
						websiteArray[i] = listArray[j];
						
					} else if (j == 1) {
						emailArray[i] = listArray[j];
					} else if (j == 2) {
						passArray[i] = listArray[j];
					} else {
						notesArray[i] = listArray[j];
					}
					
				}
				
			}
			
		} catch (Exception e) {
			e.getStackTrace();
		}
	}
	
	
	public void initialize() {
		initializeFile();
		for(int i=0; i< websiteArray.length;i++) {//loops through the list and populates the gui list.
			list.getItems().add(websiteArray[i]);
		}
		view.setOnAction(new bpaneHandler());
		edit.setOnAction(new bpaneHandler());
		save.setOnAction(new bpaneHandler());
	}
	
	class bpaneHandler implements EventHandler<ActionEvent>{

		@Override
		public void handle(ActionEvent e) {
			if(e.getSource().equals(view)) {
				ObservableList<Integer> index = list.getSelectionModel().getSelectedIndices();
				for(int i: index) {

					websiteField.setText(websiteArray[i]);
					emailField.setText(emailArray[i]);
					passField.setText(passArray[i]);
					notes.setText(notesArray[i]);
				}
				save.setDisable(true);
			}
			else if(e.getSource().equals(edit)) {
				ObservableList<Integer> index = list.getSelectionModel().getSelectedIndices();
				websiteField.setEditable(true);
				emailField.setEditable(true);
				passField.setEditable(true);
				notes.setEditable(true);
				save.setDisable(false);
				
				for(int i: index) {
					indax = i;
					websiteField.setText(websiteArray[i]);
					emailField.setText(emailArray[i]);
					passField.setText(passArray[i]);
					notes.setText(notesArray[i]);
					// save the index somewhere
					//save the fields data somewhere.
					
				}
				
				
				
			}
			if(e.getSource().equals(save)) {
				web = websiteField.getText();
				email = emailField.getText();
				pass = passField.getText();
				note = notes.getText();
				
				websiteArray[indax] = web;
				emailArray[indax] = email;
				passArray[indax] = pass;
				notesArray[indax] = note;
				
				String St = web+","+email+","+pass+","+note;
				ArrayList<String> tempList = new ArrayList<>();
				String string = null;
				for (int i = 0; i < websiteArray.length; i++) {
					string = websiteArray[i] + "," + emailArray[i] + "," + passArray[i] + "," + notesArray[i];
					tempList.add(string);
				}
				tempList = StandAlone.replace(tempList, indax, St);
				StandAlone.writeLine(file, tempList);
				save.setDisable(true);
			}
			
			
		}
		  

		
	}
	
}
