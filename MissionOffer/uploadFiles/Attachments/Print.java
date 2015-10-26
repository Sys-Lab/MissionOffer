
interface Print {
	void print();
}

class Student implements Print{
	int sID;
	String name;
	
	public void print() {
		System.out.println(sID+" "+name);
	}
}

class Teacher implements Print {
	int tID;
	String name;
	
	public void print() {
		System.out.println(tID+" "+name);
	} 
}