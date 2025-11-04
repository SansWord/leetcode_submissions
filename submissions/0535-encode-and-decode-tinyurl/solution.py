class Codec:

    short_long = {}
    long_short = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """

        if longUrl in Codec.long_short:
            return Codec.long_short[longUtl]

        r = self.getRandomShort()

        while r in Codec.short_long:
            r = self.getRandomShort()

        Codec.short_long[r] = longUrl
        Codec.long_short[longUrl] = r

        return r
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """

        if shortUrl in Codec.short_long:
            return Codec.short_long[shortUrl]

        return None


    def getRandomShort(self) -> str:
        characters = string.ascii_letters + string.digits

        return "".join(random.choice(characters) for i in range(6))
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
