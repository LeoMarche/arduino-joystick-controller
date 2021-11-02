
//Libraries
#include <Wire.h>//https://www.arduino.cc/en/reference/wire
#include <Adafruit_MPU6050.h>//https://github.com/adafruit/Adafruit_MPU6050
#include <Adafruit_Sensor.h>//https://github.com/adafruit/Adafruit_Sensor

//Objects
Adafruit_MPU6050 mpu;
float wy, wz;
unsigned long myTime;

void setup() {
  //Init Serial USB
  Serial.begin(9600);
  Serial.println(0x0);
  if (!mpu.begin()) { // Change address if needed
    Serial.println(0xe0);
    while (1) {
      delay(10);
    }
  } else {
    Serial.println(0xe1);
  }

  mpu.setAccelerometerRange(MPU6050_RANGE_16_G);
  mpu.setGyroRange(MPU6050_RANGE_250_DEG);
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
}

void loop() {
  readMPU();
  delay(100);
}

void readMPU( ) { /* function readMPU */
  ////Read acceleromter data
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  wy = g.gyro.y;
  wz = g.gyro.z;

  if (abs(wy) > 0.2) {
    Serial.println(0x21);
    Serial.println(wy);
    Serial.println(millis() - myTime);
  }
  if (abs(wz) > 0.2) {
    Serial.println(0x22);
    Serial.println(wz);
    Serial.println(millis() - myTime);
  }
  myTime = millis();
}
