#!/usr/bin/python
 
motorPrev=286
motorCurr=320
motorPrevDate="25/11/13"
motorCurrDate="22/09/13"
 
mainPrev=34518
mainCurr=35301
mainPrevDate="17/09/13"
mainCurrDate="24/11/13"
 
ffCurr=5484
ffPrev=4950
ffPrevDate="26/11/13"
ffCurrDate="17/09/13"
money = 4961
unit = 782
 
 
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
