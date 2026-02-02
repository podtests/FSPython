class Employee {

    //static variable
    public static string companyName;

//instance variable
    public int cardId; 

//constructor
    public Employee(int cardId){
        this.cardId = cardId;
    }

// Craeting method
    public string getPunchInTime(int startTime, int EndTime){
        int diff = EndTime - startTime;
        return this.cardId+ "user spent time as" + diff;
    }

}

Employee e1 = new Employee(45);
e1.cardId
e1.getPunchInTime(78, 90)
Employee.companyName= ''