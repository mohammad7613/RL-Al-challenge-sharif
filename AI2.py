
from Model import *
from random import randint
import numpy as np
import time
from queue import Queue
#############################################################functions
##################my hero
def get_path_move_directions(start_cell, end_cell, world):
    # doing a bfs from start until reaching end cell while keeping parents:

    visited_flag = np.zeros(31 ** 2)
    parents = {}
    path = []
    my_hero_pos = []
    for hero in world.my_heroes:
        my_hero_pos.append(hero.current_cell)
    front = Queue()
    front.put(start_cell)
    visited_flag[start_cell.row * 31 + start_cell.column] = 1

    while front.empty() is False:
        top = front.get()
        if top == end_cell:
            # initializing parent finder :
            while top != start_cell:
                parent = parents[top]
                if top.row < parent.row:
                    path.append(Direction.UP)
                elif top.row > parent.row:
                    path.append(Direction.DOWN)
                elif top.column > parent.column:
                    path.append(Direction.RIGHT)
                elif top.column < parent.column:
                    path.append(Direction.LEFT)
                top = parent
            path.reverse()
            return path

        if top.row < 30:
            new_cell = world.map.get_cell(row=top.row + 1, column=top.column)
            if visited_flag[new_cell.row * 31 + new_cell.column] == 0 and new_cell.is_wall is False:
                is_hero_in_new_cell = False
                for itr in my_hero_pos:
                    if itr == new_cell:
                        is_hero_in_new_cell = True
                if is_hero_in_new_cell is False:
                    visited_flag[new_cell.row * 31 + new_cell.column] = 1
                    parents[new_cell] = top
                    front.put(new_cell)
        if top.row > 0:
            new_cell = world.map.get_cell(row=top.row - 1, column=top.column)
            if visited_flag[new_cell.row * 31 + new_cell.column] == 0 and new_cell.is_wall is False:
                is_hero_in_new_cell = False
                for itr in my_hero_pos:
                    if itr == new_cell:
                        is_hero_in_new_cell = True
                if is_hero_in_new_cell is False:
                    visited_flag[new_cell.row * 31 + new_cell.column] = 1
                    parents[new_cell] = top
                    front.put(new_cell)
        if top.column < 30:
            new_cell = world.map.get_cell(row=top.row, column=top.column + 1)
            if visited_flag[new_cell.row * 31 + new_cell.column] == 0 and new_cell.is_wall is False:
                is_hero_in_new_cell = False
                for itr in my_hero_pos:
                    if itr == new_cell:
                        is_hero_in_new_cell = True
                if is_hero_in_new_cell is False:
                    visited_flag[new_cell.row * 31 + new_cell.column] = 1
                    parents[new_cell] = top
                    front.put(new_cell)
        if top.column > 0:
            new_cell = world.map.get_cell(row=top.row, column=top.column - 1)
            if visited_flag[new_cell.row * 31 + new_cell.column] == 0 and new_cell.is_wall is False:
                is_hero_in_new_cell = False
                for itr in my_hero_pos:
                    if itr == new_cell:
                        is_hero_in_new_cell = True
                if is_hero_in_new_cell is False:
                    visited_flag[new_cell.row * 31 + new_cell.column] = 1
                    parents[new_cell] = top
                    front.put(new_cell)

    return path
def my_heros_cells(world):
    CEL=[0,0,0,0]
    i=0
    for hero in world.my_heroes:
        CEL[i] = hero.current_cell
        i=i+1
    return CEL
def my_heroes_hp(world):
    hp = []
    for hero in  world.my_heroes :
        h = hero.current_hp
        hp.append(h)
    return hp
def my_heros_rows(world):
    ROW=[0,0,0,0]
    i=0
    for hero in world.my_heroes:
        ROW[i] = hero.current_cell.row
        i=i+1
    return ROW
def my_heros_columns(world):
    COL = [0, 0, 0, 0]
    i = 0
    for hero in world.my_heroes:
        COL[i] = hero.current_cell.column
        i = i + 1
    return COL
def my_hero_in_area(hero,world,area):
    l = 0
    for cell in area:
        if cell == hero.current_cell or (cell.row==hero.current_cell.row and cell.column==hero.current_cell.column ):
            l = l + 1
            break
    if l==0:
        return False
    elif l==1:
        return True
def my_hero_is_invision(world,hero):
    cellmyhero = hero.current_cell
    oppcellhero = oplive(world)
    i=0
    for cell in oppcellhero :
        if world.is_in_vision(cellmyhero,cell) is  True :
            i=1
            break
    if i==0 :
       return False
    elif i == 1:
       return True
##################opp hero
def opp_heros_cells(world):
    OPCEL = [0, 0, 0, 0]
    i = 0
    for ophero in world.opp_heroes:
        opcel = ophero.current_cell
        row = opcel.row
        if row != -1:
            OPCEL[i] = ophero.current_cell
        i = i + 1
    return OPCEL
def opp_heros_rows(world):
    OPROW = [0, 0, 0, 0]
    i = 0
    for ophero in world.opp_heroes:
        opcel = ophero.current_cell
        row = opcel.row
        if row != -1:
            OPROW[i] = ophero.current_cell.row
        i = i + 1
    return OPROW
def opp_heros_columns(world):
    OPCOL = [0, 0, 0, 0]
    i = 0
    for ophero in world.opp_heroes:
        opcel = ophero.current_cell
        row = opcel.row
        if row != -1:
            OPCOL[i] = ophero.current_cell.column
        i = i + 1
    return OPCOL
def opp_hero_in_area(hero,world,area):
    ol = 0
    for cell in area:
        if hero.current_cell.row != -1:
            if cell == hero.current_cell:
                ol = ol + 1
                break
    if ol==0 :
        return False
    if ol !=0:
        return True
def opp_hero_attacked(world,hero) :
    mycell = hero.current_cell
    l=0
    for opphero in world.opp_heroes:
        oppcell = opphero.current_cell
        if oppcell.row != -1:
            if hero.name is HeroName.BLASTER:
                r=world.get_ability_targets(ability_name=AbilityName.BLASTER_ATTACK, start_cell=mycell,target_cell=oppcell)
                if len(r)>0:
                   l = l + 1
            if hero is HeroName.GUARDIAN:
                r=world.get_ability_targets(ability_name=AbilityName.GUARDIAN_ATTACK, start_cell=mycell,target_cell=oppcell) 
                if len(r)>0:
                   l = l + 1
            if hero is HeroName.HEALER:
                r=world.get_ability_targets(ability_name=AbilityName.HEALER_ATTACK, start_cell=mycell,target_cell=oppcell)
                if len(r)>0:
                   l = l + 1
            if hero is HeroName.SENTRY:
                r=world.get_ability_targets(ability_name=AbilityName.SENTRY_ATTACK, start_cell=mycell,target_cell=oppcell)
                if len(r)>0:
                   l = l + 1
    return l
def oplive(world):
    opli=[]
    for hero in world.opp_heroes:
        if hero.current_cell.row !=-1:
            h=hero.current_cell
            opli.append(h)
    return opli
def get_nearest_opponent_distance(world, cell):
    heroes = world.get_opp_live_hero()
    minn = 31 * 31
    for hero in heroes:
        if hero.current_cell.row != -1:
            minn = min(world.manhattan_distance(cell, hero.current_cell), minn)
    return minn
def nearest_opphero(world,cell):
    e=get_nearest_opponent_distance(world,cell)
    ophero=world.get_opp_live_hero()
    if e==world.manhattan_distance(cell,ophero[0].current_cell):
        return ophero[0]
    elif e==world.manhattan_distance(cell,ophero[1].current_cell):
        return ophero[1]
    elif e==world.manhattan_distance(cell,ophero[2].current_cell):
        return ophero[2]
    elif e==world.manhattan_distance(cell,ophero[3].current_cell):
        return ophero[3]
def is_enemy_in_vision(world, cell, dis):
    heroes = world.opp_heroes
    for hero in heroes:
        if hero.current_cell.row != -1:
            if world.is_in_vision(start_cell=cell, end_cell=hero.current_cell) is True and \
                    world.manhattan_distance(start_cell=cell, end_cell=hero.current_cell) <= dis:
                return True
    return False
##################HERO Abilities
def distance_healer(world,cell) :
    mycel = cell
    dis = []
    opcel = oplive(world)
    for celll in opcel:
        d = world.manhattan_distance(start_cell=mycel,end_cell=celll)
        dis.append(d)
    return dis
def healpos(world,hero):
    c=world.map.objective_zone
    E = []
    T = []
    for cel in c:
        ui = cel.row
        iu = cel.column
        E.append(ui)
        T.append(iu)
    mxro = max(E)
    mxco = max(T)
    miro = min(E)
    mico = min(T)
    olv = oplive(world)
    mapo = world.map.cells
    senatk = []
    goodhealerpos = []
    for list in mapo:
        for cel in list:
            if cel.is_wall is False:
                if cel.row >= (miro - 3) and cel.row <= (mxro + 3) and cel.column >= (mico - 3) and cel.column <= (
                        mxco + 3):
                    dishealer = distance_healer(world, cel)
                    if my_hero_is_invision(world, hero) is False and len(dishealer)>0:
                       if min(dishealer) < 5 :
                          goodhealerpos.append(cel)
    print("goodhealerpos=", goodhealerpos)
    return goodhealerpos
def healer(world,opcels,opcel):

    ll=world.map.objective_zone
    posishen = []
    for cell in ll:
        if world.manhattan_distance(cell, opcel) == 4:
           posishen.append(cell)
    return posishen
def hero_heal(world,hero):
    cell=hero.current_cell
    ll=world.map.objective_zone
    posishen = []
    for cel in ll:
        if world.manhattan_distance(cel, cell) <= 4:
           posishen.append(cell)
    return posishen
def area_for_healer(world) :
    c = world.map.objective_zone
    E = []
    T = []
    for cel in c:
        ui = cel.row
        iu = cel.column
        E.append(ui)
        T.append(iu)
    mxro = max(E)
    mxco = max(T)
    miro = min(E)
    mico = min(T)
    mapo = world.map.cells
    area = []
    for list in mapo:
        for cel in list:
            if cel.is_wall is False:
                if cel.row >= (miro - 3) and cel.row <= (mxro + 3) and cel.column >= (mico - 3) and cel.column >= (
                        mxco + 3):
                    area.append(cel)
    return area
###################only cells and area
def nearest_cel(world,cel,cells):
    cell=[]
    f=[]
    for c in cells:
        dir=world.get_path_move_directions(start_cell=cel,end_cell=c)
        fasele=len(dir)
        f.append(fasele)
    a=min(f)
    for c in cells:
        dir = world.get_path_move_directions(start_cell=cel,end_cell=c)
        fasele = len(dir)
        if fasele==a:
            cell.append(c)
    return cell
def cell_in_direction(world,start_cell,end_cell):
    dir = world.get_path_move_directions(start_cell=start_cell,end_cell=end_cell)
    cel = []
    f= start_cell
    cel.append(f)
    for d in dir :
        c = world._get_next_cell(cell = f , direction= d)
        cel.append(c)
        f = c
    return cel
def pos(world,cel,d):
    map=world.map.cells
    posishen=[]
    for list in map:
        for cell in list :
            if cell.is_wall is False :
                if world.manhattan_distance(cell,cel)<d:
                    posishen.append(cell)

    return posishen
###################dodge

def dogcel(world,cell,end_cell,dr):
    map1 = world.map.cells
    ro=cell.row
    co=cell.column
    R=[ro+1,ro+2,ro+3,ro+4,ro-3,ro-4,ro-5]
    C=[co+1,co+2,co+3,co+4,co+5,co-3,co-4,co-5]
    area = []
    tolmasir = []
    g=None
    hhh = 31*31
    for r in R:
        for c in C:
            cel=world.map.get_cell(row=r,column=c)
            if world.manhattan_distance(start_cell=cell, end_cell=cel) < (dr + 1):
                area.append(cel)
    for cel in area:
        masir = world.get_path_move_directions(start_cell=cel, end_cell=end_cell)
        h = len(masir)
        if h < hhh:
            hhh = h
            tolmasir.append(cel)
            break
        h3 = len(tolmasir) - 1
        g = tolmasir[h3]
    return g
def bestdoge(world,start_cell,end_cell,dr):
    map1 = world.map.cells
    # BordDoge = world.hero.dodge_abilities
    BordDoge=dr
    area = []
    tolmasir =[]
    cell_direction = cell_in_direction(world,start_cell,end_cell)
    i = 0
    tol=[]
    g=[]
    fg=[]
    celdog=None
    for cell in cell_direction :
        area = []
        tolmasir = []
        for list  in map1 :
            for c in list:
                if world.manhattan_distance(start_cell=cell, end_cell=c) < dr + 1:
                    area.append(c)
        for cel in area :
            masir = world.get_path_move_directions(start_cell=cel, end_cell = end_cell)
            h = len(masir)
            tolmasir.append(h)
        for cel in area :
            masir = world.get_path_move_directions(start_cell=cel, end_cell=end_cell)
            h = len(masir)
            if h == min(tolmasir) :
                g.append(cel)
                break
        o=len(world.get_path_move_directions(start_cell=start_cell,end_cell=cell))
        od=min(tolmasir)+o
        fg.append(od)
        if od==min(fg):
            celdog=cell
    return celdog
  
####################################################################################################################
class AI2:



    def preprocess(self, world):

        print("preprocess")

    def pick(self, world):
        print("pick")
        print("im in pick AI2")
        world.pick_hero(HeroName.HEALER)
        world.pick_hero(HeroName.HEALER)
        world.pick_hero(HeroName.GUARDIAN)
        world.pick_hero(HeroName.GUARDIAN)


    def move(self, world):
        print("move")
        my_heroes_cel = my_heros_cells(world)
        opp=oplive(world)
        c = world.map.objective_zone

            #################################################################healer aval
        objective_zone_cells = world.map.objective_zone
        myhero = world.my_heroes

        cell0 = world.my_heroes[0].current_cell
        goodpos1 = healpos(world,myhero[0])
        dir0 = []
        healer_num1 = 0
        heroes_hp = my_heroes_hp(world)
        heal = AbilityName.HEALER_HEAL.name
        attack_healer = AbilityName.HEALER_ATTACK.name
        on_atak_healer = world.my_heroes[0].get_ability(attack_healer).is_ready()
        on_heal = world.my_heroes[0].get_ability(heal).is_ready()
        khatar_hero = []
        khatar = opp_hero_attacked(world, myhero[0])
        for hero in myhero :
            kh = opp_hero_attacked(world,hero)
            khatar_hero.append(kh)

        print("khatar_hero.append(kh)=",khatar_hero)
##################################### ES 1    :    go to best cell
        print("goodpos1=",goodpos1)
        if len(goodpos1)>0 :
           best_cell = nearest_cel(world,cell0,goodpos1)
           print("best_cell =",best_cell)
           dir1_0 = world.get_path_move_directions(start_cell=cell0,end_cell=best_cell[0])
           print("dir1_0",dir1_0)
           if len(dir1_0)==0 and healer_num1 == 0:
               healer_num1 = 1
           if len(dir1_0)>0 and healer_num1 == 0 :
               world.move_hero(hero=myhero[0],direction=dir1_0[0])
               healer_num1 = 1

####################################### ES 2     :  farar kone
        if khatar > 2 and healer_num1 == 0:
            min_khatar = min(khatar_hero)
            for heroo in myhero :
                if opp_hero_attacked(world,heroo) == min_khatar:
                    ce = heroo.current_cell
                    dir6_0 = world.get_path_move_directions(start_cell=cell0,end_cell=ce)
                    world.move_hero(hero=myhero[0], direction=dir6_0[0])
                    healer_num1 =1
####################################### ES 3       : heal kone
        if healer_num1 == 0 :
             goodcell2 = nearest_cel(world,cell0,objective_zone_cells)
             dir1_1 = world.get_path_move_directions(start_cell=cell0, end_cell=goodcell2[0])
             if len(dir1_1) > 0:
                 world.move_hero(hero=myhero[0], direction=dir1_1[0])
                 healer_num1 = 1
        if cell0.is_in_objective_zone is True and healer_num1==0 :
            if heroes_hp[0] < 70 and opp_hero_attacked(world,myhero[0]) > 0 and on_heal is True :
                healer_num1 =1
            if heroes_hp[2]<heroes_hp[3] and healer_num1==0 :
                if heroes_hp[2]<70 :
                    dir2_0 = world.get_path_move_directions(start_cell=cell0,end_cell=my_heroes_cel[2])
                    if world.manhattan_distance(cell0,my_heroes_cel[2])<=4 and on_heal is True:
                        healer_num1 = 1
                    elif  healer_num1==0 and len(dir2_0)>0:
                         world.move_hero(myhero[0],dir2_0[0])
            elif heroes_hp[3]<70 :
                dir3_0 = world.get_path_move_directions(start_cell=cell0,end_cell=my_heroes_cel[3])
                if world.manhattan_distance(cell0,my_heroes_cel[3])<=4 and on_heal is True :
                    healer_num1 = 1
                elif healer_num1 == 0 and len(dir3_0)>0:
                    world.move_hero(myhero[0],dir3_0[0])
######################################### ES 4         : attack kone   2  ##############################################
        if len(opp)>0 and cell0.is_in_objective_zone is True and heroes_hp[0]>70 and heroes_hp[2]>70 and heroes_hp[3]>70 and healer_num1==0 :
            near_op_hero= nearest_opphero(world,cell0)
            dir4_0 = world.get_path_move_directions(start_cell=cell0, end_cell=near_op_hero.current_cell)
            if world.manhattan_distance(cell0, near_op_hero.current_cell) <= 4 and on_atak_healer is True:
                healer_num1 =1
            elif healer_num1 == 0 and len(dir4_0)>0 :
               world.move_hero(myhero[0], dir4_0[0])
######################################## ES 5          : baghie ra heal kone
        if len(opp) ==0 :
            iii = [0,1,2,3]
            for ii in iii:
                if heroes_hp[ii] == min(heroes_hp):
                    dir5_0 = world.get_path_move_directions(start_cell=cell0, end_cell=my_heroes_cel[ii])
                    if world.manhattan_distance(cell0, my_heroes_cel[ii]) <= 4 and on_heal is True:
                        healer_num1 = 1
                    elif healer_num1 == 0 and len(dir5_0)>0:
                        world.move_hero(myhero[0], dir5_0[0])

        DO = world.get_path_move_directions(start_cell=my_heroes_cel[1], end_cell=c[10])
        if len(DO) > 0:
            world.move_hero(hero=world.my_heroes[1], direction=DO[0])
        DO = world.get_path_move_directions(start_cell=my_heroes_cel[2], end_cell=c[5])
        if len(DO) > 0:
            world.move_hero(hero=world.my_heroes[2], direction=DO[0])
        DO = world.get_path_move_directions(start_cell=my_heroes_cel[3], end_cell=c[15])
        if len(DO) > 0:
            world.move_hero(hero=world.my_heroes[3], direction=DO[0])

        ###################################
        world.Env_move_hero()


       ################################
        
       

    def action(self, world):
        print("action")
        
        mnn=world.my_score
        onn=world.opp_score
        print(mnn)
        print(onn)
        world.Env_action_hero()





