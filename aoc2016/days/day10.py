import copy

from django.db.models import Q, Count
from aoc2016.models.day10 import BalanceBot, Instruction, Microchip, Output

midComparison = False

def Init():
    for inst in Instruction.objects.all():
        inst.delete()
    for out in Output.objects.all():
        out.delete()
    for chip in Microchip.objects.all():
        chip.delete()
    for bot in BalanceBot.objects.all():
        bot.delete()

def Summarize():
    for outtie in Output.objects.all().order_by('outId'):
        print(outtie)

def Process(input):
    Init()
    idx = 0
    for item in input.split("\n"):
        if item != "":
            idx += 1
            key0 = item[:6]
            if key0 == "value ":
                nums = item[6:].split(" goes to bot ")
                try:
                    BotReceivesChip(int(nums[1]), int(nums[0]))
                except:
                    print(item)
                    raise
            else:
                bot0 = item.split(" gives low to ")
                bot1 = bot0[1].split(" and high to ")

                fromBot = int(bot0[0].split("bot ")[1])

                low = bot0[1].split(" ")
                lowType = low[0]
                lowNumb = int(low[1])
                
                high = bot1[1].split(" ")
                highType = high[0]
                highNumb = int(high[1])

                BotGetsInstructions(fromBot, lowType, lowNumb, highType, highNumb)

    """ After all the bots are loaded, begin """
    ActivateBots()

def IdentifyBot(botId: int):
    bots = BalanceBot.objects.filter(botId=botId)
    if len(bots) > 0:
        bot = bots[0]
    else:
        bot = BalanceBot(botId=botId)
        bot.save()
    
    return bot

def IdentifyChip(val: int):
    chips = Microchip.objects.filter(value=val)
    if len(chips) > 0:
        chip = chips[0]
    else:
        chip = Microchip(value=val)
        chip.save()
    
    return chip

def IdentifyOutput(outId: int):
    outputs = Output.objects.filter(outId=outId)
    if len(outputs) > 0:
        output = outputs[0]
    else:
        output = Output(outId=outId)
        output.save()
    
    return output
    
def BotReceivesChip(botId: int, val: int):
    global midComparison

    bot = IdentifyBot(botId)
    chip = IdentifyChip(val)

    chip.botHolding = bot
    chip.save()

def OutputChip(outId: int, val: int):
    out = IdentifyOutput(outId)
    out.chip1 = IdentifyChip(val)
    out.save()

    print(out, "gets chip", val)

def BotGetsInstructions(botId: int, lowType, low, highType, high):
    bot = IdentifyBot(botId)

    inst = Instruction(keyBot=bot)
    inst.condition = "low"
    inst.target = lowType
    inst.num = low
    inst.save()
    
    inst = Instruction(keyBot=bot)
    inst.condition = "high"
    inst.target = highType
    inst.num = high
    inst.save()

def BotComparesChips(bot: BalanceBot):
    global midComparison
    midComparison = True

    chipsHeld = Microchip.objects.filter(botHolding=bot)
    instructions = Instruction.objects.filter(keyBot=bot)

    if len(instructions) < 2:
        print("A bot without instructions has two chips, check for that in instructions!")
        midComparison = False
    elif len(chipsHeld) < 2:
        print("This is stupid, why are we here", bot)
    else:
        """ Special case we care about """
        if chipsHeld[0].value == 17 and chipsHeld[1].value == 61:
            print("This is one kind of neat")
        elif chipsHeld[1].value == 17 and chipsHeld[0].value == 61:
            print("This is another kind of neat")
            print("MR IMPORTANT!", bot, chipsHeld[0], chipsHeld[1])
        
        """ Clear these chips out of the robots hands """
        for chip in chipsHeld:
            chip.botHolding = None
            chip.save()

        """ Distribute based on comparison rules """
        if chipsHeld[0].value < chipsHeld[1].value:
            lowChip = chipsHeld[0].value
            highChip = chipsHeld[1].value
        else:
            lowChip = chipsHeld[1].value
            highChip = chipsHeld[0].value

        for instr in instructions:
            chipValue = lowChip if instr.condition == "low" else highChip
            if instr.target == "bot":
                BotReceivesChip(instr.num, chipValue)
            else:
                OutputChip(instr.num, chipValue)

def ActivateBots():
    haveWorkToDo = True
    while haveWorkToDo:
        counts = BalanceBot.objects.annotate(
            chips=Count('microchip')
        ).filter(chips=2)
        if (len(counts)) < 1:
            haveWorkToDo = False
        for ready in counts:
            bot = IdentifyBot(ready.botId)
            BotComparesChips(bot)
