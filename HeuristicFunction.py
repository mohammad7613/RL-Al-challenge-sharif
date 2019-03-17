from Model import *
import numpy as np
def Hp(world):

    sum=0
    dif=np.zeros(4)
    i=0
    for hero in world.my_heroes:
       dif[i]=hero.max_hp - hero.current_hp
       sum = sum + hero.max_hp
       i=i+1
    return  1-(dif.sum()/sum)
def hp_invision(world) :
    prod=0
    opp_hp=np.zeros(4)
    i=0
    for hero in world.opp_heroes:
        if hero.current_cell.row == -1:
            opp_hp[i]= 1
        else:
            opp_hp[i]=hero.current_hp
        i=i+1
    return np.prod(opp_hp)