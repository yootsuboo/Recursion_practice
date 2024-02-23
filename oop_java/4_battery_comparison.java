class Battery{
    public String manufacturer;
    public String model;
    public double voltage;
    public double ampHours;
    public double weightKg;
    public double[] dimensionMm;

    public Battery(String manufacturer, String model, double voltage, double ampHours, double weightKg, double wMm, double hMm, double dMm){
        this.manufacturer = manufacturer;
        this.model = model;
        this.voltage = voltage;
        this.ampHours = ampHours;
        this.weightKg = weightKg;
        this.dimensionMm = new double[]{wMm, hMm, dMm};
    }

    public String toString(){
        String referenceHash = Integer.toHexString(this.hashCode());
        return this.manufacturer + " " + this.model + ": " + this.getPowerCapacity() + "Wh (" + this.voltage + "V/" + this.ampHours + "Ah) - " + this.dimensionMm[0] + "(W)x" + this.dimensionMm[1] + "(H)x" + this.dimensionMm[2] + "(D) " + this.weightKg + "kg .... Instance Reference:" + referenceHash;
    }

    public double getPowerCapacity(){
        return this.voltage * this.ampHours;
    }
}

class Main {
    public static void main(String[] args) {
        // "VTec"メーカーの"MC96"モデルという新しいバッテリーオブジェクト(mc96)を作成します
        Battery mc96 = new Battery("VTec", "MC96", 14.4, 6.6, 0.55, 72, 97, 51.5);

        // mc96の参照をmc96Secondにコピーします。これは「シャローコピー」を意味します。つまり、mc96Secondはmc96と同じオブジェクトを指しています
        Battery mc96Second = mc96;

        // mc96と同じ値を持つ新しいバッテリーオブジェクト(mc96Third)を作成します。これは「ディープコピー」を意味します。つまり、mc96Thirdはmc96と同じ属性を持つ新しいオブジェクトです
        Battery mc96Third = new Battery("VTec", "MC96", 14.4, 6.6, 0.55, 72, 97, 51.5);

        // "Atomic Units"メーカーの"MD-LS95"モデルという新しいバッテリーオブジェクト(mdLs95)を作成します
        Battery mdLs95 = new Battery("Atomic Units", "MD-LS95", 14.4, 6.6, 0.55, 72, 97, 51.5);

        // mc96, mc96Second, mc96Third, mdLs95の各オブジェクトの情報を出力します
        System.out.println(mc96);
        System.out.println();
        System.out.println(mc96Second);
        System.out.println();
        System.out.println(mc96Third);
        System.out.println();
        System.out.println(mdLs95);

        System.out.println();

        // mc96がmc96自身と等しいか（つまり、同じオブジェクトを参照しているか）をチェックします。結果はTrueになります
        System.out.println(mc96 == mc96); //True

        // mc96がmc96Secondと等しいか（つまり、同じオブジェクトを参照しているか）をチェックします。mc96Secondはmc96のシャローコピーなので、結果はTrueになります
        System.out.println(mc96 == mc96Second); //True

        // mc96がmc96Thirdと等しいか（つまり、同じオブジェクトを参照しているか）をチェックします。mc96Thirdはmc96のディープコピー（別のオブジェクト）なので、結果はFalseになります
        System.out.println(mc96 == mc96Third); //False

        // mc96がmdLs95と等しいか（つまり、同じオブジェクトを参照しているか）をチェックします。mdLs95は完全に別のオブジェクトなので、結果はFalseになります
        System.out.println(mc96 == mdLs95); //False
    }
}
