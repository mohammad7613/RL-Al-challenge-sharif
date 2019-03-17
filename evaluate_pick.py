# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 20:05:22 2019

@author: mandy
"""

import numpy as np
from Model import *
from enum import Enum


class AbilityName(Enum):
    SENTRY_ATTACK = "SENTRY_ATTACK"
    SENTRY_DODGE = "SENTRY_DODGE"
    SENTRY_RAY = "SENTRY_RAY"
    BLASTER_ATTACK = "BLASTER_ATTACK"
    BLASTER_DODGE = "BLASTER_DODGE"
    BLASTER_BOMB = "BLASTER_BOMB"
    HEALER_ATTACK = "HEALER_ATTACK"
    GUARDIAN_HEAL = "HELAR_HEAL"
    HEALER_DODGE = "HEALER_DODGE" 
    GUARDIAN_ATTACK = "GUARDIAN_ATTACK"
    GUARDIAN_DODGE = "GUARDIAN_DODGE"
    GUARDIAN_FORTIFY = "GUARDIAN_FORTIFY"
def evaluate_pick(world=None):
    world=World();
    value=np.zeros(65536)
    count=0
    numberofwall=0;
    for i in range(31):
        for j in range(31):
            cell=world.map.get_cell(i,j)
            if cell in world.map.objective_zone and cell.is_wall:
                numberofwall+=1
            else:
                f=0
                for cells in world.map.objective_zone:
                    if world.manhattan_distance(cells,cell)<=2:
                        f=1;
                        break;
                if(f==1):
                    numberofwall+=1
    flag=0               
    if(numberofwall>5):
       flag=1            
    for a in range(4):
        for a1 in range(4):
            for b in range(4):
                for b1 in range(4):
                    for c in range(4):
                       for c1 in range(4):
                           for d in range(4):
                               for d1 in range(4):
                                    score=0
                                    my=[a,b,c,d]
                                    opp=[a1,b1,c1,d1]
                                    for i in my:
                                        if(i==0):
                                            ab1=world.get_ability_constants(AbilityName.SENTRY_ATTACK)#make function get_ability_constants public
                                            score+=(ab1.area_of_effect+3*ab1.power+ab1.range-2*ab1.ap_cost-0.5*ab1.cooldown)
                                            if flag==1 and ab1.is_lobbing:
                                                score+=10
                                            ab1=world.get_ability_constants(AbilityName.SENTRY_DODGE)#make function get_ability_constants public
                                            score+=(ab1.area_of_effect+3*ab1.power+ab1.range-2*ab1.ap_cost-0.5*ab1.cooldown)
                                            if flag==1 and ab1.is_lobbing:
                                               score+=10
                                            ab1=world.get_ability_constants(AbilityName.SENTRY_RAY)#make function get_ability_constants public
                                            score=(ab1.area_of_effect+3*ab1.power+ab1.range-2*ab1.ap_cost-0.5*ab1.cooldown)
                                            if flag==1 and ab1.is_lobbing:
                                                score+=10
                                            heroconst=world.get_hero_constant(HeroName.SENTRY)#add function get_hero_constant
                                            score+=(3*heroconst.max_hp-heroconst.respawn_time-2*heroconst.move_ap_cost)
                                        elif i==1:
                                            ab1=world.get_ability_constants(AbilityName.BLASTER_ATTACK)#make function get_ability_constants public
                                            score+=(ab1.area_of_effect+3*ab1.power+ab1.range-2*ab1.ap_cost-0.5*ab1.cooldown)
                                            if flag==1 and ab1.is_lobbing:
                                                score+=10
                                            ab1=world.get_ability_constants(AbilityName.BLASTER_DODGE)#make function get_ability_constants public
                                            score+=(ab1.area_of_effect+3*ab1.power+ab1.range-2*ab1.ap_cost-0.5*ab1.cooldown)
                                            if flag==1 and ab1.is_lobbing:
                                               score+=10
                                            ab1=world.get_ability_constants(AbilityName.BLASTER_BOMB)#make function get_ability_constants public
                                            score+=(ab1.area_of_effect+3*ab1.power+ab1.range-2*ab1.ap_cost-0.5*ab1.cooldown)
                                            if flag==1 and ab1.is_lobbing:
                                                score+=10
                                            heroconst=world.get_hero_constant(HeroName.BLASTER)#add function get_hero_constant
                                            score+=(3*heroconst.max_hp-heroconst.respawn_time-2*heroconst.move_ap_cost)
                                        elif(i==2):
                                           ab1=world.get_ability_constants(AbilityName.HEALAR_ATTACK)#make function get_ability_constants public
                                           score+=(ab1.area_of_effect+3*ab1.power+ab1.range-2*ab1.ap_cost-0.5*ab1.cooldown)
                                           if flag==1 and ab1.is_lobbing:
                                               score+=10
                                           ab1=world.get_ability_constants(AbilityName.HEALAR_DODGE)#make function get_ability_constants public
                                           score+=(ab1.area_of_effect+3*ab1.power+ab1.range-2*ab1.ap_cost-0.5*ab1.cooldown)
                                           if flag==1 and ab1.is_lobbing:
                                               score+=10
                                           ab1=world.get_ability_constants(AbilityName.HEALAR_HEAL)#make function get_ability_constants public
                                           score+=ab1.area_of_effect+ab1.power+ab1.range-ab1.ap_cost-ab1.cooldown
                                           if flag==1 and ab1.is_lobbing:
                                               score+=10
                                           heroconst=world.get_hero_constant(HeroName.HEALER)#add function get_hero_constant
                                           score+=(3*heroconst.max_hp-heroconst.respawn_time-2*heroconst.move_ap_cost)
                                        elif(i==3):
                                           ab1=world.get_ability_constants(AbilityName.GUARDIAN_ATTACK)#make function get_ability_constants public
                                           score+=(ab1.area_of_effect+3*ab1.power+ab1.range-2*ab1.ap_cost-0.5*ab1.cooldown)
                                           if flag==1 and ab1.is_lobbing:
                                               score+=10
                                           ab1=world.get_ability_constants(AbilityName.GUARDIAN_DODGE)#make function get_ability_constants public
                                           score+=(ab1.area_of_effect+3*ab1.power+ab1.range-2*ab1.ap_cost-0.5*ab1.cooldown)
                                           if flag==1 and ab1.is_lobbing:
                                               score+=10
                                           ab1=world.get_ability_constants(AbilityName.GUARDIAN_BOMB)#make function get_ability_constants public
                                           score+=(ab1.area_of_effect+3*ab1.power+ab1.range-2*ab1.ap_cost-0.5*ab1.cooldown)
                                           if flag==1 and ab1.is_lobbing:
                                               score+=10
                                           heroconst=world.get_hero_constant(HeroName.GUARDIAN)#add function get_hero_constant
                                           score+=(3*heroconst.max_hp-heroconst.respawn_time-2*heroconst.move_ap_cost)
                                    score1=0               
                                    for i in opp:
                                        if(i==0):
                                            ab1=world.get_ability_constants(AbilityName.SENTRY_ATTACK)#make function get_ability_constants public
                                            score1+=(ab1.area_of_effect+3*ab1.power+ab1.range-2*ab1.ap_cost-0.5*ab1.cooldown)
                                            if flag==1 and ab1.is_lobbing:
                                                score1+=10
                                            ab1=world.get_ability_constants(AbilityName.SENTRY_DODGE)#make function get_ability_constants public
                                            score1+=(ab1.area_of_effect+3*ab1.power+ab1.range-2*ab1.ap_cost-0.5*ab1.cooldown)
                                            if flag==1 and ab1.is_lobbing:
                                               score1+=10
                                            ab1=world.get_ability_constants(AbilityName.SENTRY_RAY)#make function get_ability_constants public
                                            score1=(ab1.area_of_effect+3*ab1.power+ab1.range-2*ab1.ap_cost-0.5*ab1.cooldown)
                                            if flag==1 and ab1.is_lobbing:
                                                score1+=10
                                            heroconst=world.get_hero_constant(HeroName.SENTRY)#add function get_hero_constant
                                            score1+=(3*heroconst.max_hp-heroconst.respawn_time-2*heroconst.move_ap_cost)
                                        elif(i==1):
                                            ab1=world.get_ability_constants(AbilityName.BLASTER_ATTACK)#make function get_ability_constants public
                                            score1+=(ab1.area_of_effect+3*ab1.power+ab1.range-2*ab1.ap_cost-0.5*ab1.cooldown)
                                            if flag==1 and ab1.is_lobbing:
                                                score1+=10
                                            ab1=world.get_ability_constants(AbilityName.BLASTER_DODGE)#make function get_ability_constants public
                                            score1+=(ab1.area_of_effect+3*ab1.power+ab1.range-2*ab1.ap_cost-0.5*ab1.cooldown)
                                            if flag==1 and ab1.is_lobbing:
                                               score1+=10
                                            ab1=world.get_ability_constants(AbilityName.BLASTER_BOMB)#make function get_ability_constants public
                                            score1+=(ab1.area_of_effect+3*ab1.power+ab1.range-2*ab1.ap_cost-0.5*ab1.cooldown)
                                            if flag==1 and ab1.is_lobbing:
                                                score1+=10
                                            heroconst=world.get_hero_constant(HeroName.BLASTER)#add function get_hero_constant
                                            score1+=(3*heroconst.max_hp-heroconst.respawn_time-2*heroconst.move_ap_cost)
                                        elif(i==2):
                                           ab1=world.get_ability_constants(AbilityName.HEALAR_ATTACK)#make function get_ability_constants public
                                           score1+=(ab1.area_of_effect+3*ab1.power+ab1.range-2*ab1.ap_cost-0.5*ab1.cooldown)
                                           if flag==1 and ab1.is_lobbing:
                                               score1+=10
                                           ab1=world.get_ability_constants(AbilityName.HEALAR_DODGE)#make function get_ability_constants public
                                           score1+=(ab1.area_of_effect+3*ab1.power+ab1.range-2*ab1.ap_cost-0.5*ab1.cooldown)
                                           if flag==1 and ab1.is_lobbing:
                                               score1+=10
                                           ab1=world.get_ability_constants(AbilityName.HEALAR_HEAL)#make function get_ability_constants public
                                           score1+=ab1.area_of_effect+ab1.power+ab1.range-ab1.ap_cost-ab1.cooldown
                                           if flag==1 and ab1.is_lobbing:
                                               score1+=10
                                           heroconst=world.get_hero_constant(HeroName.HEALER)#add function get_hero_constant
                                           score1+=(3*heroconst.max_hp-heroconst.respawn_time-2*heroconst.move_ap_cost)
                                        elif(i==3):
                                           ab1=world.get_ability_constants(AbilityName.GUARDIAN_ATTACK)#make function get_ability_constants public
                                           score1+=(ab1.area_of_effect+3*ab1.power+ab1.range-2*ab1.ap_cost-0.5*ab1.cooldown)
                                           if flag==1 and ab1.is_lobbing:
                                               score1+=10
                                           ab1=world.get_ability_constants(AbilityName.GUARDIAN_DODGE)#make function get_ability_constants public
                                           score1+=(ab1.area_of_effect+3*ab1.power+ab1.range-2*ab1.ap_cost-0.5*ab1.cooldown)
                                           if flag==1 and ab1.is_lobbing:
                                               score1+=10
                                           ab1=world.get_ability_constants(AbilityName.GUARDIAN_BOMB)#make function get_ability_constants public
                                           score1+=(ab1.area_of_effect+3*ab1.power+ab1.range-2*ab1.ap_cost-0.5*ab1.cooldown)
                                           if flag==1 and ab1.is_lobbing:
                                               score1+=10
                                           heroconst=world.get_hero_constant(HeroName.GUARDIAN)#add function get_hero_constant
                                           score1+=(3*heroconst.max_hp-heroconst.respawn_time-2*heroconst.move_ap_cost)
                                    scoret=score1-score1
                                    value[count]=scoret
                                    count+=1
#                                    ###########################################    
#                     
if  __name__ == '__main__' :
      for i in range(8):
          print(i)       
      print(np.zeros([2,3]))     