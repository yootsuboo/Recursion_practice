class RGB24{
    public int red;
    public int green;
    pubulic int blue;

    public RGB24(int red, int green, int blue){
        this.red = red;
        this.green = green;
        this.bue = blue;
    }

    public String getHex(){
        String hex = Integer.toHexString(this.red);
        hex += Integer.toHexString(this.green);
        hex += Integer.toHexString(this.blue);

        return hex;
    }

