#!/usr/bin/python

# This comes from the motor meter
motorCurr=368
motorPrev=346
motorCurrDate="22/03/14"
motorPrevDate="25/01/14"

# This comes from the FF meter
ffCurr=5835
ffPrev=5649
ffCurrDate="22/03/14"
ffPrevDate="25/01/14"

# This comes from the bill
mainPrev=36031
mainCurr=36499
mainCurrDate="21/03/14"
mainPrevDate="25/01/14"
money = 2323
unit = 468
 
 
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
 
ffConsumed = ffCurr - ffPrev
perUnit = money/float(unit)
perHeadMotor = (motorCurr - motorPrev)/float(2)
ffTotalConsumed = ffConsumed + perHeadMotor
print msg.format(
    mainCurr = mainCurr,
    mainCurrDate = mainCurrDate,
    mainPrev = mainPrev,
    mainPrevDate = mainPrevDate,
    money = money,
    unit  = unit,
    perUnit = perUnit,
    motorCurr = motorCurr,
    motorPrev = motorPrev,
    motorCurrDate = motorCurrDate,
    motorPrevDate = motorPrevDate,
    perHeadMotor = perHeadMotor,
    ffCurr = ffCurr,
    ffPrev = ffPrev,
    ffCurrDate = ffCurrDate,
    ffPrevDate = ffPrevDate,
    ffConsumed = ffConsumed,
    ffTotalConsumed = ffConsumed + perHeadMotor,
    moneyDue = ffTotalConsumed * perUnit
)
