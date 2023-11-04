
class LightSwitch():
    def __init__(self):
        self.switchIsOn = False

    def turnOn(self):
        self.switchIsOn = True

    def turnOff(self):
        self.switchIsOn = False

    def show(self):
        print(self.switchIsOn)

# 메인
oLightSwitch1 = LightSwitch()  # LightSwitch 객체 생성
oLightSwitch2 = LightSwitch()  # 다른 LightSwitch 객체 생성

oLightSwitch1.show()
oLightSwitch2.show()
oLightSwitch1.turnOn()
oLightSwitch2.turnOff()
oLightSwitch1.show()
oLightSwitch2.show()
