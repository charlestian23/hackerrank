import java.util.*;

class Student implements Comparable<Student>{
    private int id;
    private String fname;
    private double cgpa;
    public Student(int id, String fname, double cgpa) {
        super();
        this.id = id;
        this.fname = fname;
        this.cgpa = cgpa;
    }
    public int getId() {
        return id;
    }
    public String getFname() {
        return fname;
    }
    public double getCgpa() {
        return cgpa;
    }

    @Override
    public int compareTo(Student o) {
        if (this.getCgpa() != o.getCgpa()) {
            if (o.getCgpa() - this.getCgpa() < 0)
                return -1;
            return 1;
        }
        else if (!o.getFname().equals(this.getFname())) {
//            System.out.println("2");
            return this.getFname().compareTo(o.getFname());
        }
        else {
//            System.out.println("3");
            return o.getId() - this.getId();
        }
    }
}

//Complete the code
public class JavaSort
{
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int testCases = Integer.parseInt(in.nextLine());

        List<Student> studentList = new ArrayList<Student>();
        while(testCases>0){
            int id = in.nextInt();
            String fname = in.next();
            double cgpa = in.nextDouble();

            Student st = new Student(id, fname, cgpa);

            boolean added = false;
            int counter = 0;
            while (!added && counter < studentList.size())
            {
                if (st.compareTo(studentList.get(counter)) < 0) {
                    studentList.add(counter, st);
                    added = true;
                }
                counter++;
            }
            if (!added)
                studentList.add(st);
//            studentList.add(st);

            testCases--;
        }

        for(Student st: studentList){
            System.out.println(st.getFname());
        }
    }
}



