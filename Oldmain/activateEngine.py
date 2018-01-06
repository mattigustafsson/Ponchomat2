import time
from MCP23017 import Adafruit_MCP230XX

mcp = Adafruit_MCP230XX(0x20, 16)


def Rotate_Enginge(HowLong):
    mcp.config(0, mcp.OUTPUT)
    mcp.config(1, mcp.OUTPUT)
    mcp.config(2, mcp.OUTPUT)

    mcp.output(0, mcp.HIGH)
    mcp.output(2, mcp.HIGH)

    time.sleep(HowLong)

    mcp.output(2, mcp.LOW)
    mcp.output(1, mcp.HIGH)
    time.sleep(0.15)
    mcp.output(1, mcp.LOW)
    mcp.output(0, mcp.LOW)


def main():
    Rotate_Enginge(3)


if __name__ == '__main__':
    main()
