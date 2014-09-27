#!/usr/bin/python

class Reading(object):
    def __init__(self, valCurr, valPrev, dateCurr, datePrev):
        self.valCurr  = valCurr
        self.valPrev  = valPrev
        self.dateCurr = dateCurr
        self.datePrev = datePrev
        self.valConsumed  = valCurr - valPrev

# This comes from the water motor reading
motor = Reading(
    valPrev  = 436,
    valCurr  = 472,
    datePrev = "18/07/14",
    dateCurr = "27/09/14"
)

# This comes from the FF meter
ff = Reading(
    valPrev  = 6239,
    valCurr  = 6472,
    datePrev = "18/07/14",
    dateCurr = "27/09/14"
)

# This comes from the bill
main = Reading(
    valPrev  = 37900,
    valCurr  = 38645,
    datePrev = "18/07/14",
    dateCurr = "23/09/14",
)

money = 4049
unit  = 745
 
msg='''
 
Main Reading:
-------------
CUR: {mainCurr}: {mainCurrDate}
PREV: {mainPrev}: {mainPrevDate}
 
Money/Unit = Per Unit
{money}/{unit} = {perUnit}
 
Motor Reading:
--------------
{motorCurr} {motorCurrDate}
{motorPrev} {motorPrevDate}
 
(Curr - Prev)/2 = Consumed Per Head
({motorCurr} - {motorPrev})/2 = {perHeadMotor}
 
FirstFloor Reading:
------------------
{ffCurr} {ffCurrDate}
{ffPrev} {ffPrevDate}
 
Curr - Prev = FirstFloor
{ffCurr} - {ffPrev} = {ffConsumed}
 
Total:
------
FirstFloor + Motor = Total Units (Consumed by FirstFloor)
{ffConsumed} + {perHeadMotor} = {ffTotalConsumed}
 
Money:
------
TotalUnits * PerUnit = MoneyDue
{ffTotalConsumed} * {perUnit} = {moneyDue}
'''
 
perUnit         = money/float(unit)
perHeadMotor    = motor.valConsumed/2.0
ffTotalConsumed = ff.valConsumed + perHeadMotor

print msg.format(
    mainCurr        = main.valCurr,
    mainPrev        = main.valPrev,
    mainCurrDate    = main.dateCurr,
    mainPrevDate    = main.datePrev,

    motorCurr       = motor.valCurr,
    motorPrev       = motor.valPrev,
    motorCurrDate   = motor.dateCurr,
    motorPrevDate   = motor.datePrev,

    ffCurr          = ff.valCurr,
    ffPrev          = ff.valPrev,
    ffCurrDate      = ff.dateCurr,
    ffPrevDate      = ff.datePrev,

    money           = money,
    unit            = unit,
    perUnit         = perUnit,

    perHeadMotor    = perHeadMotor,
    ffConsumed      = ff.valConsumed,
    ffTotalConsumed = ff.valConsumed + perHeadMotor,
    moneyDue        = ffTotalConsumed * perUnit
)
