
public class Student extends Person{

	int sID, classNo;
	
	Student(String name, char sex, int age) {
		super(name, sex, age);
	}
	
	void setData(String name, char sex, int age,int sID, int classNo) {
		super.setData(name, sex, age);
		this.sID = sID;
		this.classNo = classNo;
	}
	
	String getData() {
		return super.getdata() + " sID:" + sID + " classNo:" + classNo;
	}
}
