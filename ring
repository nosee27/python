class naozhong:
    id=None
    def ring(self):
       import winsound
       winsound.Beep(2000,3000)

clock =naozhong()
clock.id="明明"
clock.ring()
