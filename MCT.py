# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 17:50:00 2019

@author: mandy
"""
import json
import numpy as np
from Model import *
from AI2 import AI2
from AI3 import AI3
class game:
    def __init__(self,client1,client2):
             self.client1=client1
             self.client2=client2
             self.beforeworld=None
             self.currentworld=World();
             self.world_init()
             #self.AI=AI
             self.possibleaction=None
             self.possiblemove=None
    def world_init(self,mapjson=None):
        if(mapjson==None):
            with open("C:/Users/mandy/Desktop/aichallengeofsharif/map/AIC19-Maps-1.0/practice/DiagonalOnline1.map") as mapf:
                    mapjson=json.load(mapf)
            self.currentworld.map_init(mapjson["map"])
            self.currentworld.Envgame_constant_init(mapjson["gameConstants"])
            self.currentworld.ability_constants_init(mapjson["abilityConstants"])
            self.currentworld.Env_hero_constant_init(mapjson["heroConstants"])
        #this is for init hero
        self.handel_pick()


    def make_action(self,action): 
        self.beforesworld=self.currentworld
        if self.currentworld.current_phase==Phase.MOVE:
            self.currentworld.Env_move_hero(action)
        elif self.currentworld.current_phase==Phase.ACTION:
            self.currentworld.Env_action_hero(action)
    def update_score(self):
        pass
    def undo_action(self):
        self.currentworld=self.beforeworld
    def get_possible_action(self):
        actions={}
        l=[]
        heros=[]#contain heros that make action 
        heros1=[]#contain other heros
        if(self.currentworld.myturn==1):
            heros=self.currentworld.get_my_live_heroes()
            heros1=self.currentworld.get_opp_live_heroes()
        else:
            heros=self.currentworld.get_opp_live_heroes()
            heros1=self.currentworld.get_my_live_heroes()
            
        if self.currentworld.current_phase==Phase.MOVE:
            heroscells=[]
            for hero in heros:
                heroscells+=[hero.current_cell]
            for hero in heros:
                if(self.currentworld.ap>hero.move_ap_cost):
                    row = hero.current_cell.row - 1
                    cell=self.currentworld.map.get_cell(row=row, column=hero.current_cell.column)
                    if((cell==None)and(cell.is_wall is not True )and not cell in heroscells):
                        l+=[Direction.UP]
                    row=hero.current_cell.row+1
                    cell = self.currentworld.map.get_cell(row=row, column=hero.current_cell.column)
                    if ((cell == None) and (cell.is_wall is not True) and not cell in heroscells):
                        l+=[Direction.DOWN]
                    column=hero.current_cell.column-1
                    cell = self.currentworld.map.get_cell(row=hero.current_cell.row,column=column)
                    if ((cell == None) and (cell.is_wall is not True) and not cell in heroscells):
                        l+=[Direction.LEFT]
                    column=hero.current_cell.column+1
                    cell = self.currentworld.map.get_cell(row=hero.current_cell.row,column=column)
                    if ((cell == None) and (cell.is_wall is not True) and not cell in heroscells):
                        l+=[Direction.RIGHT]
                    l+=[None]
                    actions[hero.id]=l
                    l=[]
                else:
                    actions[hero.id] = [None]
            self.collect_possible_action(heros, actions)
        if self.currentworld.current_phase==Phase.ACTION:
            actions={}
            heroscells=[]
            heros1cells=[]
            for hero in heros:
                heroscells+=[hero.current_cell]
            for hero in heros1:
                heros1cells+=[hero.current_cell]
            ATTACK=[AbilityName.BLASTER_ATTACK,AbilityName.GUARDIAN_ATTACK,AbilityName.HEALER_ATTACK,AbilityName.SENTRY_ATTACK]
            for hero in  heros:
                abilitis={}
                for ability in hero.abilities:
                    if(ability.is_ready and ability.type== AbilityType.DODGE and ability.ap_cost<self.currentworld.ap):
                           abilitis[ability]=[]
                           for row in range(self.currentworld.map.row_num):
                               for column in range(self.currentworld.map.column_num):
                                   cell=self.currentworld.map.get_cell(row,column)
                                   if(not cell.is_wall and not cell in heroscells and self.currentworld.manhattan_distance(cell,hero.current_cell)<ability.range):
                                       if (self.currentworld.is_in_vision(cell,hero) and self.currentworld.manhattan_distance(cell, hero.current_cell) < ability.range):
                                           for hero1 in heros:
                                               if (self.currentworld.manhattan_distance(cell,hero1.current_cell) < ability.area_of_effect):
                                                   flag[row][column] += 1
                                                   if (max < flag[row][column]):
                                                       max = flag[row][column]
                                                       abilitis[ability] = []
                                                       abilitis[ability] += [cell]
                                                   else:
                                                       abilitis[ability] += [cell]
                                        
                    if(ability.is_ready and ability.type==AbilityType.DEFENSIVE  and ability.ap_cost<self.currentworld.ap):
                           abilitis[ability]=[]
                           for row in range(self.currentworld.map.row_num):
                               for column in range(self.currentworld.map.column_num):
                                   cell=self.currentworld.map.get_cell(row,column)
                                   if(self.currentworld.manhattan_distance(cell,hero.current_cell)<ability.range ):
                                        abilitis[ability.type]+=[cell]
                    if(ability.is_ready and ability.name== AbilityName.BLASTER_BOMB and ability.ap_cost<self.currentworld.ap):
                          abilitis[ability]=[]
                          flag=np.zeros([31 ,31])
                          for row in range(self.currentworld.map.row_num):
                               for column in range(self.currentworld.map.column_num):
                                   cell=self.currentworld.map.get_cell(row,column)
                                   if(self.currentworld.manhattan_distance(cell,hero.current_cell)<ability.range ):
                                           for hero1 in heros1:
                                               if(self.currentworld.manhattan_distance(cell,heros1.current_cell)<ability.area_of_effect):
                                                       flag[row][column]+=1
                                                       if(max<flag[row][column]):
                                                             max=flag[row][column]
                                                             abilitis[ability]=[]
                                                             abilitis[ability]+=[cell]
                                                       else:
                                                             abilitis[ability]+=[cell]
                    if(ability.is_ready and ability.name== AbilityName.SENTRY_RAY  and ability.ap_cost<self.currentworld.ap):
                          abilitis[ability]=[]
                          for hero1 in heros1:
                              if(self.currentworld.is_in_vision(hero1.current,hero.current_cell)):
                                   abilitis[ability]+=[hero1.current_cell]
                    if(ability.is_ready and ability.name in ATTACK   and ability.ap_cost<self.currentworld.ap):
                          abilitis[ability]=[]
                          flag=np.zeros([31 ,31])
                          for row in range(self.currentworld.map.row_num):
                               for column in range(self.currentworld.map.column_num):
                                   cell=self.currentworld.map.get_cell(row,column)
                                   if(self.currentworld.is_in_vision(cell,hero) and self.currentworld.manhattan_distance(cell,hero.current_cell)<ability.range ):
                                           for hero1 in heros1:
                                               if(self.currentworld.manhattan_distance(cell,hero1.current_cell)<ability.area_of_effect):
                                                       flag[row][column]+=1
                                                       if(max<flag[row][column]):
                                                             max=flag[row][column]
                                                             abilitis[ability]=[]
                                                             abilitis[ability]+=[cell]
                                                       else:
                                                             abilitis[ability]+=[cell]
                abilitis["None"]=None
                actions[hero.id]=abilitis
            self.collect_possible_action(heros,actions)
    def collect_possible_action(self,hero,actions):
            self.possibleaction=[]
            if self.currentworld.current_phase==Phase.ACTION:
                for abilitya in actions[hero[0].id]:
                    for abilityb in  actions[hero[1].id]:
                        for abilityc in actions[hero[2].id]:
                            for abilityd in actions[hero[3].id]:
                                ap_cost=0
                                if abilitya is not "None":
                                    ap_cost+=abilitya.ap_cost
                                if abilityb is not "None":
                                    ap_cost += abilityb.ap_cost
                                if abilityc is not "None":
                                    ap_cost += abilityb.ap_cost
                                if abilityd is not "None":
                                    ap_cost += abilityd.ap_cost
                                if ap_cost<self.currentworld.ap:
                                    self.possibleaction+=[{hero[0].id:{abilitya:actions[hero[0].id][abilitya]},
                                                           hero[1].id:{abilityb:actions[hero[1].id][abilityb]},
                                                           hero[2].id:{abilityc:actions[hero[2].id][abilityc]},
                                                           hero[3].id:{abilityd:actions[hero[3].id][abilityd]}}]
                self.discrete_cell(hero)
            if self.currentworld.current_phase==Phase.MOVE:
                for direction1 in actions[hero[0].id]:
                    for direction2 in actions[hero[1].id]:
                        for direction3 in actions[hero[2].id]:
                            for direction4 in actions[hero[3].id]:
                                ap_cost=0
                                if(direction1 is not None):
                                    ap_cost+=hero[0].move_ap_cost
                                if (direction2 is not None):
                                    ap_cost += hero[1].move_ap_cost
                                if (direction3 is not None):
                                    ap_cost += hero[2].move_ap_cost
                                if (direction4 is not None):
                                    ap_cost += hero[3].move_ap_cost
                                if ap_cost<self.currentworld.ap:
                                    self.possiblemove += [{hero[0].id:direction1,hero[1].id:direction2,hero[2].id:direction3,hero[3].id:direction4}]
    def discrete_cell(self,hero):
        temp=self.possibleaction
        self.possibleaction=[]
        for item in temp:
            for ability1 in item[hero[0].id]:# this 'for' have one iteration        so we can omit  these for loops  but i dom=nt know the syntax
                for ability2 in item[hero[1].id]:# this 'for' have one iteration
                    for ability3 in item[hero[2].id]:# this 'for' have one iteration
                        for ability4 in item[hero[3].id]:# this 'for' have one iteration
                            for cell1 in item[hero[0].id][ability1]:
                                for cell2 in item[hero[1].id][ability2]:
                                    for cell3 in item[hero[2].id][ability3]:
                                         for cell4 in item[hero[1].id][ability2]:
                                             self.possibleaction+=[{hero[0].id:{ability1:cell1},
                                                                   hero[1].id:{ability2:cell2},
                                                                   hero[2].id:{ability3:cell3},
                                                                   hero[3].id:{ability4:cell4}}]
    def handel_pick(self):
        self.client1.pick(self.currentworld)
        print(self.currentworld.myturn)
        self.currentworld.Env_pick_hero()
        print(self.currentworld.myturn)
        self.client2.pick(self.currentworld)
        self.currentworld.Env_pick_hero()
        print(self.currentworld.myturn)
    def handle_move(self):
        self.client1.move(game.currentworld)
        self.currentworld.Env_move_hero()
        self.client2.move(game.currentworld)
        self.currentworld.Env_move_hero()
    def handle_action(self):
        self.client1.action(game.currentworld)
        self.currentworld.Env_action_hero()
        self.client2.action(game.currentworld)
        self.currentworld.Env_action_hero()

    def run(self):
        while self.currentworld.game_over is False:
            if (self.currentworld.current_phase == Phase.MOVE):
                self.handle_move()
            elif (self.currentworld.current_phase == Phase.ACTION):
                self.handle_action()
                print("myturn:{},myscore:{},oppscore:{}".format(game.currentworld.current_turn,game.currentworld.my_score,game.currentworld.opp_score))
            for hero in self.currentworld.my_heroes:
                print("heroid:{},heroname:{},herohealth:{},heroposition:({},{})".format(hero.id,hero.name,hero.current_hp,hero.current_cell.row,hero.current_cell.column))
            for hero  in self.currentworld.opp_heroes:
                print("heroid:{},heroname:{},herohealth:{},heroposition:({},{})".format(hero.id,hero.name,hero.current_hp,hero.current_cell.row,hero.current_cell.column))
        delattr(game,"currentworld")
        print("world")




if __name__ == '__main__':
   player1 = AI2()
   player2 = AI3()
   game=game(player1,player2)
   for cell in game.currentworld.map.objective_zone:
       print(cell.row)
       print(cell.column)
   game.run()







