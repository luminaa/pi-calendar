#include <Wire.h>
#include "rgb_lcd.h"

rgb_lcd lcd;

void setup() {
    Serial.begin(9600);
    lcd.begin(16, 2);
    lcd.write("LCD Ready");
}

void loop() {
    if (Serial.available() > 0) {
        lcd.clear();
        String summary = "";
        String start = "";

        while (Serial.available()) {
            summary = Serial.readStringUntil('\n');
            start = Serial.readStringUntil('\n');
        }
        delay(1000);
        lcd.setCursor(0, 0);
        lcd.print(summary);
        lcd.setCursor(0, 1);
        lcd.print(start);
    }
}