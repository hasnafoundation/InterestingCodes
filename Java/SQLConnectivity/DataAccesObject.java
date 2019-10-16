package com.shriaas.student;

import java.sql.*;

public class DataAccesObject {
	
	//---------------Declaring and initializing data members----------------
	private static DataAccesObject dao = null;
	private String database,user,pass;
	private Connection conn;
	
	//Constructor
	private DataAccesObject(String database,String user,String pass) {
		this.database = database;
		this.user = user;
		this.pass = pass;
		this.conn = getConnection();
		
	}
	
	//For creating a single object
	public static DataAccesObject getDataAccessObject(String database,String user,String pass) {
		if(dao == null) {
			dao = new DataAccesObject(database, user, pass);
			
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
		//execute update is used for create/insert/update operations
		st.executeUpdate(query);
														 
	}
		catch (SQLException e) {
		e.printStackTrace();
	}
	
}
	
	
	
}
