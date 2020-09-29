class Range():

    def isMilHair(self, red, green, blue):
        if 132 <= blue <= 240 and 51 <= green <= 116 and 45 <= red <= 92:
            return True
        return False

    def isMilShirt(self, red, green, blue):
        if 181 <= blue <= 222 and 141 <= green <= 188 and 182 <= red <= 223:
            return True

        return False

    def isMilShorts(self, red, green, blue):
        if 0 <= blue <= 20 and 0 <= green <= 20 and 120 <= red <= 240:
            return True

        return False

    def isApuBody(self, red, green, blue):
        if 88 <= red <= 222 and 30 <= green <= 102 and 0 <= blue <= 40:
            return True

        return False

    def isApuShirt(self, red, green, blue):
        if 0 <= red <= 40 and 30 <= green <= 251 and 0 <= blue <= 52:
            return True

        return False

    def isApuPants(self, red, green, blue):
        if 188 <= red <= 221 and 174 <= green <= 211 and 118 <= blue <= 201:
            return True

        return False

        return False
