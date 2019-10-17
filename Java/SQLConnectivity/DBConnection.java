package com.shriaas.student;

import java.sql.*;
/*
 * Author: shriaas2898
 * Date: 16th OCT 2019
 * Description: Simple class to demonstrate CRUD operations in java.
 */

public class DBConnection {
	
	//---------------Declaring and initializing data members----------------
	private static DBConnection dao = null;
	private String database,user,pass;
	private Connection conn;
	
	//Constructor
	private DBConnection(String database,String user,String pass) {
		this.database = database;
		this.user = user;
		this.pass = pass;
		this.conn = getConnection();
		
	}
	
	//For creating a single object
	public static DBConnection getDBConnection(String database,String user,String pass) {
		if(dao == null) {
			dao = new DBConnection(database, user, pass);
			
		}
		return dao;
	}
	
	/*
	 * getConnection()->Connection 
	 * returns the connection to database with supplied username and password.
	 * For establishing the connection we first need to get a driver, think of it like a device
	  driver, like a device driver helps us connect device to our computer, database driver helps us
	  connect our java code to database.
	 *Here we are using mysql driver you can download it from here: https://dev.mysql.com/downloads/connector/j/
	 */
	private Connection getConnection() {
	
		//This is for specifying our driver
		String driver = "com.mysql.jdbc.Driver";
		
		//Exception Handling
		try {
		
			Class.forName(driver);
		} catch (ClassNotFoundException e) {
			
			System.out.println(e);
		}
		
		//URL of the data base if your database is running on a different port change 3306 to your port
		String url = "jdbc:mysql://localhost:3306/"+database;	
		Connection conn = null;
		
		try {
			//Establishing the connection
			conn = DriverManager.getConnection(url, user, pass);
		} catch (SQLException e) {
			
			e.printStackTrace();
		}
		return conn;
	}
	
	/*
	 * Creates table using Statement class (present in java.sql package)
	 * Statement class is used to create and execute SQL statements through java's strings.
	 */
	
	public void createTable() {
		
		try {
			//Create query
		String query = "CREATE TABLE IF NOT EXISTS student(roll_no int,marks int, name varchar(30))";
		
		//Initializing statement object
		Statement st = conn.createStatement();
		//execute update is used for create/insert/update/delete operations.It returns nothing
		st.executeUpdate(query);
														 
	}
		catch (SQLException e) {
		e.printStackTrace();
	}
	
}
    public void showRecords(){

    		try {
			//Create query
		String query = "SELECT * FROM student";
		
		//Initializing statement object
		Statement st = conn.createStatement();
		ResultSet rs;
		//executeQuery returns a result set of select statement 
		rs = st.executeQuery(query);
		
		//Here ResultSet class is used to store result of a query
		//It is a type of iterator in java, which initial points at the top of resultset i.e before first record
		while(rs.next()) {
			//ResultSet object has getXXX methods where XXX -> datatype of column 
			//You have to pass column label to getXXX method
			//To know more on what method is suitable for which sql datatype refer here: https://docs.oracle.com/javadb/10.8.3.0/tuning/ctunperf98197.html
			System.out.print("Roll No. "+rs.getInt("roll_no")+"\t");
			System.out.print("Name "+rs.getString("name")+"\t");
			System.out.println("Marks "+rs.getInt("marks"));
		}
														 
	}
		catch (SQLException e) {
		e.printStackTrace();
	}
}
    
    
    public void insert(int roll,String name,int marks) {
    	try {
			//Insert query
		String query = "INSERT INTO student(roll_no,name,marks) values("+roll+",'"+name+"',"+marks+")";
		
		//Initializing statement object
		Statement st = conn.createStatement();
		//execute update is used for create/insert/update/delete operations.It returns nothing
		st.executeUpdate(query);		
														 
	}
		catch (SQLException e) {
		e.printStackTrace();
	}	
    }
	
	
	public void updateName(int roll,String name){
    	try {
			//Update query
		String query = "UPDATE student set name ='"+name+"' where roll_no ="+roll;
		
		//Initializing statement object
		Statement st = conn.createStatement();
		//execute update is used for create/insert/update/delete operations.It returns nothing
		st.executeUpdate(query);		
														 
	}
		catch (SQLException e) {
		e.printStackTrace();
	}	
    }
	
	
	public void delete(int roll){
    	try {
			//Delete query
		String query = "DELETE FROM student where roll_no ="+roll;
		
		//Initializing statement object
		Statement st = conn.createStatement();
		//execute update is used for create/insert/update/delete operations.It returns nothing
		st.executeUpdate(query);		
														 
	}
		catch (SQLException e) {
		e.printStackTrace();
	}	
    }
}
