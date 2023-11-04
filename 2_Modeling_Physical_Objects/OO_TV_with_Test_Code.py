import TV

oTV = TV.TV()  # TV 클래스 객체 생성

# TV 켜고 상태 출력
oTV.power()
oTV.showInfo()

# 채널 두 번 위로 이동 후 볼륨 두 단계 낮추고 상태 출력
oTV.channelUp()
oTV.channelUp()
oTV.volumeUp()
oTV.volumeUp()
oTV.showInfo()

# TV 끄고 상태 출력, TV 켜고 다시 상태 출력
oTV.power()
oTV.showInfo()
oTV.power()
oTV.showInfo()

# 볼륨 하나 낮추고 음소거 활성화 후 상태 출력
oTV.volumeDown()
oTV.mute()
oTV.showInfo()

# 채널 11로 변경 후 음소거 활성화 후 상태 출력
oTV.setChannel(11)
oTV.mute()
oTV.showInfo()

