# encoding:utf-8

class TV():
    def __init__(self):
        self.isOn = False
        self.isMuted = False

        # 선택할 수 있는 기본 채널 목록
        self.channelList = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]
        self.nChannels = len(self.channelList)
        self.channelIndex = 0
        self.VOLUME_MINIMUM = 0  # 상수
        self.VOLUME_MAXIMUM = 10  # 상수
        self.volume = self.VOLUME_MAXIMUM // 2  # 볼륨의 초깃값을 최대로 설정

    def power(self):
        self.isOn = not self.isOn  # 토글(값 뒤집기)

    def volumeUp(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False  # 음소거가 활성화됐을 때 볼륨을 조절하면 음소거 비활성화 시키기
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume += 1

    def volumeDown(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False  # 음소거가 활성화됐을 때 볼륨을 조절하면 음소거 비활성화 시키기
        if self.volume > self.VOLUME_MINIMUM:
            self.volume -= 1

    def channelUp(self):
        if not self.isOn:
            return
        self.channelIndex += 1
        if self.channelIndex == self.nChannels:
            self.channelIndex = 0  # 마지막 채널 다음 다시 첫번째 채널로 이동

    def channelDown(self):
        if not self.isOn:
            return
        self.channelIndex -= 1
        if self.channelIndex < 0:
            self.channelIndex -= 1  # 첫 번째 채널 다음은 마지막 채널로 이동

    def mute(self):
        if not self.isOn:
            return
        self.isMuted = not self.isMuted

    def setChannel(self, newChannel):
        if newChannel in self.channelList:
            self.channelIndex = self.channelList.index(newChannel)

    def showInfo(self):
        print()
        print('TV Status:')
        if self.isOn:
            print('     TV 전원 상태: 켜짐')
            print('     Channel is:', self.channelList[self.channelIndex])
            if self.isMuted:
                print('     볼륨:', self.volume, '(음소거)')
            else:
                print('     볼륨:', self.volume)
        else:
            print('     TV 전원 상태: 꺼짐')









