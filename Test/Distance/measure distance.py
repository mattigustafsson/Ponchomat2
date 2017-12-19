from proximity import VL6180X

DistSensor = VL6180X(1)

def read_distance():
    dist = DistSensor.read_distance()
    return dist

def main():
    print read_distance()

if __name__ == '__main__':
    main()
    