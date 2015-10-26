
public class Person {
	String name;
	char sex;
	int age;
	
	Person(String name,char sex,int age) {
		setData(name,sex,age);
	}
	
	void setData(String name,char sex,int age) {
		this.name = name;
		this.sex = sex;
		this.age = age;
	}
	
	String getdata() {
		return "name:" + name + " sex:" + sex + " age:" + age;
	}
}
