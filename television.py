class Television:
    MIN_Volume = 0
    MAX_Volume = 2
    MIN_Channel = 0
    MAX_Channel = 3

    def __init__(self) -> None:
        """
        Initially sets tv power to off, mute to off, volume to 0, channel to 0.
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_Volume
        self.__channel = Television.MIN_Channel

    def power(self) -> None:
        """
        Method to turn on and off tv.
        """
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False

    def mute(self) -> None:
        """
        Method to turn mute and unmute tv.
        """
        if self.__status:
            if self.__muted == False:
                self.__muted = True
            else:
                self.__muted = False

    def channel_up(self) -> None:
        """
        Method to increase the tv channel.
        """
        if self.__status:
            if self.__channel < Television.MAX_Channel:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_Channel

    def channel_down(self) -> None:
        """
        Method to decrease the tv channel.
        """
        if self.__status:
            if self.__channel > Television.MIN_Channel:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_Channel

    def volume_up(self) -> None:
        """
        Method to increase the tv volume.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_Volume:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Method to decrease the tv volume.
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_Volume:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Method to show the tv status.
        :return: tv status.
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_Volume}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'