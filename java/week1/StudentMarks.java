class StudentMarks {
    public static void main(String[] args) {
        String studentName = "Guna Vardhan";
        int rollNumber = 101;
        float mark1 = 85, mark2 = 90, mark3 = 80;

        int total = (int)(mark1 + mark2 + mark3);
        float percentage = total / 3.0f;

        System.out.println("----- Student Details -----");
        System.out.println("Name: " + studentName);
        System.out.println("Roll Number: " + rollNumber);
        System.out.println("Marks: " + mark1 + ", " + mark2 + ", " + mark3);
        System.out.println("Total Marks: " + total);
        System.out.println("Percentage: " + percentage + "%");
    }
}
