class RGB24{
    public int red;
    public int green;
    public int blue;

    public RGB24(int red, int green, int blue){
        this.red = red;
        this.green = green;
        this.blue = blue;
    }

    // このコンストラクタは、文字列形式で色を入力できるようにします。
    // 関数のオーバーロードを使用しています。
    // 具体的には、16進数で6文字（例："FF00FF"）または、2進数で24文字（例："111111110000000011111111"）で色を指定できます。
    // 文字列の長さが6または24でなければ、色は黒になります。
    public RGB24(String inputString){
        int l = inputString.length();
        // 長さが6なら16進数と解釈
        if(l == 6) this.setColorsByHex(inputString);
        // 長さが24なら2進数と解釈
        else if(l == 24) this.setColorsByBin(inputString);
        // 長さが6でも24でもなければ黒にする
        else this.setAsBlack();
    }

    // このメソッドは、16進数の色を設定します。
    // 例えば、"FF00FF"を入力とすると、赤255、緑0、青255となります。
    // ただし、文字列の長さが6でなければ、色は黒になります。
    public void setColorsByHex(String hex){
        // 長さが6でなければ黒にする
        if(hex.length() != 6) this.setAsBlack();
        else{
            // 最初の2文字を赤と解釈
            this.red = Integer.parseInt(hex.substring(0,2), 16);
            // 次の2文字を緑と解釈
            this.green = Integer.parseInt(hex.substring(2,4), 16);
            // 最後の2文字を青と解釈
            this.blue = Integer.parseInt(hex.substring(4,6), 16);
        }
    }

    // このメソッドは、2進数の色を設定します。
    // 例えば、"111111110000000011111111"を入力とすると、赤255、緑0、青255となります。
    // ただし、文字列の長さが24でなければ、色は黒になります。
    public void setColorsByBin(String bin){
        // 長さが24でなければ黒にする
        if(bin.length() != 24) this.setAsBlack();
        else{
            // 最初の8文字を赤と解釈
            this.red = Integer.parseInt(bin.substring(0,8), 2);
            // 次の8文字を緑と解釈
            this.green = Integer.parseInt(bin.substring(8,16), 2);
            // 最後の8文字を青と解釈
            this.blue = Integer.parseInt(bin.substring(16), 2);
        }
    }

    // このメソッドは、色を黒（赤0、緑0、青0）に設定します。
    public void setAsBlack(){
        this.red = 0;
        this.green = 0;
        this.blue = 0;
    }

    public String getHex(){
        String hex = Integer.toHexString(this.red);
        hex+=Integer.toHexString(this.green);
        hex+=Integer.toHexString(this.blue);

        return hex;
    }

    public String getBits(){
        return Integer.toBinaryString(Integer.parseInt(this.getHex(), 16));
    }

    // このメソッドは、赤、緑、青の中で一番強い色を判断します。
    // 赤、緑、青が全て同じ値であれば、"grayscale"（グレースケール）を返します。
    // そうでなければ、一番強い色（赤、緑、青）の名前を返します。
    public String getColorShade(){
        // 全ての色が同じなら"grayscale"
        if(this.red == this.green && this.green == this.blue) return "grayscale";
        // 色の名前を保存する配列
        String[] stringTable = new String[]{"red","green","blue"};
        // 色の値を保存する配列
        int[] values = {this.red, this.green, this.blue};

        // 最大値の初期値を赤の値にする
        int max = values[0];
        // 最大値があるインデックスの初期値を0（赤）にする
        int maxIndex = 0;
        // 緑と青をチェックする
        for(int i = 1; i < values.length; i++){
            // 現在の最大値よりも大きければ、その値が新しい最大値になる
            if(max <= values[i]){
                max = values[i];
                // そして、そのインデックスを保存する
                maxIndex = i;
            }
        }
        // 最大値がある色の名前を返す
        return stringTable[maxIndex];
    }

    // 文字列変換メソッドtoString()
    // Javaは、System.out.println(data)関数のように、オブジェクトを文字列に変換する必要がある場合、この関数を自動的に呼び出します。
    // 今回、toStringメソッドはRGB値、16進数表記、2進数表記の情報を含む文字列を返すようにオーバーライドされています。
    public String toString(){
        return "The color is rgb(" + this.red + "," + this.green + "," + this.blue + "). Hex: " + this.getHex() + ", binary: " + this.getBits();
    }
}

class Main{
    public static void main(String[] args){
        RGB24 color1 = new RGB24(0, 153, 255);
        RGB24 color2 = new RGB24("ff99cc"); //rgb(255, 153, 204)
        RGB24 color3 = new RGB24("100110011111111100110011"); //rgb(153, 255, 51)
        RGB24 gray = new RGB24("7b7b7b"); //rgb(123, 123, 123)

        System.out.println(color1);
        System.out.println(color2);
        System.out.println(color3);
        System.out.println(gray);
        
        System.out.println();	
        System.out.println("Changing the state of colors");
        System.out.println();
        
        // 状態の変更
        gray.setAsBlack();
        System.out.println(gray);
        color1.setColorsByHex("2EB656");
        System.out.println(color1);
    }
}
