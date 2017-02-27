import java.util.Arrays;
import java.util.List;
import java.util.Optional;
import java.util.function.Function;
import java.util.function.Supplier;
import java.util.stream.IntStream;

/**
 * Created by andrewho on 2017-02-16.
 */

public class TestClass {

    //if an interface has one method, you can put the interface in a lambda expression
    //it will execute the function within the interface. If there's ore than one function
    // that is not a default function, it can't do it
    interface OutputFunc{
        void interface_func (String str);
    }


    //function
    static String execute (Function<Integer, String> f){
        return f.apply(11);
    }

    static String aa(Integer a){
        return "dd" + a;
    }


    //for each function
    //takes into account supplier/producer functions
    static void foreach(List<String> l_list, OutputFunc f){
        for (String s: l_list){
            f.interface_func(s);
        }
    }

    public static void main(String args[]){

        //lambda expression
        //so you can build a high order function (submit a function as an argument)
        Function<Integer, String> f = a -> "andrew" + a;


        System.out.println(f.apply(10));

        //high level
        System.out.println(execute(f));

        //define the function inline
        //should output andrew211 or andrew2<x>
        System.out.println(execute(a -> "andrew2" + a));

        //call a function within the class
        System.out.println(execute(TestClass::aa));

        List<String> l_list = Arrays.asList("1", "2", "3", "4");

        foreach(l_list, System.out::println);

        //foreach loops are already implemented
        l_list.forEach(System.out::println);

        //remove item from list
        //l_list.removeIf(a -> a.contains("b"));  //not supported in lists
        l_list.forEach(System.out::println);



        //streams introduced in java 8
        l_list.stream().forEach(System.out::println);


        String reduce = l_list.stream()
                    .reduce("", (a, b) -> a + "," + b);
        System.out.println(reduce);

        //what if don't want the first printed
        String reduce2 = l_list.stream()
                .skip(1)
                .reduce(l_list.get(0), (a, b) -> a + "," + b);
        System.out.println(reduce2);

        //what if multiply by 5 (all of them are initially strings)
        String reduce3 = l_list.stream()
                .skip(1)
                .map(a -> Integer.valueOf(a) * 5)
                //convert back to string
                .map(a -> a.toString())
                .reduce(l_list.get(0), (a,b) -> a + "," + b);
        System.out.println(reduce3);


        //implent range
        IntStream.range(0,10).forEach(a -> );

        //l_list.parallelStream() --> multiple threads, in parallel (map reduce)

        //Optional class
        String nulll = null;
        //how to avoid null checks?

        Optional<String> nulll_1 = Optional.ofNullable(nulll);
        System.out.println(nulll_1.get());
        System.out.println(nulll_1.orElse("aa"));   //if optional class not set
        System.out.println(nulll_1.orElseGet( ""));// orelse get, only gets executed (pass in function) if the value is null

        //Future.java (multithreading)
    }
}
