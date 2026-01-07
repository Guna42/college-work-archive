public class StudentGrade {
    public static void main(String[] args) {
        int sub1 = 60, sub2 = 55, sub3 = 40;
        int total = sub1 + sub2 + sub3;
        int percentage = total / 3;
        if (percentage >= 50 && sub1 >= 35 && sub2 >= 35 && sub3 >= 35) {
            System.out.println("Pass");
        } else {
            System.out.println("Fail");
        }
    }
}
