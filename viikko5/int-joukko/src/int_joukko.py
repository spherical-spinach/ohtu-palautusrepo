class IntJoukko:
    KAPASITEETTI = 5
    OLETUSKASVATUS = 5

    def _luo_lista(self, koko):
        return [0] * koko

    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = self._set_kapasiteetti(kapasiteetti)
        self.kasvatuskoko = self._set_kasvatuskoko(kasvatuskoko)
        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def _set_kapasiteetti(self, kapasiteetti):
        if kapasiteetti is None:
            return self.KAPASITEETTI
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")
        return kapasiteetti

    def _set_kasvatuskoko(self, kasvatuskoko):
        if kasvatuskoko is None:
            return self.OLETUSKASVATUS
        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Väärä kasvatuskoko")
        return kasvatuskoko

    def kuuluu(self, n):
        return n in self.ljono[:self.alkioiden_lkm]

    def lisaa(self, n):
        if self.kuuluu(n):
            return False

        if self.alkioiden_lkm >= len(self.ljono):
            self._kasvata_lista()

        self.ljono[self.alkioiden_lkm] = n
        self.alkioiden_lkm += 1
        return True

    def _kasvata_lista(self):
        uusi_lista = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
        for i in range(self.alkioiden_lkm):
            uusi_lista[i] = self.ljono[i]
        self.ljono = uusi_lista

    def poista(self, n):
        for i in range(self.alkioiden_lkm):
            if self.ljono[i] == n:
                self.ljono[i:] = self.ljono[i + 1:self.alkioiden_lkm] + [0]
                self.alkioiden_lkm -= 1
                return True
        return False

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    def mahtavuus(self):
        return self.alkioiden_lkm

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        for i in a.to_int_list() + b.to_int_list():
            x.lisaa(i)
        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        for i in a.to_int_list():
            if b.kuuluu(i):
                y.lisaa(i)
        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        for i in a.to_int_list():
            z.lisaa(i)
        for i in b.to_int_list():
            z.poista(i)
        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        return "{" + ", ".join(str(self.ljono[i]) for i in range(self.alkioiden_lkm)) + "}"
