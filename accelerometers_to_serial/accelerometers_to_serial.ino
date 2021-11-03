
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

  // Send DEVICE_STARTED
  Serial.println(0x0);
  if (!mpu.begin()) { // Change address if needed

    // Send NO_ACCELEROMETER
    Serial.println(0xe0);
    while (1) {
      delay(10);
    }
  } else {

    // Send ACCELEROMETER_DETECTED
    Serial.println(0xe1);
  }

  // Configure MPU6050
  mpu.setAccelerometerRange(MPU6050_RANGE_16_G);
  mpu.setGyroRange(MPU6050_RANGE_250_DEG);
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
}

void loop() {

  // Retrieve informations from MPU6050
  readMPU();

  // Delays 20 ms (better accuracy)
  delay(20);
}

void readMPU( ) {
  // Read MPU6050 datas
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  // Retrieve relevant metrics
  wy = g.gyro.y;
  wz = g.gyro.z;

  // If player is moving, transmit relevant datas
  if (abs(wy) > 0.05) {

    // Send Y_GYRO
    Serial.println(0x21);
    Serial.println(wy);
    Serial.println(millis() - myTime);
  }
  if (abs(wz) > 0.05) {

    // Send Z_GYRO
    Serial.println(0x22);
    Serial.println(wz);
    Serial.println(millis() - myTime);
  }

  // Update execution time
  myTime = millis();
}
