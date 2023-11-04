# 절차적
# 조명 스위치

def turnOn():
    global switchIsOn
    # 조명을 켠다
    switchIsOn = True


def turnOff():
    global switchIsOn
    # 조명 끄기
    switchIsOn = False

# 메인
switchIsOn = False  # 전역 불리언 변수

# 검증 코드
print(switchIsOn)
turnOn()
print(switchIsOn)
turnOff()
print(switchIsOn)
turnOn()
print(switchIsOn)


# 객체지향 조명 스위치 LightSwitch 클래스

class LightSwitch():
    def __init__(self):
        self.switchIsOn = False

    def turnOn(self):
        self.switchIsOn = True

    def turnOff(self):
        self.switchIsOn = False
        
