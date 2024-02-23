class Wallet{
    public int bill1;
    public int bill5;
    public int bill10;
    public int bill20;
    public int bill50;
    public int bill100;

    public Wallet(){}

    public int getTotalMoney(){
        return (1*bill1) + (5*bill5) + (10*bill10) + (20*bill20) + (50*bill50) + (100*bill100);
    }

    // 札の額面（bill）と枚数（amount）を引数にとるメソッドです。
    // billに応じて対応するメンバ変数を増やし、挿入した総額（bill*amount）を返します。
    // billが1,5,10,20,50,100以外の場合は何もせずに0を返します。
    public int insertBill(int bill, int amount){
        switch(bill){
            case(1):
                bill1 += amount;
                break;
            case(5):
                bill5 += amount;
                break;
            case(10):
                bill10 += amount;
                break;
            case(20):
                bill20 += amount;
                break;
            case(50):
                bill50 += amount;
                break;
            case(100):
                bill100 += amount;
                break;
            default:
                return 0;
        }
        
        return bill*amount;
    }
}

class Person{
    public String firstName;
    public String lastName;
    public int age;
    public double heightM;
    public double weightKg;
    public Wallet wallet;

    // firstName, lastName, age, heightM, weightKgの値を引数にとるコンストラクタです。
    // walletには新しいWalletオブジェクトを割り当てます。
    public Person(String firstName, String lastName, int x, double y, double z){
        this.firstName = firstName;
        this.lastName = lastName;
        age = x; // ageの状態がxへアップデートされます。
        heightM = y;
        weightKg = z;
        wallet = new Wallet();
    }

    public int getCash(){
        if(this.wallet == null){
            System.out.println("NO WALLET");
            return 0;
        }
        return this.wallet.getTotalMoney();
    }

    // Personオブジェクトの状態を出力するメソッドです。
    // 注意点として、weightKgについてはローカル変数が新たに定義されており、これが優先的に参照されます。
    // しかしheightMの出力ではthis.weightKgとしてクラスのメンバ変数を明示的に参照しているため、そちらの値が出力されます。
    public void printState(){
        // thisキーワードは必須ではありません。同じ名前のローカル変数（メソッド内で宣言された変数）が存在しない限り、インスタンス変数は直接参照できます。
        System.out.println("firstname - " + firstName);
        System.out.println("lastname - " + lastName); 
        System.out.println("age - " + age);
        double weightKg = 495; // weightKg ローカル変数が優先度が高いです。
        System.out.println("height - " + heightM + ", joking it is: " + this.weightKg);
        System.out.println("weight - " + weightKg);
        System.out.println("Current Money - " + getCash());
        System.out.println();
    }
}

class Main{
    public static void main(String[] args){
        // 引数付きのコンストラクタを用いてPersonオブジェクトを作成します。
        Person p = new Person("Ryu","Poolhopper", 40, 180, 140); 
        p.printState();

        // 札の額面と枚数を指定して財布に入金します。
        p.wallet.insertBill(5,3);
        p.wallet.insertBill(100,2);

        // 状態を再度出力します。ここでの出力では先程挿入した札が反映された状態になっています。
        p.printState();
    }
}

// クラスは新たなオブジェクトスコープを創出し、その中にあるメソッドや変数の利用を許可します。オブジェクトに関連するメソッドが呼び出されるときには、該当オブジェクトのメンバ変数へのアクセス優先度が決まります。

// スコープの優先順位は、以下のようになります。

// メソッド内のローカルスコープ
// オブジェクトを定義するクラススコープ
// ソフトウェア全体で共有されるグローバルスコープ
// プログラミング言語によっては、オブジェクト自身を参照するための特別なキーワード「this」が提供されていますが、メソッド内で必ず使わなければならないわけではありません。この「this」キーワードを利用するか否かは、上述のスコープルールを参照して、どの変数を使用するかが決定されます。


// 言語のスコープルールが許す場合、メソッド内からメンバ変数にアクセスするときに、「this」キーワードの使用を選択したり、省略したりすることができます。「this」キーワードを使用するとコードが長くなり、冗長性が増すというデメリットがある一方で、「this」キーワードを使用することで、メンバ変数のアクセスが保証され、開発者はそのメンバ変数が活用されていることを理解しやすくなります。したがって、「this」キーワードの使用は個人の嗜好やチームのポリシーによります。

// 例として、Javaの開発者の間では、コンストラクタやゲッター、セッターを除いて、「this」キーワードを省略する傾向が見受けられます。しかし、一部の開発者はインスタンス変数へのアクセスを明示的に示し、テキストエディタのチェック機能で警告が出ることを避けるために、「this」キーワードを利用します。

// どちらのアプローチを採用するにせよ、その選択を一貫して適用し、スタイルの統一性を保つことが重要です。Recursion では、一貫性を保つために全てのプログラミング言語で「this」キーワードを使用しています。
