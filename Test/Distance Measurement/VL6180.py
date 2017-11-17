import GPIO as GPIO
import I2C as I2C
import VL6180_Constants as CON

class Distance:
    def __init__(self):
        self.i2c = I2C.Device(0x29, I2C.get_default_bus)
        self.init()
        self.default_settings()

    def init(self):
        if self.i2c.readU8(CON.VL6180_SYSTEM_FRESH_OUT_OF_RESET) != 1:
            raise RuntimeError("Faliure reset")

        #Required by datasheet
        #http://www.st.com/st-web-ui/static/active/en/resource/technical/document/application_note/DM00122600.pdf
        self.i2c.write8(0x0207, 0x01)
        self.i2c.write8(0x0208, 0x01)
        self.i2c.write8(0x0096, 0x00)
        self.i2c.write8(0x0097, 0xfd)
        self.i2c.write8(0x00e3, 0x00)
        self.i2c.write8(0x00e4, 0x04)
        self.i2c.write8(0x00e5, 0x02)
        self.i2c.write8(0x00e6, 0x01)
        self.i2c.write8(0x00e7, 0x03)
        self.i2c.write8(0x00f5, 0x02)
        self.i2c.write8(0x00d9, 0x05)
        self.i2c.write8(0x00db, 0xce)
        self.i2c.write8(0x00dc, 0x03)
        self.i2c.write8(0x00dd, 0xf8)
        self.i2c.write8(0x009f, 0x00)
        self.i2c.write8(0x00a3, 0x3c)
        self.i2c.write8(0x00b7, 0x00)
        self.i2c.write8(0x00bb, 0x3c)
        self.i2c.write8(0x00b2, 0x09)
        self.i2c.write8(0x00ca, 0x09)
        self.i2c.write8(0x0198, 0x01)
        self.i2c.write8(0x01b0, 0x17)
        self.i2c.write8(0x01ad, 0x00)
        self.i2c.write8(0x00ff, 0x05)
        self.i2c.write8(0x0100, 0x05)
        self.i2c.write8(0x0199, 0x05)
        self.i2c.write8(0x01a6, 0x1b)
        self.i2c.write8(0x01ac, 0x3e)
        self.i2c.write8(0x01a7, 0x1f)
        self.i2c.write8(0x0030, 0x00)

    def default_settings(self):
        #Recommended settings from datasheet
        #http://www.st.com/st-web-ui/static/active/en/resource/technical/document/application_note/DM00122600.pdf

        #Enable Interrupts on Conversion Complete (any source)
        self.i2c.write8(CON.VL6180_SYSTEM_INTERRUPT_CONFIG_GPIO, (4 << 3)|(4))  #Set GPIO1 high when sample complete

        self.i2c.write8(CON.VL6180_SYSTEM_MODE_GPIO1, 0x10)              #Set GPIO1 high when sample complete
        self.i2c.write8(CON.VL6180_READOUT_AVERAGING_SAMPLE_PERIOD, 0x30)#Set Avg sample period
        self.i2c.write8(CON.VL6180_SYSALS_ANALOGUE_GAIN, 0x46)           #Set the ALS gain
        self.i2c.write8(CON.VL6180_SYSRANGE_VHV_REPEAT_RATE, 0xFF)       #Set auto calibration period (Max = 255)/(OFF = 0)
        self.i2c.write8(CON.VL6180_SYSALS_INTEGRATION_PERIOD, 0x63)      #Set ALS integration time to 100ms
        self.i2c.write8(CON.VL6180_SYSRANGE_VHV_RECALIBRATE, 0x01)       #perform a single temperature calibration

        #Optional settings from datasheet
        #http://www.st.com/st-web-ui/static/active/en/resource/technical/document/application_note/DM00122600.pdf
        self.i2c.write8(CON.VL6180_SYSRANGE_INTERMEASUREMENT_PERIOD, 0x09)      #Set default ranging inter-measurement period to 100ms
        self.i2c.write8(CON.VL6180_SYSALS_INTERMEASUREMENT_PERIOD, 0x0A)        #Set default ALS inter-measurement period to 100ms
        self.i2c.write8(CON.VL6180_SYSTEM_INTERRUPT_CONFIG_GPIO, 0x24)          #Configures interrupt on 'New Sample Ready threshold event'

        #Additional settings defaults from community
        self.i2c.write8(CON.VL6180_SYSRANGE_MAX_CONVERGENCE_TIME, 0x32)
        self.i2c.write8(CON.VL6180_SYSRANGE_RANGE_CHECK_ENABLES, 0x10 | 0x01)
        self.i2c.write16(CON.VL6180_SYSRANGE_EARLY_CONVERGENCE_ESTIMATE, 0x7B)
        self.i2c.write16(CON.VL6180_SYSALS_INTEGRATION_PERIOD, 0x64)

        self.i2c.write8(CON.VL6180_READOUT_AVERAGING_SAMPLE_PERIOD, 0x30)
        self.i2c.write8(CON.VL6180_SYSALS_ANALOGUE_GAIN, 0x40)
        self.i2c.write8(CON.VL6180_FIRMWARE_RESULT_SCALER, 0x01)


    def singel_meassurement(self):
        if self.i2c.readU8(CON.VL6180_RESULT_RANGE_STATUS) != 0x1:
            #Device is busy and not ready to take measurements
            pass

        self.i2c.write8(CON.VL6180_SYSRANGE_START, 0x1)  #Start a singel measurement

        #wait until measurement is complete
        while self.i2c.readU8(CON.VL6180_RESULT_INTERRUPT_STATUS_GPIO) != 0x3:
            pass    #Do nothing

        #measurement in mm
        measurement = self.i2c.readU8(CON.VL6180_RESULT_RANGE_VAL)

        self.i2c.write8(CON.VL6180_SYSTEM_INTERRUPT_CLEAR, 0x7)

        return measurement


