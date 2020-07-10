from django.db import models

class BalanceBot(models.Model):
    """ Collects two microchips, then acts """
    botId = models.IntegerField()
    
    def __str__(self):
        return "bot " + str(self.botId)
    
class Microchip(models.Model):
    """ Simple microchip with an integer value embedded in storage """
    botHolding = models.ForeignKey(BalanceBot, on_delete=models.CASCADE, blank=True, null=True)
    value = models.IntegerField()
    
    def __str__(self):
        return "chip " + str(self.value)

class Output(models.Model):
    """ Receptable for microchips that a bot is done with """
    outId = models.IntegerField()

    chip1 = models.ForeignKey(Microchip, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        if self.chip1 != None:
            return "output " + str(self.outId) + " holds " + str(self.chip1)
        else:
            return "output " + str(self.outId)

class Instruction(models.Model):
    """ Instructs a bot what to do with low and high chips """
    keyBot = models.ForeignKey(BalanceBot, on_delete=models.CASCADE)

    condition = models.CharField(max_length=20) # low, high
    num = models.IntegerField()
    target = models.CharField(max_length=20) # bot, output
    
    def __str__(self):
        return "instructions for " + str(self.keyBot) + " " + self.condition + " to " + self.target + " " + str(self.num)