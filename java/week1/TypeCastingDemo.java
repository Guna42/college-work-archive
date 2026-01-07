class TypeCastingDemo {
    public static void main(String[] args) {
        
        
        int num1 = 100;
        double widenedValue = num1;  
        System.out.println("Original int value: " + num1);
        System.out.println("After widening to double: " + widenedValue);

    
        double num2 = 99.99;
        int narrowedValue = (int) num2;  
        System.out.println("Original double value: " + num2);
        System.out.println("After narrowing to int: " + narrowedValue);
    }
}
