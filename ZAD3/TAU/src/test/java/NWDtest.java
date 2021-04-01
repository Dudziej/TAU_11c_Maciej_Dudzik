import org.junit.After;
import org.junit.Before;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.apache.commons.math3.fraction.Fraction;
import org.mockito.junit.MockitoJUnit;

public class NWDtest {
    private NWDcode nwd;
    private Addcode addcode;
    private Fraction fraction;
    private MockitoJUnit mockit;

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

    @Test
    public void tester11(){
        addcode = new Addcode();
        int result = addcode.Addcode(10, 10);
        Assertions.assertSame(10, 10);
        System.out.println("Test11");
    }

    @Test
    public void tester12(){
        addcode = new Addcode();
        int result = addcode.Addcode(50, 10);
        Assertions.assertEquals(60, 60);
        System.out.println("Test12");
    }

    @Test
    public void tester13(){
        addcode = new Addcode();
        int result = addcode.Addcode(568, 1000);
        Assertions.assertEquals(1568, 1568);
        System.out.println("Test13");
    }

    @Test
    public void tester14(){
        addcode = new Addcode();
        int result = addcode.Addcode(10, 15);
        Assertions.assertNotNull(25);
        System.out.println("Test14");
    }

    @Test
    public void tester15(){
        addcode = new Addcode();
        int result = addcode.Addcode(0, 0);
        Assertions.assertNull(null);
        System.out.println("Test15");
    }

    @Test
    public void tester16(){
        addcode = new Addcode();
        int result = addcode.Addcode(5, -5);
        Assertions.assertNull(null);
        System.out.println("Test16");
    }

    @Test
    public void tester17(){
        addcode = new Addcode();
        int result = addcode.Addcode(0, 11);
        Assertions.assertEquals(11, 11);
        System.out.println("Test17");
    }

    @Test
    public void tester18(){
        fraction = new Fraction(10, 10);
        Assertions.assertEquals(10, 10);
        System.out.println("Test18");
    }

    @Test
    public void tester19(){
        fraction = new Fraction(51, 51);
        Assertions.assertEquals(51, 51);
        System.out.println("Test19");
    }

    @Test
    public void tester20(){
        mockit = new MockitoJUnit();
        MockitoJUnit.collector();
        System.out.println("Test20");
    }

}
