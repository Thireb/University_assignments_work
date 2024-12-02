import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;

public class calculatorControler {

	
	int textToDisplay = 0;
	String firstInput = "";
	String secondInput = "";
	String operator = "";
	Double sqrtResult = 0.0;
	boolean switchOn = true;
	@FXML
	private Button zero;
	@FXML
	private Button one;
	@FXML
	private Button two;
	@FXML
	private Button three;
	@FXML
	private Button four;
	@FXML
	private Button five;
	@FXML
	private Button six;
	@FXML
	private Button seven;
	@FXML
	private Button eight;
	@FXML
	private Button nine;
	@FXML
	private Button plus;
	@FXML
	private Button minus;
	@FXML
	private Button divide;
	@FXML
	private Button multiply;
	@FXML
	private Button equla;
	@FXML
	private TextField txtfield;
	@FXML
	private Button root;
	@FXML
	private Button clear;
	
	
	
	public void initialize() {
		zero.setOnAction(new buttonHandler());
		one.setOnAction(new buttonHandler());
		two.setOnAction(new buttonHandler());
		three.setOnAction(new buttonHandler());
		four.setOnAction(new buttonHandler());
		five.setOnAction(new buttonHandler());
		six.setOnAction(new buttonHandler());
		seven.setOnAction(new buttonHandler());
		eight.setOnAction(new buttonHandler());
		nine.setOnAction(new buttonHandler());
		plus.setOnAction(new buttonHandler());
		minus.setOnAction(new buttonHandler());
		divide.setOnAction(new buttonHandler());
		multiply.setOnAction(new buttonHandler());
		equla.setOnAction(new buttonHandler());
		root.setOnAction(new buttonHandler());
		clear.setOnAction(new buttonHandler());
	}
	
	public class buttonHandler implements EventHandler<ActionEvent>{

		@Override
		public void handle(ActionEvent e) {
			
			
			if(e.getSource().equals(clear)) {
				txtfield.setText(null);
				firstInput = "";
				operator = "";
				secondInput = "";
			}
			
			// first number to be put here
				if(e.getSource().equals(zero)) {
					if(operator == "") {
						firstInput += '0';
						txtfield.setText(firstInput);
						System.out.println(firstInput);}
					else {
						secondInput += '0';
						txtfield.setText(secondInput);
						System.out.println(secondInput);
					}
				}else if(e.getSource().equals(one)){
					if(operator == "") {
						firstInput += '1';
						txtfield.setText(firstInput);
						System.out.println(firstInput);}
					else {
						secondInput += '1';
						txtfield.setText(secondInput);
						System.out.println(secondInput);
					}
				}else if(e.getSource().equals(two)){
					if(operator == "") {
						firstInput += '2';
						txtfield.setText(firstInput);
						System.out.println(firstInput);}
					else {
						secondInput += '2';
						txtfield.setText(secondInput);
						System.out.println(secondInput);
					}
				}else if(e.getSource().equals(three)){
					if(operator == "") {
						firstInput += '3';
						txtfield.setText(firstInput);
						System.out.println(firstInput);}
					else {
						secondInput += '3';
						txtfield.setText(secondInput);
						System.out.println(secondInput);
					}
				}else if(e.getSource().equals(four)){
					if(operator == "") {
						firstInput += '4';
						txtfield.setText(firstInput);
						System.out.println(firstInput);}
					else {
						secondInput += '4';
						txtfield.setText(secondInput);
						System.out.println(secondInput);
					}
				}else if(e.getSource().equals(five)){
					if(operator == "") {
						firstInput += '5';
						txtfield.setText(firstInput);
						System.out.println(firstInput);}
					else {
						secondInput += '5';
						txtfield.setText(secondInput);
						System.out.println(secondInput);
					}
				}else if(e.getSource().equals(six)){
					if(operator == "") {
						firstInput += '6';
						txtfield.setText(firstInput);
						System.out.println(firstInput);}
					else {
						secondInput += '6';
						txtfield.setText(secondInput);
						System.out.println(secondInput);
					}
				}else if(e.getSource().equals(seven)){
					if(operator == "") {
						firstInput += '7';
						txtfield.setText(firstInput);
						System.out.println(firstInput);}
					else {
						secondInput += '7';
						txtfield.setText(secondInput);
						System.out.println(secondInput);
					}
				}else if(e.getSource().equals(eight)){
					if(operator == "") {
						firstInput += '8';
						txtfield.setText(firstInput);
						System.out.println(firstInput);}
					else {
						secondInput += '8';
						txtfield.setText(secondInput);
						System.out.println(secondInput);
					}
				}else if(e.getSource().equals(nine)){
					if(operator == "") {
						firstInput += '9';
						txtfield.setText(firstInput);
						System.out.println(firstInput);}
					else {
						secondInput += '9';
						txtfield.setText(secondInput);
						System.out.println(secondInput);
					}}
				
				// choose operator
				if(e.getSource().equals(plus)) {
					operator = "+";
					txtfield.setText(operator);
					System.out.println(operator);
				}else if(e.getSource().equals(minus)) {
					operator = "-";
					txtfield.setText(operator);
					System.out.println(operator);
				}else if(e.getSource().equals(divide)) {
					operator = "/";
					txtfield.setText(operator);
					System.out.println(operator);
				}else if(e.getSource().equals(multiply)) {
					operator = "*";
					txtfield.setText(operator);
					System.out.println(operator);
				}else if(e.getSource().equals(root)) {
					operator = "^1/2";
					txtfield.setText(firstInput + operator);
				}
				
				
				if(e.getSource().equals(equla)) {
					switch(operator) {
					
					case "+":
						textToDisplay = Integer.parseInt(firstInput) + Integer.parseInt(secondInput);
						txtfield.setText(Integer.toString(textToDisplay));
						System.out.println(textToDisplay);
						
						break;
						
					case "-":
						textToDisplay = Integer.parseInt(firstInput) - Integer.parseInt(secondInput);
						txtfield.setText(Integer.toString(textToDisplay));
						System.out.println(textToDisplay);
						break;
						
					case "/":
						textToDisplay = Integer.parseInt(firstInput) / Integer.parseInt(secondInput);
						txtfield.setText(Integer.toString(textToDisplay));
						System.out.println(textToDisplay);
						
						break;
						
					case "*":
						textToDisplay = Integer.parseInt(firstInput) * Integer.parseInt(secondInput);
						txtfield.setText(Integer.toString(textToDisplay));
						System.out.println(textToDisplay);
						break;
					
					case "^1/2":
						sqrtResult = Math.sqrt(Double.parseDouble(firstInput));
						txtfield.setText(Double.toString(sqrtResult));
						System.out.println(sqrtResult);
						
						break;
					
					}
				}
				
		/*		// enter second number if operator is not null
				if(operator != ' ') {
					if(e.getSource().equals(zero)) {
						secondInput += '0';
						System.out.println(secondInput);
					}else if(e.getSource().equals(one)){
						secondInput += '1';
						System.out.println(secondInput);
					}else if(e.getSource().equals(two)){
						secondInput += '2';
						System.out.println(secondInput);
					}else if(e.getSource().equals(three)){
						secondInput += '3';
						System.out.println(secondInput);
					}else if(e.getSource().equals(four)){
						secondInput += '4';
						System.out.println(secondInput);
					}else if(e.getSource().equals(five)){
						secondInput += '5';
						System.out.println(secondInput);
					}else if(e.getSource().equals(six)){
						secondInput += '6';
						System.out.println(secondInput);
					}else if(e.getSource().equals(seven)){
						secondInput += '7';
						System.out.println(secondInput);
					}else if(e.getSource().equals(eight)){
						secondInput += '8';
						System.out.println(secondInput);
					}else if(e.getSource().equals(nine)){
						secondInput += '9';
						System.out.println(secondInput);}
			*/		
					
				}
				
		
			
		}
		
	}

