from Model import *
from random import randint
import numpy as np
from FeatureExtractor import feature_extractor
from NeuralNet import FeedForwardNeuralNet
from MiniMax import MiniMax
import evaluate_pick
class AI:
    def __init__(self,name):
        self.name = name
        self.network_input_dim = 100
        self.value_network = FeedForwardNeuralNet(is_training_on=False)
        self.value_network.addLayer("relu",self.network_input_dim,150,"hidden1")
        self.value_network.addLayer("relu", 150, 150, "hidden2")
        self.value_network.addLayer("relu", 150, 1, "output")
        self.pick_history =[]
    def preprocess(self, world):
        print(self.name + ": "+"preprocess")
        print(world.ability_constants.range)
        #features = feature_extractor(world,is_in_preprocess=True)
        #leaf_nodes = self.value_network.process(features)
        leaf_nodes = evaluate_pick(world)

        #leaf_nodes = np.random.randn(4**8)
        self.min_max_tree = MiniMax(leaf_nodes,4)
        self.min_max_tree.backup()

    def pick(self, world):
        print(self.name + ": "+"pick AI")
        # if len(world.opp_heroes) > 0 :
        #     opp_picked_hero = world.opp_heroes[-1].name
        #     print(self.name + ": "+"opponnent in the last round picked:{}".format(opp_picked_hero))
        #     if opp_picked_hero == HeroName.BLASTER:
        #         self.pick_history.append(1)
        #     if opp_picked_hero == HeroName.GUARDIAN:
        #         self.pick_history.append(3)
        #     if opp_picked_hero == HeroName.HEALER:
        #         self.pick_history.append(2)
        #     if opp_picked_hero == HeroName.SENTRY:
        #         self.pick_history.append(0)
        # value, pick_number = self.min_max_tree.best_action(self.pick_history)
        # self.pick_history.append(pick_number)
        # hero_names = [hero_name for hero_name in HeroName]
        # print(self.name + ": "+"we picked {} in this round!".format(hero_names[int(pick_number)].name))
        #
        world.pick_hero(HeroName.BLASTER)
        world.pick_hero(HeroName.BLASTER)
        world.pick_hero(HeroName.BLASTER)
        world.pick_hero(HeroName.BLASTER)


    def move(self, world):
        #print(self.name + ": "+"move")
        if world.current_turn == 4 and world.move_phase_num == 2:
            if world.my_heroes[0].id == 0 and self.name == "p1":
                #print("True")
                pass
            else:
                #print("False")
                pass

        dirs = [direction for direction in Direction]
        for hero in world.my_heroes:
            world.move_hero(hero=hero, direction=dirs[randint(0, len(dirs) - 1)])

    def action(self, world):
        #print(self.name + ": "+"action")
        for hero in world.my_heroes:
            row_num = randint(0, world.map.row_num)
            col_num = randint(0, world.map.column_num)
            abilities = hero.abilities
            world.cast_ability(hero=hero, ability=abilities[randint(0, len(abilities) - 1)],
                               cell=world.map.get_cell(row_num, col_num))
# class game:
#     def __init__(self,aherolist,game_Constant,mapjson):
#              self.beforeworld=None
#              self.currentworld=World();
#              #self.world_init(herolist,game_Constant,ability_list,Ap,mapjson)
#              self.score=0;
#              self.AI=AI
#              self.actins#array of action we can do in each phase
#              self.possibleaction=None
#              self.myturn=1
#              self.oppturn=0
#     def world_init(self,heroslisit,game_Constant,ability_list,Ap,mapjson=None):
#         if(mapjson==None):
#             with open('G:\filmuniversity\lessonfolder\4\aichallengeofsharif\map\AIC19-Maps-master\AIC19-Maps-master\practice\DiagonalOnline1.map') as mapf:
#                     mapjson=json.load(mapf)
#             self.currentworld._map_init(mapjson)
#         else:
#             self.currentworld._map_init(mapjson)
#         self.currentworld._heros_init(heroslisit)
#         self.currentworld._game_constant_init(game_Constant)
#         self.currentworld._ability_constants_init(ability_list)
#         self.currentworld.ap=Ap
#     def make_action(self,action):
#         self.beforesworld=self.currentworld
#         pass #determine the next using current state and action and compute the score and update it
#     def update_score():
#         pass
#     def undo_action(self):
#         self.currentworld=self.beforeworld
#     def get_possible_action(self):
#         actions={}
#         l=[]
#         heros=[]#contain heros that make action
#         heros1=[]#contain heros other heros
#         if(self.myturn==1):
#             heros=self.currentworld.get_my_live_heroes()
#             heros1=self.currentworld.get_opp_live_heroes()
#         else:
#             heros=self.currentworld.get_opp_live_heroes()
#             heros1=self.currentworld.get_my_live_heroes()
#
#         if self.currentworld.current_phase==Phase.MOVE:
#             for hero in heros:
#                 row=hero.current_cell.row-1
#                 if((self.currentworld.map.get_cell(row,hero.current_cell.column)==None)and(not self.currentworld.map.get_cell(row,hero.current_cell.column).is_wall )):
#                      l+=[Direction.UP]
#                 row=hero.current_cell.row+1
#                 if((self.currentworld.map.get_cell(row,hero.current_cell.column)==None)and(not self.currentworld.map.get_cell(row,column).is_wall )):
#                      l+=[Direction.DOWN]
#                 column=hero.current_cell.column+1
#                 if((self.currentworld.map.get_cell(heros.current_cell.row,column)==None)and(not self.currentworld.map.get_cell(heros.current_cell.row,column).is_wall )):
#                      l+=[Direction.LEFT]
#                 colmun=hero.current_cell.column-1
#                 if(self.currentworld.map.get_cell(heros.current_cell.row,column)==None and not self.currentworld.map.get_cell(heros.current_cell.row,column).is_wall ):
#                      l+=[Direction.RIGHT]
#                 action[hero.id]=l;
#                 l=[];
#             return action
#         if self.currentworld.current_phase==Phase.ACTION:
#             abilitis={}
#             actions={}
#             cells=[]
#             heroscells=[]
#             heros1cells=[]
#             for hero in heros:
#                 heroscells+=[hero.current_cell]
#             for hero in heros1:
#                 heros1cells+=[hero.current_cell]
#             ATTACK=[AbilityName.BLASTER_ATTACK,AbilityName.GUARDIAN_ATTACK,AbilityName.HEALER_ATTACK,AbilityName.SENTRY_ATTACK]
#             for hero in  heros:
#                 for ability in hero.abilities:
#                     if(ability.is_ready and abality.type== AbilityType.DODGE and abality.ap_cost<self.currentworld.ap):
#                            abilitis[ability.name]=[]
#                            for row in range(self.currentworld.map.row_num):
#                                for column in range(self.currentworld.map.column_num):
#                                    cell=self.currentworld.map.get_cell(row,column)
#                                    if(not cell.is_wall and not cell in heroscells):
#                                         abilitis[ability.name]+=[cell]
#
#                     if(ability.is_ready and ability.type==AbilityType.DEFENSIVE  and ability.ap_cost<self.currentworld.ap):
#                            abilitis[ability.type]=[]
#                            for row in range(self.currentworld.map.row_num):
#                                for column in range(self.currentworld.map.column_num):
#                                    cell=self.currentworld.map.get_cell(row,column)
#                                    if(not cell.is_wall and cell in heroscells and self.currentworld.manhattan_distance(cell,hero.current_cell)):
#                                         abilitis[ability.type]+=[cell]
#                     if(ability.is_ready and ability.name== AbilityName.BLASTER_BOMB and abality.ap_cost<self.currentworld.ap):
#                           abilitis[ability.name]=[]
#                           flag=np.zeros([31 ,31])
#                           for row in range(self.currentworld.map.row_num):
#                                for column in range(self.currentworld.map.column_num):
#                                    cell=self.currentworld.map.get_cell(row,column)
#                                    if(self.currentworld.manhattan_distance(cell,hero.current_cell)<ability.range ):
#                                            for hero1 in heros1:
#                                                if(self.currentworld.manhattan_distance(cell,heros1.current_cell)<ability.area_of_effect):
#                                                        flag[row][column]+=1
#                                                        if(max<flag[row][column]):
#                                                              max=flag[row][column]
#                                                              abilitis[ability.name]=[]
#                                                              abilitis[ability.name]+=[cell]
#                                                        else:
#                                                              abilitis[ability.name]+=[cell]
#                     if(ability.is_ready and ability.name== AbilityName.SENTRY_RAY  and abality.ap_cost<self.currentworld.ap):
#                           abilitis[ability.name]=[]
#                           for hero1 in heros1:
#                               if(self.currentworld.is_in_vision(hero1.current,hero.current_cell)):
#                                    abilitis[ability.name]+=[hero1.current_cell]
#                     if(ability.is_ready and ability.name in ATTACK   and abality.ap_cost<self.currentworld.ap):
#                           abilitis[ability.name]=[]
#                           flag=np.zeros([31 ,31])
#                           for row in range(self.currentworld.map.row_num):
#                                for column in range(self.currentworld.map.column_num):
#                                    cell=self.currentworld.map.get_cell(row,column)
#                                    if(self.currentworld.is_in_vision(cell,hero) and self.currentworld.manhattan_distance(cell,hero.current_cell)<ability.range ):
#                                            for hero1 in heros1:
#                                                if(self.currentworld.manhattan_distance(cell,heros1.current_cell)<ability.area_of_effect):
#                                                        flag[row][column]+=1
#                                                        if(max<flag[row][column]):
#                                                              max=flag[row][column]
#                                                              abilitis[ability.name]=[]
#                                                              abilitis[ability.name]+=[cell]
#                                                        else:
#                                                              abilitis[ability.name]+=[cell]
#                 actions[hero.id]=abilitis
