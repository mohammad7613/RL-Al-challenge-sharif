
import Model as Model
from Model import *
from random import randint



class AI2:



    def preprocess(self, world):


        global c

        global r
        r=world.map.my_respawn_zone

        # print(r[2])
        # print(c[2])
        print("preprocess")

    def pick(self, world):
        print("pick")
        # J=world.my_heroes
        # if len(J)==0:
        #     world.pick_hero(Model.HeroName.SENTRY)
        # elif len(J)==1:
        #     world.pick_hero(Model.HeroName.BLASTER)
        # elif len(J)==2:
        #     world.pick_hero(Model.HeroName.HEALER)
        # elif len(J)==3:
        #     world.pick_hero(Model.HeroName.GUARDIAN)
        # # if i == 1 :
        world.Env_pick_hero(HeroName.SENTRY)
        #     i=i+1
        # elif i==2 :
        print(world.counter)
        world.Env_pick_hero(HeroName.BLASTER)
        #     i=i+1
        # elif i == 3:
        print(world.counter)
        world.Env_pick_hero(HeroName.HEALER)
        #     i = i + 1
        # elif i == 4:
        print(world.counter)
        world.Env_pick_hero(HeroName.GUARDIAN)
        print(world.counter)
        print(world.myturn)
    def move(self, world):
        print("move")



   #      c = world.map.objective_zone
   #      toz=len(c)
   #      HP=[0,0,0,0]
   #      CEL=[0,0,0,0]
   #      COL=[0,0,0,0]
   #      ROW=[0,0,0,0]
   #      OPCEL=[0,0,0,0]
   #      OPROW=[0,0,0,0]
   #      OPCOL=[0,0,0,0]
   #      OPHP=[0,0,0,0]
   #      i=0
   #      for ophero in world.opp_heroes :
   #          if ophero != -1 and ophero != 0:
   #            OPHP[i]= ophero.current_hp
   #          i=i+1
   #      i=0
   #      for ophero in world.opp_heroes:
   #          if ophero != -1 and ophero != 0:
   #            OPCEL[i] = ophero.current_cell
   #            OPCOL[i]=OPCEL[i].column
   #            OPROW[i]= OPCEL[i].row
   #          i = i + 1
   #      i=0
   #      for hero in world.my_heroes :
   #          HP[i]= hero.current_hp
   #          i=i+1
   #      i=0
   #      for hero in world.my_heroes:
   #          CEL[i] = hero.current_cell
   #          COL[i]=CEL[i].column
   #          ROW[i]= CEL[i].row
   #          i = i + 1
   #      FAZ =world.move_phase_num
   #      xx = c[1].row
   #      yy = c[1].column
   #      xx1 = c[7].row
   #      yy1 = c[7].column
   #      xx2 = c[12].row
   #      yy2 = c[12].column
   #      xx3 = c[20].row
   #      yy3 = c[20].column
   #
   #      DO2 = world.get_path_move_directions(CEL[2], ROW[2], COL[2], c[12], xx2, yy2)
   #      DO = world.get_path_move_directions(CEL[0], ROW[0], COL[0], c[1], xx, yy)
   #      DO1 = world.get_path_move_directions(CEL[1], ROW[1], COL[1], c[7], xx1, yy1)
   #      DO3 = world.get_path_move_directions(CEL[3], ROW[3], COL[3], c[20], xx3, yy3)
   #
   #      l = 0
   #      i = 0
   #      for cell in c:
   #          if c[i] == CEL[0]:
   #              l = l + 1
   #              break
   #          i = i + 1
   #      l1 = 0
   #      i = 0
   #      for cell in c:
   #          if c[i] == CEL[1]:
   #              l1 = l + 1
   #              break
   #          i = i + 1
   #      l2 = 0
   #      i = 0
   #      for cell in c:
   #          if c[i] == CEL[2]:
   #              l2 = l + 1
   #              break
   #          i = i + 1
   #      l3 = 0
   #      i = 0
   #      for cell in c:
   #          if c[i] == CEL[3]:
   #              l3 = l + 1
   #              break
   #          i = i + 1
   #
   #      OPD=0
   #      if OPROW[0] != -1 and OPCOL[0] !=0 :
   #          OPD=world.get_path_move_directions(CEL[0],ROW[0],COL[0],OPCEL[0],OPROW[0],OPCOL[0])
   #          if len(OPD) > 0:
   #             world.move_hero(hero=world.my_heroes[0],direction=OPD[0])
   #      elif 0 < len(DO) and l<1:
   #          world.move_hero(hero=world.my_heroes[0],direction=DO[0])
   #      OPD1 = 0
   #      if OPROW[1] != -1 and OPCOL[1] != 0:
   #          OPD1 = world.get_path_move_directions(CEL[1], ROW[1], COL[1], OPCEL[1], OPROW[1], OPCOL[1])
   #          print(OPD1)
   #          if len(OPD1) > 0:
   #             world.move_hero(hero=world.my_heroes[1], direction=OPD1[0])
   #      elif 0 < len(DO1) and l1 < 1:
   #          world.move_hero(hero=world.my_heroes[1], direction=DO1[0])
   #      OPD2 = 0
   #      if OPROW[2] != -1 and OPCOL[2] != 0:
   #          OPD2 = world.get_path_move_directions(CEL[2], ROW[2], COL[2], OPCEL[2], OPROW[2],OPCOL[2])
   #          print(OPD2)
   #          if len(OPD2)>0 :
   #            world.move_hero(hero=world.my_heroes[2], direction=OPD2[0])
   #      elif 0 < len(DO2) and l2 < 1:
   #          world.move_hero(hero=world.my_heroes[2], direction=DO2[0])
   #      OPD3 = 0
   #      if OPROW[3] != -1 and OPCOL[3] != 0:
   #          OPD3 = world.get_path_move_directions(CEL[3], ROW[3], COL[3], OPCEL[3], OPROW[3], OPCOL[3])
   #          print(OPD3)
   #          if len(OPD3) > 0:
   #            world.move_hero(hero=world.my_heroes[3], direction=OPD3[0])
   #      elif 0 < len(DO3) and l3 < 1:
   #          world.move_hero(hero=world.my_heroes[3], direction=DO3[0])
   #      # if 0 > len(DO1) and l1<1:
   #      #     world.move_hero(hero=world.my_heroes[1], direction=DO1[0])
   #      # if 0 > len(DO2) and l2<1:
   #      #     world.move_hero(hero=world.my_heroes[2], direction=DO2[0])
   #      # if 0 > len(DO3) and l3<1:
   #      #     world.move_hero(hero=world.my_heroes[3], direction=DO3[0])
   #      # HEALERRRRRRRRRRRRRR
   #
   #      #    print(l)
   #
   #      #    DH = world.get_path_move_directions(CEL[2],ROW[2],COL[2],CEL[0],ROW[0],COL[0])
   #      #    DH1= world.get_path_move_directions(CEL[2], ROW[2], COL[2], CEL[1], ROW[1], COL[1])
   #      #    DH2= world.get_path_move_directions(CEL[2], ROW[2], COL[2], CEL[2], ROW[2], COL[2])
   #      #    DH3 = world.get_path_move_directions(CEL[2], ROW[2], COL[2], CEL[3], ROW[3], COL[3])
   #      #    w=world.ability.rem_cooldown(f[2])
   #      #    if w<1:
   #      #        if (120 - HP[0]) > 30 and (len(DH) - FAZ + 1) < 11 and world.manhattan_distance(CEL[0], CEL[2]) > 4:
   #      #            world.move_hero(hero=world.my_heroes[2], direction=DH[0])
   #      #        elif (250 - HP[1]) > 30 and (len(DH1) - FAZ + 1) < 11 and world.manhattan_distance(CEL[1], CEL[2]) > 4:
   #      #            world.move_hero(hero=world.my_heroes[2], direction=DH1[0])
   #      #        elif (200 - HP[2]) > 30 and (len(DH2) - FAZ + 1) < 11 and world.manhattan_distance(CEL[2], CEL[2]) > 4:
   #      #            world.move_hero(hero=world.my_heroes[2], direction=DH2[0])
   #      #        elif (400 - HP[3]) > 30 and (len(DH3) - FAZ + 1) < 11 and world.manhattan_distance(CEL[3], CEL[2]) > 4:
   #      #            world.move_hero(hero=world.my_heroes[2], direction=DH3[0])
   #      #        elif 0 != len(DO2) and l < 1:
   #      #            world.move_hero(hero=world.my_heroes[2], direction=DO2[0])
   #      #
   #      #    # ------------------------------------------------------------------------
   #      #    id= world.my_heroes[0].id
   #      #    id1=world.my_heroes[1].id
   #      #    id2 = world.my_heroes[2].id
   #      #    id3 = world.my_heroes[3].id
   #
   #      #    # if d[0]== Direction.DOWN :
   #      # d[0]=Model.Direction.DOWN
   #      # elif d[0]== Direction.LEFT:
   #      # d[0]=Model.Direction.LEFT
   #      # elif d[0]== Direction.UP:
   #      # d[0]=Model.Direction.UP
   #      # elif d[0]== Direction.RIGHT:
   #      # d[0]=Model.Direction.LEFT
   #      # if d1[0]== <Direction.DOWN: 'DOWN'> :
   #      # d1[0]=Model.Direction.DOWN
   #      # elif d1[0]==<Direction.LEFT: 'LEFT'>:
   #      # d1[0]=Model.Direction.LEFT
   #      # elif d1[0]==<Direction.UP: 'UP'>:
   #      # d1[0]=Model.Direction.UP
   #      # elif d1[0]==<Direction.RIGHT: 'RIGHT'>:
   #      # d1[0]=Model.Direction.LEFT
   #      # if d2[0]== <Direction.DOWN: 'DOWN'> :
   #      # d2[0]=Model.Direction.DOWN
   #      # elif d2[0]==<Direction.LEFT: 'LEFT'>:
   #      # d2[0]=Model.Direction.LEFT
   #      # elif d2[0]==<Direction.UP: 'UP'>:
   #      # d2[0]=Model.Direction.UP
   #      # elif d2[0]==<Direction.RIGHT: 'RIGHT'>:
   #      # d2[0]=Model.Direction.LEFT
   #      # if d3[0]== <Direction.DOWN: 'DOWN'> :
   #      # d3[0]=Model.Direction.DOWN
   #      # elif d3[0]==<Direction.LEFT: 'LEFT'>:
   #      # d3[0]=Model.Direction.LEFT
   #      # elif d3[0]==<Direction.UP: 'UP'>:
   #      # d3[0]=Model.Direction.UP
   #      # elif d3[0]==<Direction.RIGHT: 'RIGHT'>:
   #      # d3[0]=Model.Direction.LEFT
   #      #
   #      # if 0 != len(DO):
   #      #   world.move_hero(hero=world.my_heroes[0],direction=DO[0])
   #      # if 0 != len(DO1):
   #      #  world.move_hero(hero=world.my_heroes[1], direction=DO1[0])
   #      # if 0 != len(DO3) :
   #      #  world.move_hero(hero=world.my_heroes[3], direction=DO3[0])
   #      # # dirs = [direction for direction in Model.Direction]
   #      # # for hero in world.my_heroes:
   #      # #     world.move_hero(hero=hero, direction=dirs[randint(0, len(dirs) - 1)])
   #
        world.Env_move_hero()
    def action(self, world):
        print("action")
        t=world.my_heroes[0].defensive_abilities

        HP = [0, 0, 0, 0]
        CEL = [0, 0, 0, 0]
        COL = [0, 0, 0, 0]
        ROW = [0, 0, 0, 0]
        OPCEL = [0, 0, 0, 0]
        OPROW = [0, 0, 0, 0]
        OPCOL = [0, 0, 0, 0]
        OPHP = [0, 0, 0, 0]
        i = 0
        for ophero in world.opp_heroes:
            if ophero != -1 and ophero != 0:
                OPHP[i] = ophero.current_hp
            i = i + 1
        i = 0
        for ophero in world.opp_heroes:
            if ophero != -1 and ophero != 0:
                OPCEL[i] = ophero.current_cell
                OPCOL[i] = OPCEL[i].column
                OPROW[i] = OPCEL[i].row
            i = i + 1
        i = 0
        for hero in world.my_heroes:
            HP[i] = hero.current_hp
            i = i + 1
        i = 0
        for hero in world.my_heroes:
            CEL[i] = hero.current_cell
            COL[i] = CEL[i].column
            ROW[i] = CEL[i].row
            i = i + 1
        f = Model.AbilityName.BLASTER_BOMB
        j = Model.Hero.get_ability(world.my_heroes[0], f)
        j1 = Model.Hero.get_ability(world.my_heroes[1], f)
        j2 = Model.Hero.get_ability(world.my_heroes[2], f)
        j3 = Model.Hero.get_ability(world.my_heroes[3], f)
        h = (Model.Ability.is_ready(j))
        h1 = (Model.Ability.is_ready(j1))
        h2 = (Model.Ability.is_ready(j2))
        h3 = (Model.Ability.is_ready(j3))

        if (h is True) and OPCOL[0] != -1 and world.manhattan_distance(CEL[0],OPCEL[0])<5:
            world.cast_ability(hero=world.my_heroes[0],ability=j,cell=OPCEL[0])
        elif (h is True) and OPCOL[1] != -1 and world.manhattan_distance(CEL[0],OPCEL[1])<5:
            world.cast_ability(hero=world.my_heroes[0], ability=j, cell=OPCEL[1])
        elif (h is True) and OPCOL[2] != -1 and world.manhattan_distance(CEL[0], OPCEL[2]) < 5:
            world.cast_ability(hero=world.my_heroes[0], ability=j, cell=OPCEL[2])
        elif (h is True) and OPCOL[3] != -1 and world.manhattan_distance(CEL[0], OPCEL[3]) < 5:
            world.cast_ability(hero=world.my_heroes[0], ability=j, cell=OPCEL[3])
        #ghhjklkjhgfghjklkjhgfdfghjklkjhgfdfghjkl
        if (h1 is True) and OPCOL[1] != -1 and world.manhattan_distance(CEL[1],OPCEL[1])<5:
            world.cast_ability(hero=world.my_heroes[1],ability=j1,cell=OPCEL[1])
        elif (h1 is True) and OPCOL[0] != -1 and world.manhattan_distance(CEL[1],OPCEL[0])<5:
            world.cast_ability(hero=world.my_heroes[1], ability=j1, cell=OPCEL[0])
        elif (h1 is True) and OPCOL[2] != -1 and world.manhattan_distance(CEL[1], OPCEL[2]) < 5:
            world.cast_ability(hero=world.my_heroes[1], ability=j1, cell=OPCEL[2])
        elif (h1 is True) and OPCOL[3] != -1 and world.manhattan_distance(CEL[1], OPCEL[3]) < 5:
            world.cast_ability(hero=world.my_heroes[1], ability=j1, cell=OPCEL[3])
        #dsfghjkljhgfrdesdfghjkljhygtrfews
        if (h2 is True) and OPCOL[2] != -1 and world.manhattan_distance(CEL[2],OPCEL[2])<5:
            world.cast_ability(hero=world.my_heroes[2],ability=j2,cell=OPCEL[2])
        elif (h2 is True) and OPCOL[1] != -1 and world.manhattan_distance(CEL[2],OPCEL[1])<5:
            world.cast_ability(hero=world.my_heroes[2], ability=j2, cell=OPCEL[1])
        elif (h2 is True) and OPCOL[0] != -1 and world.manhattan_distance(CEL[2], OPCEL[0]) < 5:
            world.cast_ability(hero=world.my_heroes[2], ability=j2, cell=OPCEL[0])
        elif (h2 is True) and OPCOL[3] != -1 and world.manhattan_distance(CEL[2], OPCEL[3]) < 5:
            world.cast_ability(hero=world.my_heroes[2], ability=j2, cell=OPCEL[3])
        #fghjkhfdsdfghjkjhgfdfghjk
        if (h3 is True) and OPCOL[3] != -1 and world.manhattan_distance(CEL[3],OPCEL[3])<5:
            world.cast_ability(hero=world.my_heroes[3],ability=j3,cell=OPCEL[3])
        elif (h3 is True) and OPCOL[1] != -1 and world.manhattan_distance(CEL[3],OPCEL[1])<5:
            world.cast_ability(hero=world.my_heroes[3], ability=j3, cell=OPCEL[1])
        elif (h3 is True) and OPCOL[2] != -1 and world.manhattan_distance(CEL[3], OPCEL[2]) < 5:
            world.cast_ability(hero=world.my_heroes[3], ability=j3, cell=OPCEL[2])
        elif (h3 is True) and OPCOL[0] != -1 and world.manhattan_distance(CEL[3], OPCEL[0]) < 5:
            world.cast_ability(hero=world.my_heroes[3], ability=j3, cell=OPCEL[0])

        # if( h1 is True) and OPCOL[1] != -1 and world.manhattan_distance(CEL[1],OPCEL[1])<5:
        #     world.cast_ability(hero=world.my_heroes[1],ability=j1,cell=OPCEL[1])
        # if (h2 is True ) and OPCOL[2] != -1 and world.manhattan_distance(CEL[2],OPCEL[2])<5:
        #     world.cast_ability(hero=world.my_heroes[2],ability=j2,cell=OPCEL[2])
        # if (h3 is True) and OPCOL[3] != -1 and world.manhattan_distance(CEL[3],OPCEL[3])<5:
        #     world.cast_ability(hero=world.my_heroes[3],ability=j3,cell=OPCEL[3])
        f = Model.AbilityName.BLASTER_ATTACK
        j = Model.Hero.get_ability(world.my_heroes[0], f)
        j1 = Model.Hero.get_ability(world.my_heroes[1], f)
        j2 = Model.Hero.get_ability(world.my_heroes[2], f)
        j3 = Model.Hero.get_ability(world.my_heroes[3], f)
        h = (Model.Ability.is_ready(j))
        h1 = (Model.Ability.is_ready(j1))
        h2 = (Model.Ability.is_ready(j2))
        h3 = (Model.Ability.is_ready(j3))
        bomc= world.get_impact_cell(ability=j,start_cell=CEL[0],target_cell=OPCEL[0])
        bomc1 = world.get_impact_cell(ability=j, start_cell=CEL[0], target_cell=OPCEL[1])
        bomc2 = world.get_impact_cell(ability=j, start_cell=CEL[0], target_cell=OPCEL[2])
        bomc3 = world.get_impact_cell(ability=j, start_cell=CEL[0], target_cell=OPCEL[3])
        if ( h is True) and bomc==OPCEL[0] :
            world.cast_ability(hero=world.my_heroes[0],ability=j,cell=OPCEL[0])
        elif (h is True) and bomc1 == OPCEL[1]:
            world.cast_ability(hero=world.my_heroes[0], ability=j, cell=OPCEL[1])
        elif (h is True) and bomc2 == OPCEL[2]:
            world.cast_ability(hero=world.my_heroes[0], ability=j, cell=OPCEL[2])
        elif (h is True) and bomc3 == OPCEL[3]:
            world.cast_ability(hero=world.my_heroes[0], ability=j, cell=OPCEL[3])

        bomc = world.get_impact_cell(ability=j1, start_cell=CEL[1], target_cell=OPCEL[0])
        bomc1 = world.get_impact_cell(ability=j1, start_cell=CEL[1], target_cell=OPCEL[1])
        bomc2 = world.get_impact_cell(ability=j1, start_cell=CEL[1], target_cell=OPCEL[2])
        bomc3 = world.get_impact_cell(ability=j1, start_cell=CEL[1], target_cell=OPCEL[3])
        if (h1 is True) and bomc1 == OPCEL[1]:
            world.cast_ability(hero=world.my_heroes[1], ability=j1, cell=OPCEL[1])
        elif (h1 is True) and bomc == OPCEL[0]:
            world.cast_ability(hero=world.my_heroes[1], ability=j1, cell=OPCEL[0])
        elif (h1 is True) and bomc2 == OPCEL[2]:
            world.cast_ability(hero=world.my_heroes[1], ability=j1, cell=OPCEL[2])
        elif (h1 is True) and bomc3 == OPCEL[3]:
            world.cast_ability(hero=world.my_heroes[1], ability=j1, cell=OPCEL[3])

        bomc = world.get_impact_cell(ability=j2, start_cell=CEL[2], target_cell=OPCEL[0])
        bomc1 = world.get_impact_cell(ability=j2, start_cell=CEL[2], target_cell=OPCEL[1])
        bomc2 = world.get_impact_cell(ability=j2, start_cell=CEL[2], target_cell=OPCEL[2])
        bomc3 = world.get_impact_cell(ability=j2, start_cell=CEL[2], target_cell=OPCEL[3])
        if (h2 is True) and bomc2 == OPCEL[2]:
            world.cast_ability(hero=world.my_heroes[2], ability=j2, cell=OPCEL[2])
        elif (h2 is True) and bomc1 == OPCEL[1]:
            world.cast_ability(hero=world.my_heroes[2], ability=j2, cell=OPCEL[1])
        elif (h2 is True) and bomc == OPCEL[0]:
            world.cast_ability(hero=world.my_heroes[2], ability=j2, cell=OPCEL[0])
        elif (h2 is True) and bomc3 == OPCEL[3]:
            world.cast_ability(hero=world.my_heroes[2], ability=j2, cell=OPCEL[3])

        bomc = world.get_impact_cell(ability=j3, start_cell=CEL[3], target_cell=OPCEL[0])
        bomc1 = world.get_impact_cell(ability=j3, start_cell=CEL[3], target_cell=OPCEL[1])
        bomc2 = world.get_impact_cell(ability=j3, start_cell=CEL[3], target_cell=OPCEL[2])
        bomc3 = world.get_impact_cell(ability=j3, start_cell=CEL[3], target_cell=OPCEL[3])
        if (h3 is True) and bomc3 == OPCEL[3]:
            world.cast_ability(hero=world.my_heroes[3], ability=j3, cell=OPCEL[3])
        elif (h3 is True) and bomc1 == OPCEL[1]:
            world.cast_ability(hero=world.my_heroes[3], ability=j3, cell=OPCEL[1])
        elif (h3 is True) and bomc2 == OPCEL[2]:
            world.cast_ability(hero=world.my_heroes[3], ability=j3, cell=OPCEL[2])
        elif (h3 is True) and bomc == OPCEL[0]:
            world.cast_ability(hero=world.my_heroes[3], ability=j3, cell=OPCEL[0])
        # if  HP[0]<200 and( h is True):
        #     world.cast_ability(hero=world.my_heroes[0],ability= j,cell= CEL[0])
        # if  HP[1]<200 and (h1 is True):
        #     world.cast_ability(hero=world.my_heroes[1],ability= j1, cell=CEL[1])
        # if  HP[2]<200 and (h2 is True) :
        #     world.cast_ability(hero=world.my_heroes[2], ability=j2, cell=CEL[2])
        # if  HP[3]<200 and (h3 is True) :
        #     world.cast_ability(hero=world.my_heroes[3], ability=j3, cell=CEL[3])
        f = Model.AbilityName.BLASTER_DODGE
        j = Model.Hero.get_ability(world.my_heroes[0], f)
        j1 = Model.Hero.get_ability(world.my_heroes[1], f)
        j2 = Model.Hero.get_ability(world.my_heroes[2], f)
        j3 = Model.Hero.get_ability(world.my_heroes[3], f)
        h = (Model.Ability.is_ready(j))
        h1 = (Model.Ability.is_ready(j1))
        h2 = (Model.Ability.is_ready(j2))
        h3 = (Model.Ability.is_ready(j3))
        if( h is True)  and OPCOL[0] == -1 :
            world.cast_ability(hero=world.my_heroes[0], ability=j, cell=world.map.get_cell(ROW[0]+randint(-4, 4), COL[0]+randint(-4, 4)))
        if (h1 is True) and OPCOL[1] == -1:
            world.cast_ability(hero=world.my_heroes[1],ability= j1, cell=world.map.get_cell(ROW[1]+randint(-4, 4), COL[1]+randint(-4, 4)))
        if (h2 is True) and OPCOL[2] == -1:
            world.cast_ability(hero=world.my_heroes[2],ability= j2, cell=world.map.get_cell(ROW[2]+randint(-4, 4), COL[2]+randint(-4, 4)))
        if (h3 is True) and OPCOL[3] == -1:
            world.cast_ability(hero=world.my_heroes[3],ability= j3, cell=world.map.get_cell(ROW[3]+randint(-4, 4), COL[3]+randint(-4, 4)))
        s= world.my_score
        e= world.opp_score
        print(s)
        print(e)
        # world.hero.get_ability(Model.AbilityName.GUARDIAN_FORTIFY)
   #      f = world.my_heroes[2].ability_names
   #      print(f)
   #      HP = [0, 0, 0, 0]
   #      CEL = [0, 0, 0, 0]
   #      COL = [0, 0, 0, 0]
   #      ROW = [0, 0, 0, 0]
   #      i=0
   #      for hero in world.my_heroes:
   #          HP[i] = hero.current_hp
   #          i = i + 1
   #      i = 0
   #      for hero in world.my_heroes:
   #          CEL[i] = hero.current_cell
   #          COL[i] = CEL[i].column
   #          ROW[i] = CEL[i].row
   #          i = i + 1
   #          # healer heeeel
   #      # healer=Model.AbilityName.HEALER_HEAL
   #      # z=
   #      # #z=healer.world.ability.rem_cooldown
   #      # if z==0:
   #      if (120 - HP[0]) > 40 and world.manhattan_distance(CEL[0], CEL[2]) < 5:
   #              world.cast_ability(hero=world.my_heroes[2], ability=Model.AbilityName.HEALER_HEAL, cell=CEL[0])
   #      elif (250 - HP[1]) > 40 and world.manhattan_distance(CEL[1], CEL[2]) > 5:
   #              world.cast_ability(hero=world.my_heroes[2], ability=Model.AbilityName.HEALER_HEAL, cell=CEL[1])
   #      elif (400 - HP[3]) > 40 and world.manhattan_distance(CEL[3], CEL[2]) > 5:
   #              world.cast_ability(hero=world.my_heroes[2], ability=Model.AbilityName.HEALER_HEAL, cell=CEL[3])
   #      elif (200 - HP[2]) > 40 and world.manhattan_distance(CEL[2], CEL[2]) > 5:
   #              world.cast_ability(hero=world.my_heroes[2], ability=Model.AbilityName.HEALER_HEAL, cell=CEL[2])
   # #------------------------------------------------------------
   #      # h = world.current_cell(Model.HeroName.SENTRY)
   #      # h1 = world.current_cell(Model.HeroName.BLASTER)
   #      # h2 = world.current_cell(Model.HeroName.HEALER)
   #      # h3 = world.current_cell(Model.HeroName.GUARDIAN)
   #      # hp= world.Hero.current_hp(Model.HeroName.SENTRY)
   #      # hp1=world.Hero.current_hp(Model.HeroName.BLASTER)
   #      # hp2=world.Hero.current_hp(Model.HeroName.HEALER)
   #      # hp3=world.Hero.current_hp(Model.HeroName.GUARDIAN)
   #      # dhp=120-hp
   #      # dhp1=250-hp1
   #      # dhp2=200-hp2
   #      # dhp3=400-hp3
   #      #     if dhp > 40 and dhp > dhp1 and dhp > dhp2 and dhp > dhp3 and world.manhattan_distance(h,h2)<5:
   #      #         world.cast_ability(Model.HeroName.HEALER,Model.AbilityName.HEALER_HEAL , h)
   #      #     if dhp1 > 40 and dhp1 > dhp and dhp1 > dhp2 and dhp1 > dhp3 and world.manhattan_distance(h1,h2)<5:
   #      #         world.cast_ability(Model.HeroName.HEALER,Model.AbilityName.HEALER_HEAL , h1)
   #      #     if dhp2 > 40 and dhp2 > dhp1 and dhp2 > dhp and dhp2 > dhp3:
   #      #         world.cast_ability(Model.HeroName.HEALER,Model.AbilityName.HEALER_HEAL , h2)
   #      #     if dhp3 > 40 and dhp3 > dhp1 and dhp3 > dhp2 and dhp3 > dhp and world.manhattan_distance(h3,h2)<5:
   #      #         world.cast_ability(Model.HeroName.HEALER,Model.AbilityName.HEALER_HEAL , h3)
   #      # if world.Ability.is_ready(Model.AbilityName.GUARDIAN_FORTIFY) :
   #      #     if dhp > 40 and dhp > dhp1 and dhp > dhp2 and dhp > dhp3 and world.manhattan_distance(h, h3) < 5:
   #      #         world.cast_ability(Model.HeroName.GUARDIAN, Model.AbilityName.GUARDIAN_FORTIFY, h)
   #      #     if dhp1 > 40 and dhp1 > dhp and dhp1 > dhp2 and dhp1 > dhp3 and world.manhattan_distance(h1, h3) < 5:
   #      #         world.cast_ability(Model.HeroName.GUARDIAN, Model.AbilityName.GUARDIAN_FORTIFY, h1)
   #      #     if dhp2 > 40 and dhp2 > dhp1 and dhp2 > dhp and dhp2 > dhp3 and world.manhattan_distance(h2,h3):
   #      #         world.cast_ability(Model.HeroName.GUARDIAN, Model.AbilityName.GUARDIAN_FORTIFY, h2)
   #      #     if dhp3 > 40 and dhp3 > dhp1 and dhp3 > dhp2 and dhp3 > dhp and world.manhattan_distance(h3, h3) < 5:
   #      #         world.cast_ability(Model.HeroName.GUARDIAN, Model.AbilityName.GUARDIAN_FORTIFY, h3)
   #      # H=world.opp_heroes
   #      # oh=world.Hero.current_cell(H[0])
   #      # oh1 = world.Hero.current_cell(H[1])
   #      # oh2 = world.Hero.current_cell(H[2])
   #      # oh3 = world.Hero.current_cell(H[3])
   #      # ohp = world.Hero.current_hp(H[0])
   #      # ohp1 = world.Hero.current_hp(H[1])
   #      # ohp2 = world.Hero.current_hp(H[2])
   #      # ohp3 = world.Hero.current_hp(H[3])
   #      #
   #      # if world.Ability.is_ready(Model.AbilityName.SENTRY_RAY) :
   #      #     R=world.get_ray_cells(h,oh)
   #      #     R1 = world.get_ray_cells(h, oh1)
   #      #     R2 = world.get_ray_cells(h, oh2)
   #      #     R3 = world.get_ray_cells(h, oh3)
   #      #     if R==oh:
   #      #         world.cast_ability(Model.HeroName.SENTRY, Model.AbilityName.SENTRY_RAY, oh)
   #      #
   #      #     elif R1 == oh1:
   #      #         world.cast_ability(Model.HeroName.SENTRY, Model.AbilityName.SENTRY_RAY, oh1)
   #      #
   #      #
   #      #     elif R2 == oh2:
   #      #         world.cast_ability(Model.HeroName.SENTRY, Model.AbilityName.SENTRY_RAY, oh2)
   #      #
   #      #     elif R3 == oh3:
   #      #         world.cast_ability(Model.HeroName.SENTRY, Model.AbilityName.SENTRY_RAY, oh3)
   #          # SH = world.get_ability_targets("SENTRY_RAY", h, oh)
   #          # if H[0] == SH[0] or H[0] == SH[1] or H[0] == SH[2] or H[0] == SH[3]:
   #          #     world.cast_ability("SENTRY", "SENTRY_RAY", oh)
   #          # SH1 = world.get_ability_targets("SENTRY_RAY", h, oh1)
   #          # if H[1] == SH1[0] or H[1] == SH1[1] or H[1] == SH1[2] or H[1] == SH1[3]:
   #          #     world.cast_ability("SENTRY", "SENTRY_RAY", oh1)
   #          # SH2 = world.get_ability_targets("SENTRY_RAY", h, oh2)
   #          # if H[2] == SH2[0] or H[2] == SH2[1] or H[2] == SH2[2] or H[2] == SH2[3]:
   #          #     world.cast_ability("SENTRY", "SENTRY_RAY", oh2)
   #          # SH3 = world.get_ability_targets("SENTRY_RAY", h, oh3)
   #          # if H[3] == SH3[0] or H[3] == SH3[1] or H[3] == SH3[2] or H[3] == SH3[3]:
   #          #     world.cast_ability("SENTRY", "SENTRY_RAY", oh3)
   #      # if world.Ability.is_ready(Model.AbilityName.BLASTER_BOMB) :
   #      #     if world.manhattan_distance(h1,oh)>-1 and world.manhattan_distance(h1,oh)<6 :
   #      #         world.cast_ability(Model.HeroName.HEALER,Model.AbilityName.BLASTER_BOMB , oh)
   #      #     if world.manhattan_distance(h1, oh) > -1 and world.manhattan_distance(h1, oh) < 6:
   #      #         world.cast_ability(Model.HeroName.HEALER,Model.AbilityName.BLASTER_BOMB , oh1)
   #      #     if world.manhattan_distance(h1, oh) > -1 and world.manhattan_distance(h1, oh) < 6:
   #      #         world.cast_ability(Model.HeroName.HEALER,Model.AbilityName.BLASTER_BOMB , oh2)
   #      #     if world.manhattan_distance(h1, oh) > -1 and world.manhattan_distance(h1, oh) < 6:
   #      #         world.cast_ability(Model.HeroName.HEALER,Model.AbilityName.BLASTER_BOMB , oh3)
   #

        # for hero in world.my_heroes:
        #     row_num = randint(0, world.map.row_num)
        #     col_num = randint(0, world.map.column_num)
        #     abilities = hero.abilities
        #     world.cast_ability(hero=hero, ability=abilities[randint(0, len(abilities) - 1)],
        #cell=world.map.get_cell(row_num, col_num)
        world.Env_action_hero()