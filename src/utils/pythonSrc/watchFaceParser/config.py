class Config:
    _is_gtr = False
    _is_gts = False
    _image_size = (360, 360)
    _preview_size = (210, 210)


    @staticmethod
    def setGtrMode(gtr):
        Config._is_gtr = gtr
        if Config._is_gtr == 47:
            Config._image_size = (454, 454)
            Config._preview_size = (266, 266)
        if Config._is_gtr == 42:
            Config._image_size = (390, 390)
            Config._preview_size = (266, 266)

    @staticmethod
    def isGtrMode():
        return Config._is_gtr

    @staticmethod
    def setGtsMode(gts):
        Config._is_gts = 40
        Config._image_size = (348,442)
        Config._preview_size = (210,266)

    @staticmethod
    def isGtsMode():
        return Config._is_gts

    @staticmethod
    def getImageSize():
        return Config._image_size


    @staticmethod
    def getImageSizeHalf():
        return (int(Config._image_size[0] / 2),int(Config._image_size[1] / 2))


    @staticmethod
    def getPreviewSize():
        # return (Config._preview_size, Config._preview_size)
        return Config._preview_size

