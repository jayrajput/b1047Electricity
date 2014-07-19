#!/usr/bin/python

# This comes from the motor meter
motorPrev=368
motorCurr=396
motorPrevDate="22/03/14"
motorCurrDate="21/05/14"

# This comes from the FF meter
ffPrev=5835
ffCurr=5937
ffPrevDate="22/03/14"
ffCurrDate="21/05/14"

# This comes from the bill
mainCurr=36922
mainPrev=36499
mainPrevDate="21/03/14"
mainCurrDate="19/05/14"
money = 2083
unit = 423
 
 
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
