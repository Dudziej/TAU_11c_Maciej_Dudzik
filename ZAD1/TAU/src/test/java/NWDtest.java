import org.junit.After;
import org.junit.Before;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class NWDtest {
    private NWDcode nwd;

    @Before
    public void doIt(){
        nwd = new NWDcode();
        System.out.println("Before");
    }

    @After
    public void destroyIt(){
        nwd = null;
        System.out.println("After");
    }

    @Test
    public void tester1(){
        nwd = new NWDcode();
        int result = nwd.NWDcode(10, 6);
        Assertions.assertEquals(2, result);
        System.out.println("Test1");
    }

    @Test
    public void  tester2(){
        nwd = new NWDcode();
        int result = nwd.NWDcode(1, 1);
        Assertions.assertEquals(1,result);
        System.out.println("Test2");
    }

    @Test
    public void tester3(){
        nwd = new NWDcode();
        int result = nwd.NWDcode(10000, 24500);
        Assertions.assertEquals(500, result);
        System.out.println("Test3");
    }

    @Test
    public void tester4(){
        nwd = new NWDcode();
        int result = nwd.NWDcode(0,0);
        Assertions.assertEquals(0, result);
        System.out.println("Test4");
    }

    @Test
    public void tester5(){
        nwd = new NWDcode();
        int result = nwd.NWDcode(10, 5);
        Assertions.assertNotNull(result);
        System.out.println("Test5");
    }

    @Test
    public void tester6(){
        nwd = new NWDcode();
        int result = nwd.NWDcode(5, 20);
        Assertions.assertNotNull(result);
        System.out.println("Test6");
    }

    @Test
    public void tester7(){
        nwd = new NWDcode();
        int result = nwd.NWDcode(0, 15);
        Assertions.assertNotNull(result);
        System.out.println("Test7");
    }

    @Test
    public void tester8(){
        nwd = new NWDcode();
        int result = nwd.NWDcode(0, 0);
        Assertions.assertNull(result);
        System.out.println("Test8");
    }

    @Test
    public void tester9(){
        nwd = new NWDcode();
        int result = nwd.NWDcode(10, 5);
        Assertions.assertSame(5 ,result);
        System.out.println("Test9");
    }

    @Test
    public void tester10(){
        nwd = new NWDcode();
        int result = nwd.NWDcode(69, 69);
        Assertions.assertSame(69, result);
        System.out.println("Test10");
    }
}
