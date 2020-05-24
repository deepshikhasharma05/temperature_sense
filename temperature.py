# import wire.h
# import SparkFunMLX90614.h
# import SPI.h
# import Adafruit_GFX.h
# import Adafruit_SSD1306.h
#If using software SPI (the default case):
#define OLED_MOSI   9
#define OLED_CLK   10
#define OLED_DC    11
#define OLED_CS    12
#define OLED_RESET 13
#Adafruit_SSD1306 display(OLED_MOSI, OLED_CLK, OLED_DC, OLED_RESET, OLED_CS);

#IRTherm therm

def setup():
    Serial.begin(9600); 
    therm.begin(); 
    therm.setUnit(TEMP_C); 
    display.begin(SSD1306_SWITCHCAPVCC);
    display.clearDisplay();
    display.setRotation(2);
  

temperature = 0
runner = 0

def loop():

    if therm.read():# On success, read() will return 1, on fail 0.
        
        temperature = String(therm.object(), 2);
        Serial.print("Object: ");
        Serial.print(temperature); Serial.println("C");
        display.clearDisplay();
        runner=runner+1;
        delay(5);
        

        display.setTextSize(2);
        display.setTextColor(WHITE);
        display.setCursor(display.width()/4,display.height()/12);
        
        if therm.object()>=100:
            display.setCursor(display.width()/4,display.height()/12);
            
            display.println(temperature);

            display.drawLine(display.width()/runner,display.height() - display.height()/2.5, display.width()/runner+1, display.height() - display.height()/2.5, WHITE);

            display.setCursor(0,display.height()-display.height()/4);
            display.setTextSize(1);
            display.println("   Arduino Thermlgun");
            display.setCursor(display.width()- display.width()/4,display.height()/12);
            display.println("deg C");
            display.display();

        if runner>20:
            runner=0;


    

